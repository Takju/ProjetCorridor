import argparse
import json
def analyser_commande():

    # Créer un analyseur de ligne de commande
    parser = argparse.ArgumentParser()
    # Insérer ici les bons appels à la méthode add_argument
    parser.add_argument("idul", help ="idul du joueur")   
    parser.add_argument("--parties", help = "Lister les identifiants de vos 20 dernières parties")                    
    args = parser.parse_args()
    return args
    

	
def afficher_damier_ascii():
	print("Légende")
	print("1 = IDUL", "murs =" )
	print("2 = automate", "murs =")



def afficher_damier_asc(dc):

    m1 = dc["joueurs"][0]["murs"]
    m2 = dc["joueurs"][1]["murs"]
    h = "--------"
    v = "|"
    
    print("Légende")
    print()
    
    print("1 = IDUL", "murs =", "|"*m1 )
    print("2 = automate", "murs =", "|"*m2)

    
    #print(L)
    posj1 = dc["joueurs"][0]["pos"][0]
    posj2= dc["joueurs"][0]["pos"][1]

    posa1 = dc["joueurs"][1]["pos"][0]
    posa2 = dc["joueurs"][1]["pos"][1]
    H = dc["murs"]["horizontaux"]
    V = dc["murs"]["verticaux"]
    
    print(H)
    print(v)
                

    for i in range(9):
        print(i+1,"|", end =  "   ")
        for j in range(9):
            if i == posj1 and j == posj2:
                print("1", end = "  ")
            elif i == posa1 and j == posa2:
                print("2", end = "  ")
            else:
                print(".", end = "  ")
            #print("|")
        print("|")
        for k in range(9):
            
                if [i, k]== [4, 5]:
                    print('  |  ','-----','                     |')
                elif i == 2 and k == 5:
                        print("  |          |                   |")
    
        
        
    print("-"*35)
        
dc = {
    "joueurs": [
        {"nom": "IDUL", "murs": 7, "pos": [5, 5]}, 
        {"nom": "automate", "murs": 3, "pos": [8, 6]}
    ], 
    "murs": {
        "horizontaux": [[4, 4], [2, 6], [3, 8], [5, 8], [7, 8]], 
        "verticaux": [[6, 2], [4, 4], [2, 6], [7, 5], [7, 7]]
    }
}



afficher_damier_asc(dc)

