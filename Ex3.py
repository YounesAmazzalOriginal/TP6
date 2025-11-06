# Une voiture est caractérisée par son matricule, sa marque, son modèle et son prix.
# Proposer un programme en python qui permet d’enregistrer les informations de n
# voitures et afficher celle la plus chère

data = []
n = int(input("Entrer le nombre n de voiture : "))

for i in range(n):
    print()
    voitures = {}

    nom = input(f"Entrer le nom voiture {i+1} : ")
    matricule = input(f"Entrer la matricule voiture {i+1} : ")
    marque = input(f"Entrer la marque voiture {i+1} : ")
    modèle = input(f"Entrer le modèle voiture {i+1} : ")
    prix = float(input(f"Entrer le prix voiture {i+1} : "))
    while prix < 0 :
        prix = int(input(f"Entrer le prix voiture {i+1} : "))
    
    voitures['voiture'] = nom
    voitures['matricule'] = matricule
    voitures['marque'] = marque
    voitures['modèle'] = modèle
    voitures['prix'] = prix

    data.append(voitures)

print(data)
print()

"""
Example de data :
data = [
    {'voiture': 'Toyota', 'matricule': '111111', 'marque': 'Vs', 'modèle': '45', 'prix': 1000000},
    {'voiture': 'BMW', 'matricule': '222222', 'marque': 'BMMMM', 'modèle': '11', 'prix': 5412000},
    {'voiture': 'Mercedes', 'matricule': '333333', 'marque': 'C-Class', 'modèle': '2020', 'prix': 3500000},
    {'voiture': 'Audi', 'matricule': '444444', 'marque': 'A4', 'modèle': '2019', 'prix': 2800000},
    {'voiture': 'Honda', 'matricule': '555555', 'marque': 'Civic', 'modèle': '2018', 'prix': 1200000},
    {'voiture': 'Ford', 'matricule': '666666', 'marque': 'Focus', 'modèle': '2017', 'prix': 900000},
    {'voiture': 'Nissan', 'matricule': '777777', 'marque': 'Altima', 'modèle': '2021', 'prix': 1500000},
    {'voiture': 'Chevrolet', 'matricule': '888888', 'marque': 'Malibu', 'modèle': '2019', 'prix': 1300000},
    {'voiture': 'Kia', 'matricule': '999999', 'marque': 'Sportage', 'modèle': '2020', 'prix': 1100000},
    {'voiture': 'Hyundai', 'matricule': '101010', 'marque': 'Elantra', 'modèle': '2022', 'prix': 1400000}
]
"""


voiture_plus_chere = None
max = 0
for voiture in data :
    if voiture["prix"] > max :
        max = voiture["prix"]
        voiture_plus_chere = voiture

print(f"max prix : {max}")
print(f"max prix voiture : {voiture_plus_chere}")