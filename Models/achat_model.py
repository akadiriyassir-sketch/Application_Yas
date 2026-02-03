from collections import Counter

class Achat:
    def __init__(self, nom, prix, categorie):
        self.nom = nom
        self.prix = prix
        self.categorie = categorie

    def __repr__(self):
        return f"Achat(nom='{self.nom}', prix={self.prix}, categorie='{self.categorie}')"

class GestionAchats:
    def __init__(self):
        self.historique = []

    def enregistrer_achat(self, achat):
        self.historique.append(achat)

    def consulter_historique(self):
        return self.historique

def obtenir_top_produit(liste):
    """
    Analyse une liste et retourne l'élément le plus fréquent.
    Si la liste est vide, retourne None.
    """
    if not liste:
        return None
    compteur = Counter(liste)
    # most_common(1) retourne une liste de tuples [(element, count)]
    return compteur.most_common(1)[0][0]
