def remplacer_si_correspondance(d1, d2):
    for k, v in d1.items():
        if k in d2 and d2[k] != v:
            # Remplacer par la nouvelle version (exemple : ici on ajoute "_modifié")
            d2[k] = f"{v}"
    return d2

# Exemple :
d1 = {'a': '1', 'b': '6'}
d2 = {'a': '1', 'b': '4', 'c': '3'}

resultat = remplacer_si_correspondance(d1, d2)
print(resultat)
