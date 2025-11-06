produit = {
    'id': 101, 
    'nom': 'Clavier', 
    'prix': 250.0, 
    'stock': 15
}

# 1 Afficher toutes les clés du dictionnaire
print(produit.keys())

# 2 Afficher toutes les valeurs.
print(produit.values())

# 3 Afficher chaque clé → valeur sur une ligne.
for key in produit :
    val = produit[key]
    print(f"clé:{key} → valeur:{val}")

# 4 Modifier le prix du produit à 300.0.
produit['prix'] = 300
print(produit)

# 5 Ajouter une nouvelle clé 'couleur' avec la valeur 'noir'
couleur = input("Ajouter un couleur : ")
produit['couleur'] = couleur
print(produit)

# 6 Supprimer la clé 'stock'
del produit['stock']
print(produit)


