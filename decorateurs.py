from contextlib import redirect_stdout
from functools import lru_cache, wraps
from io import StringIO
from time import perf_counter


def clock(func):
    """
    >>> @clock
    ... def addition(a, b=0):
    ...     return a + b
    >>> sortie = StringIO()
    >>> with redirect_stdout(sortie):
    ...     resultat = addition(2, b=3)
    >>> resultat
    5
    >>> addition.__name__
    'addition'
    >>> addition.statistiques["appels"]
    1
    >>> addition.statistiques["temps_global"] >= 0
    True
    >>> "addition(2, b=3)" in sortie.getvalue()
    True
    """
    calls = 0
    profondeur = 0
    debut_global = None
    cumul = 0.0

    statistiques = {
        "appels": 0,
        "temps_cumule": 0.0,
        "temps_global": 0.0,
    }

    @wraps(func)
    def clocked(*args, **kwargs):
        nonlocal calls, profondeur, debut_global, cumul

        debut = perf_counter()

        if profondeur == 0:
            debut_global = debut

        profondeur += 1

        try:
            result = func(*args, **kwargs)
        finally:
            profondeur -= 1

        fin = perf_counter()
        duree = fin - debut
        calls += 1
        cumul += duree

        statistiques["appels"] = calls
        statistiques["temps_cumule"] = cumul

        arglist = [repr(arg) for arg in args]
        arglist.extend(
            f"{cle}={valeur!r}"
            for cle, valeur in kwargs.items()
        )
        argstr = ", ".join(arglist)

        print(
            f"appel : {calls:4d} | "
            f"durée : {duree:.8f} s | "
            f"{func.__name__}({argstr}) = {result!r} | "
            f"cumul : {cumul:.8f} s"
        )

        if profondeur == 0:
            statistiques["temps_global"] = perf_counter() - debut_global
            print(
                f"Temps global : "
                f"{statistiques['temps_global']:.8f} s"
            )

        return result

    clocked.statistiques = statistiques
    return clocked


@clock
def fib(n):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)


@lru_cache(maxsize=None)
@clock
def fib_cache(n):
    if n < 2:
        return n
    return fib_cache(n - 2) + fib_cache(n - 1)


def verifier_fibonacci():
    """
    >>> sortie = StringIO()
    >>> with redirect_stdout(sortie):
    ...     resultat = fib(10)
    >>> resultat
    55
    >>> fib_cache.cache_clear()
    >>> with redirect_stdout(sortie):
    ...     resultat_cache = fib_cache(10)
    >>> resultat_cache == resultat
    True
    >>> fib_cache.cache_info().misses
    11
    >>> appels = fib_cache.__wrapped__.statistiques["appels"]
    >>> fib_cache(10)
    55
    >>> fib_cache.__wrapped__.statistiques["appels"] == appels
    True
    """


if __name__ == "__main__":
    print("Fibonacci sans cache")
    print(fib(10))
    print(fib.statistiques)

    print("Fibonacci avec cache")
    print(fib_cache(10))
    print(fib_cache.__wrapped__.statistiques)
    print(fib_cache.cache_info())

    print("Deuxième appel avec cache")
    print(fib_cache(10))
    print(fib_cache.cache_info())