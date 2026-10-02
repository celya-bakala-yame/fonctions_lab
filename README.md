# Les fonctions en Python

Ce dépôt regroupe les exemples et l’exercice du chapitre sur les fonctions.

main.py présente la récursion avec la factorielle, l’introspection avec inspect et dis, et la manipulation des fonctions comme objets. Il contient également des exemples d’arguments positionnels et nommés, de *args et **kwargs, de closures et de fonctions lambda.

decorateurs.py contient un décorateur de chronométrage utilisant wraps et nonlocal. Il affiche la durée de chaque appel, leur cumul et le temps global de l’appel extérieur. La suite de Fibonacci permet de comparer une version récursive sans cache avec une version utilisant lru_cache.

Le cumul des durées récursives peut compter plusieurs fois les mêmes intervalles de temps. Il ne représente donc pas le temps global du calcul. Les mesures affichées dépendent aussi du coût des traces dans la console.

valeurs_defaut.py illustre le partage involontaire d’une liste utilisée comme valeur par défaut et sa correction avec None. Il compare également une date calculée à la définition de la fonction avec une date calculée au moment de l’appel.

Des doctests vérifient les résultats des fonctions, le fonctionnement des closures, les arguments, la conservation des métadonnées et la réutilisation des résultats du cache.

Pour exécuter les exemples :

uv run python main.py
uv run python decorateurs.py
uv run python valeurs_defaut.py

Pour exécuter tous les doctests :

uv run python -m doctest -v main.py decorateurs.py valeurs_defaut.py