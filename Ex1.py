"""
## ================ 1 ================
## Creation d'un mot aprés l'ajoute le longeur  
# mot = ""
# i = 1
# N = int(input("Entrer longeur de mot : "))

# while i < N :
#     n = input(f"lettre {i} : ")
#     mot += n
#     i += 1

# print(mot)
"""


"""
## ================ 2 ================
# Longeur de mot
mot = "INFO S1 FSSM"
print(len(mot))

# Le premier et dernier caracter de mot
print(mot[0],mot[-1])

# Les 5 premiers caractères
print(mot[:5:])

# Les caractères de position paire (0, 2, 4, ...).
for index in range(len(mot)) :
    if index % 2 == 0 :
        print(mot[index])
"""


"""
## ================ 3 ================
mot = "INFO S1 FSSM"
for letter in mot :
    print(letter , end='*')
"""

"""
## ================ 4 ================
mot = "INFO S1 FSSM"
aux = list(mot)
mot2 = ""
Ind = aux.index("1")
print(f"index of 1 : {Ind}")
aux[Ind] = "2"
for letter in aux :
    mot2 += letter

print(f"Mot2 modifiant : {mot2}")
print(type(mot2))
"""