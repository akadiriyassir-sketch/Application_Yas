class MainView:
    def afficher_menu(self):
        print("\n--- Menu Gestion Achats ---")
        print("1. Enregistrer un achat")
        print("2. Consulter l'historique")
        print("3. Obtenir le produit le plus fréquent")
        print("4. Quitter")
        return input("Choix : ")

    def demander_achat(self):
        nom = input("Nom du produit : ")
        try:
            prix = float(input("Prix : "))
        except ValueError:
            print("Prix invalide.")
            return None, None, None
        categorie = input("Catégorie : ")
        return nom, prix, categorie

    def afficher_historique(self, historique):
        print("\n--- Historique des achats ---")
        if not historique:
            print("Aucun achat enregistré.")
        else:
            for achat in historique:
                print(achat)

    def afficher_top_produit(self, produit):
        if produit:
            print(f"\nLe produit le plus fréquent est : {produit}")
        else:
            print("\nAucune donnée pour déterminer le top produit.")

    def afficher_message(self, message):
        print(message)
