from Models.achat_model import GestionAchats, Achat, obtenir_top_produit
from Views.main_view import MainView

class MainController:
    def __init__(self):
        self.model = GestionAchats()
        self.view = MainView()

    def executer(self):
        while True:
            choix = self.view.afficher_menu()
            
            if choix == '1':
                nom, prix, categorie = self.view.demander_achat()
                if nom and prix is not None:
                    achat = Achat(nom, prix, categorie)
                    self.model.enregistrer_achat(achat)
                    self.view.afficher_message("Achat enregistré avec succès.")
            
            elif choix == '2':
                historique = self.model.consulter_historique()
                self.view.afficher_historique(historique)
            
            elif choix == '3':
                # Pour le top produit, on extrait juste les noms des achats
                historique = self.model.consulter_historique()
                noms_produits = [achat.nom for achat in historique]
                top_produit = obtenir_top_produit(noms_produits)
                self.view.afficher_top_produit(top_produit)
            
            elif choix == '4':
                self.view.afficher_message("Au revoir !")
                break
            
            else:
                self.view.afficher_message("Choix invalide.")
