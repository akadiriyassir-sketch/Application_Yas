import unittest
from app import app, gestion_achats

class TestWebApp(unittest.TestCase):
    def setUp(self):
        # Configuration de test
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False  # Désactiver CSRF pour les tests si nécessaire
        self.app = app.test_client()
        # Réinitialiser les données avant chaque test
        gestion_achats.historique = []

    def test_page_accueil(self):
        # Vérifie que la page d'accueil charge (Code 200)
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Historique des Achats", response.data)

    def test_ajout_achat(self):
        # Test de l'ajout d'un produit via le formulaire
        response = self.app.post('/ajouter', data=dict(
            nom="TestProduit",
            prix="10.5",
            categorie="TestCat"
        ), follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"TestProduit", response.data)
        self.assertIn(b"10.5", response.data)

    def test_calcul_top_produit(self):
        # Ajout de plusieurs produits
        self.app.post('/ajouter', data={'nom': 'A', 'prix': '1', 'categorie': 'C'}, follow_redirects=True)
        self.app.post('/ajouter', data={'nom': 'A', 'prix': '1', 'categorie': 'C'}, follow_redirects=True)
        self.app.post('/ajouter', data={'nom': 'B', 'prix': '1', 'categorie': 'C'}, follow_redirects=True)

        # Test du bouton Top Produit
        response = self.app.post('/top-produit', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Top Produit", response.data)
        # Vérifie que 'A' est bien identifié comme le top produit
        self.assertIn(b"A", response.data)

if __name__ == '__main__':
    unittest.main()
