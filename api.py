import requests

BASE_URL = 'https://python.gel.ulaval.ca/quoridor/api/'

def lister_parties(idul):
    
    rep = requests.get(f'{BASE_URL}parties/', params={'idul': idul})

    try:
        rep = requests.get(f'{BASE_URL}parties/', params={'idul': idul})
        if rep.status_code == 200:
        # la requête s'est déroulée normalement; décoder le JSON
            rep = rep.json()
            return rep
        elif rep.status_code == 406:
            raise RuntimeError
    except RuntimeError as err:
            return ("Votre requête est invalide; décoder le JSON")
    else:
        return f"Le GET sur '{BASE_URL}parties/' a produit le code d'erreur {rep.status_code}."



    



def initialiser_partie(idul):
    L = []
    rep = requests.post(f'{BASE_URL}partie/', data={'idul':idul})
    try:
        if rep.status_code == 200:
    # la requête s'est déroulée normalement; décoder le JSON
            rep1 = rep.json()
            return rep1
        elif rep.status_code == 406:
    # Votre requête est invalide; décoder le JSON
             raise RuntimeError
    except RuntimeError as err:
            return ("Votre requête est invalide; décoder le JSON")
    else:
        return f"Le POST sur '{BASE_URL}partie/' a produit le code d'erreur {rep.status_code}."
    

def jouer_coup(id, type, position):
    
    coup ={"id":id, "type":type, "position":position}
    
    rep = requests.put(f'{BASE_URL}partie/', data = coup)
    
    try:
        if rep.status_code == 200:
    # la requête s'est déroulée normalement; décoder le JSON
            rep1 = rep.json()
            return rep1
        elif rep.status_code == 406:
    # Votre requête est invalide; décoder le JSON
             raise RuntimeError
    except RuntimeError as err:
            return ("Votre requête est invalide; décoder le JSON")
    else:
        return f"Le PUT sur '{BASE_URL}partie/' a produit le code d'erreur {rep.status_code}."
        


    
