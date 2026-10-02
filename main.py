import inspect
import timeit
from dis import dis
from math import factorial


def fact(n):
    """
    >>> fact(0)
    1
    >>> fact(5)
    120
    >>> fact(10) == factorial(10)
    True
    >>> fact(-1)
    Traceback (most recent call last):
        ...
    ValueError: n doit être positif ou nul
    """
    if n < 0:
        raise ValueError("n doit être positif ou nul")
    return 1 if n < 2 else n * fact(n - 1)


def create_adder(x):
    """
    >>> add_5 = create_adder(5)
    >>> add_5(8)
    13
    >>> create_adder(-2)(5)
    3
    """
    def adder(y):
        return x + y

    return adder


def create_multiplier(x):
    """
    >>> create_multiplier(3)(7)
    21
    >>> create_multiplier(0)(7)
    0
    """
    def multiplier(y):
        return x * y

    return multiplier


def change_value(x, fonction):
    """
    >>> change_value(10, create_adder(5))
    15
    >>> change_value(10, create_multiplier(3))
    30
    """
    return fonction(x)


def trigger(seuil, nombres):
    """
    >>> trigger(50, [11, 12, 36, 78, 50])
    [11, 12, 36]
    >>> trigger(50, [])
    []
    """
    return [nombre for nombre in nombres if nombre < seuil]


def trigger2(seuil, *args):
    """
    >>> trigger2(50, 11, 12, 36, 78)
    [11, 12, 36]
    >>> trigger2(50)
    []
    >>> trigger2(50, *[10, 50, 70])
    [10]
    """
    return [nombre for nombre in args if nombre < seuil]


def calcul(arg1=0, arg2=1, arg3=0):
    """
    >>> calcul(3, 4, 5)
    -4.25
    >>> calcul(3, 4)
    0.75
    >>> calcul()
    0.0
    >>> calcul(arg3=5, arg2=4, arg1=3)
    -4.25
    """
    return arg1 / arg2 - arg3


def arguments(*args, **kwargs):
    """
    >>> arguments(1, 2, couleur="bleu")
    ((1, 2), {'couleur': 'bleu'})
    >>> arguments()
    ((), {})
    """
    return args, kwargs


def ajouter(valeur, elements=None):
    """
    >>> ajouter(1)
    [1]
    >>> ajouter(2)
    [2]
    >>> elements = []
    >>> ajouter(1, elements)
    [1]
    >>> ajouter(2, elements)
    [1, 2]
    """
    if elements is None:
        elements = []
    elements.append(valeur)
    return elements


if __name__ == "__main__":
    print(fact(5))

    print(timeit.timeit(lambda: fact(200), number=5))
    print(timeit.timeit(lambda: factorial(200), number=5))

    try:
        fact(10_000)
    except RecursionError:
        print("Limite de récursion atteinte")

    print(len(str(factorial(1000))))

    print(type(fact))
    print(callable(fact))
    print(dir(fact))
    print(fact.__code__.co_argcount)
    print(fact.__code__.co_consts)
    print(fact.__code__.co_filename)
    print(fact.__code__.co_name)
    print(fact.__code__.co_varnames)
    print(inspect.signature(fact))
    dis(fact)

    add_5 = create_adder(5)
    mul_3 = create_multiplier(3)

    print(add_5(8))
    print(mul_3(7))
    print(change_value(10, add_5))
    print(change_value(10, mul_3))

    fonctions = [add_5, mul_3]
    print([fonction(10) for fonction in fonctions])
    print(add_5.__closure__[0].cell_contents)

    nombres = [11, 12, 36, 78, 50]
    print(trigger(50, nombres))
    print(trigger2(50, *nombres))
    print(trigger2(50))

    print(calcul(3, 4, 5))
    print(calcul(arg3=5, arg2=4, arg1=3))
    print(arguments(1, 2, 3, couleur="bleu", taille=10))

    print(ajouter(1))
    print(ajouter(2))

    pairs = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]
    print(sorted(pairs, key=lambda pair: pair[1]))
    print(sorted(pairs, key=lambda pair: len(pair[1])))
    print(list(map(lambda x: x * 2, range(5))))
    print(list(filter(lambda x: x % 2 == 0, range(5))))