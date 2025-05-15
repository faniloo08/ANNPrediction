import pandas as pd

# Génération des 500 itérations
# La fonction de base est Xn+1 = A * Xn * (1 - Xn) = f(Xn)
# Sachant que la valeur initiale X0 = 0.1

def generer_données(A):
    x = [0.1]  # Initialisation avec X0 = 0.1
    for i in range(1, 501):  # Boucle de 1 à 500
        x.append(round(A * x[i-1] * (1 - x[i-1]), 8))  # Calcul et arrondi
    
    return x  # Retourner toute la liste

# Générer les séries pour A = 2 et A = 4.2
croissance_2 = generer_données(2)
croissance_4_2 = generer_données(4.2)

# Stocker dans un DataFrame avec la colonne temps
df = pd.DataFrame({
    "temps": list(range(501)),  # Génère les indices de 0 à 500
    "croissance_A2": croissance_2,
    "croissance_A4_2": croissance_4_2
})

# Enregistrer en CSV
df.to_csv("../data/serie_temporelle.csv", index=False)

print("Fichier sauvegardé : ../data/serie_temporelle.csv")