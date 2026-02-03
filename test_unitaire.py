import unittest
from Models.achat_model import obtenir_top_produit

class TestGestionAchats(unittest.TestCase):
    def test_obtenir_top_produit(self):
        liste = ["pomme", "poire", "pomme"]
        resultat = obtenir_top_produit(liste)
        self.assertEqual(resultat, "pomme")

    def test_obtenir_top_produit_vide(self):
        liste = []
        resultat = obtenir_top_produit(liste)
        self.assertIsNone(resultat)

    def test_obtenir_top_produit_egalite(self):
        # Cas où il y a égalité, Counter retourne l'un des premiers rencontrés ou arbitraire selon l'implémentation
        # Ici on vérifie juste que ça ne plante pas et retourne un des éléments max
        liste = ["pomme", "poire"]
        resultat = obtenir_top_produit(liste)
        self.assertIn(resultat, ["pomme", "poire"])

if __name__ == '__main__':
    unittest.main()
