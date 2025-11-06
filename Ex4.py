# ========= 1 =========
notes_etudiants = {
    "NomE" : ["M1","M2","M3","M4","M5","M6"] ,
    "Said" : [14,12,15,16,18,15] ,
    "Sara" : [15,17,14,18,17,16] ,
    "Sami" : [13,14,16,15,14,14] ,
    "Mina" : [16,15,17,17,19,18] ,
}


# ========= 2 =========
 for key in notes_etudiants :
     notes = notes_etudiants[key]
    
     print(key , end=" ")
    
     for note in notes :
         print(note , end=" ")
    
     print()


# ========= 3 =========
# La moyenne de chaque étudiant,
for key in notes_etudiants :
    s = 0
    m = 0
    val = notes_etudiants[key]
    if key == "NomE" :
        continue
    for note in val :
        s = s + note
        m = s / len(val)
        m = round(m,2)
        # rounde pour prendre just 2 point apre la virgule
    print(f"{key} : {m}")
    s , m = 0 , 0

