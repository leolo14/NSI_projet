
# Fonction d'affichage :

def afficher_grille(grille):
    """ Prend en entrée une grille de type liste et affiche une grille 9x9 """
    if len(grille[8]) == 9:
        for i in range(9):
            for j in range(9):
                print(grille[i][j], end='|')
            print()
    else:
        for i in range (9):
            print(grille_vide[i], "\n", end= "")


# Fonctions de création / modification :

def creer_grille(grille_vide,n=0):
    while not len(grille_vide[n]) ==9:
        x = int(input("Inserez un chiffre : " ))
        grille_vide[n].append(x), afficher_grille(grille_vide)
        return creer_grille(grille_vide, n)
    if len(grille_vide[8]) == 9:
        print("Grille complète !")
        return afficher_grille(grille_vide)
    x=int(input("Inserez un chiffre : "))
    grille_vide[n+1].append(x), afficher_grille(grille_vide)
    return creer_grille(grille_vide, n+1)

    
def modifier_case(a,b,grille):
    m = grille[a][b]
    grille[a][b] = "X"
    print(grille[a]," \n X =",m)
    x = int(input("Entrez le chiffre que vous souhaitez : "))
    afficher_grille(grille)
    print("Le chiffre", m,"sera remplacé par :",x)
    choix = int(input("Êtes-vous sur de vouloir faire ce changement ? \n 1: Oui  0: Non  -> "))
    if choix ==1:
        grille[a][b]= x
        return afficher_grille(grille)
    else :
        grille[a][b] = m

    

# Fonctions de résolution :


def trouver_case_vide(grille):
    for i in range(9):
        for j in range(9):
            if grille[i][j] == 0 :
                return(i, j)
    


def est_valide(grille, num, position):
    for i in range(9):
        if grille[position[0]][i] == num and position[1] != i \
           or grille[i][position[1]]== num and position[0] != i:
            return False
    sous_grille_x, sous_grille_y = position[1]//3, position[0] //3
    for i in range(sous_grille_y * 3, sous_grille_y * 3 + 3):
        for j in range(sous_grille_x * 3, sous_grille_x * 3 + 3):
            if grille[i][j] == num and (i, j) != position:
                return False
    return True
    


def resoudre_sudoku(grille):
    case_vide = trouver_case_vide(grille)
    if not case_vide:
        return True
    ligne, colonne = case_vide
    for num in range(1, 10):
        if est_valide(grille, num, (ligne, colonne)):
            grille[ligne][colonne] = num
            if resoudre_sudoku(grille):
                return True
            grille[ligne][colonne] = 0 
 


# Fonctions de test

def demo():
    print("Grille avant la résolution : \n" )
    afficher_grille(grille)
    print("\n")
    print("Grille après résolution : \n")
    resoudre_sudoku(grille)
    afficher_grille(grille)


def sudoku(x=True):
    print(" SUDOKU \n 1: Oui  0: Non ")
    while x == True:
        x=  int(input("Voulez-vous voir la démo ? "))
        if x == 1 :
            return demo(), sudoku(x=False)
    m = int(input("Voulez-vous créer votre grille ? "))
    if m == 1:
        creer_grille(grille_vide)
        n= int(input("voulez-vous resoudre votre grille ? "))
        if n==1 :
            return resoudre_sudoku(grille_vide)
    print("Fin")



# Grilles

grille_vide = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

grille = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
