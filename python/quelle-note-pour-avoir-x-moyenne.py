def note_ramener_sur20():
    note_pas_20=float(input("note à ramener sur 20: "))
    la_note_total=float(input("la note max: "))
    note_sur_20=note_pas_20/la_note_total*20
    round(note_sur_20,2)
    return note_sur_20

def la_note():
    nombre_de_note=int(input("combien de note: "))
    lesnotes=[]
    lescoeff=[]
    note_et_coeff=[]
    note_et_coeff_total=0
    coeff_total=0
    for i in range (nombre_de_note):
        print("c'est pour la ",i+1," note")
        special=str(input("la note doit etre ramener ou non sur 20: "))
        if special=="oui":
                note=note_ramener_sur20()
                coeff=(float(input("quelle est le coef de cette note: ")))
        else:
            note=(float(input("quelle est la note: ")))
            coeff=(float(input("quelle est le coef de cette note: ")))
        lesnotes.append(note)
        lescoeff.append(coeff)
    

    for o in range(len(lescoeff)):
        coeff_total+=lescoeff[o]

    for l in range(nombre_de_note):    
        note_et_coeff.append(lesnotes[l]*lescoeff[l])

    for j in range (len(note_et_coeff)):
        note_et_coeff_total+=note_et_coeff[j]

    la_moyenne_à_avoir=float(input("quelle est la moyenne à atteindre: "))
    
    moyenne=note_et_coeff_total/coeff_total         #permet d'avoir la moyenne
    moyenne=round(moyenne,2)        #permet d'arondir la moyenne
    
    print ("la moyenne est ici",moyenne)

    coeff_de_la_note=float(input("quelle est le coeff de la note à avoir"))

    nouveaucoeff=coeff_total+coeff_de_la_note   
    
    note_finale=(la_moyenne_à_avoir*nouveaucoeff-note_et_coeff_total)/coeff_de_la_note
    round(note_finale,2)
    print("il te faut au minimum: ",note_finale)

la_note()