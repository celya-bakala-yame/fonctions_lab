from datetime import datetime


def ajouter_partage(valeur, elements=[]):
    """
    >>> ajouter_partage.__defaults__[0].clear()
    >>> ajouter_partage(1)
    [1]
    >>> ajouter_partage(2)
    [1, 2]
    >>> ajouter_partage.__defaults__[0].clear()
    """
    elements.append(valeur)
    return elements


def ajouter_separe(valeur, elements=None):
    """
    >>> ajouter_separe(1)
    [1]
    >>> ajouter_separe(2)
    [2]
    >>> elements = []
    >>> ajouter_separe(1, elements)
    [1]
    >>> ajouter_separe(2, elements)
    [1, 2]
    """
    if elements is None:
        elements = []
    elements.append(valeur)
    return elements


def log_fixe(message, when=datetime.now()):
    """
    >>> log_fixe("Bonjour")[0] is log_fixe("Bonsoir")[0]
    True
    """
    return when, message


def log_dynamique(message, when=None):
    """
    >>> instant = datetime(2026, 10, 2, 14, 0)
    >>> log_dynamique("Bonjour", instant)
    (datetime.datetime(2026, 10, 2, 14, 0), 'Bonjour')
    >>> isinstance(log_dynamique("Bonjour")[0], datetime)
    True
    """
    if when is None:
        when = datetime.now()
    return when, message


if __name__ == "__main__":
    print(ajouter_partage(1))
    print(ajouter_partage(2))

    print(ajouter_separe(1))
    print(ajouter_separe(2))

    elements = []
    print(ajouter_separe(1, elements))
    print(ajouter_separe(2, elements))

    print(log_fixe("Bonjour"))
    print(log_fixe("Bonsoir"))

    print(log_dynamique("Bonjour"))
    print(log_dynamique("Bonsoir"))