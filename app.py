from flask import Flask, render_template, request, redirect, url_for, flash
from Models.achat_model import GestionAchats, Achat, obtenir_top_produit
import os

app = Flask(__name__)
app.secret_key = 'cle_secrete_pour_flash'  # Nécessaire pour les messages flash

# Instance globale pour simuler la base de données en mémoire
gestion_achats = GestionAchats()

@app.route('/')
def index():
    historique = gestion_achats.consulter_historique()
    return render_template('index.html', historique=historique)

@app.route('/ajouter', methods=['GET', 'POST'])
def ajouter():
    if request.method == 'POST':
        nom = request.form['nom']
        try:
            prix = float(request.form['prix'])
        except ValueError:
            flash("Erreur : Le prix doit être un nombre valide.")
            return redirect(url_for('ajouter'))
            
        categorie = request.form['categorie']
        
        nouvel_achat = Achat(nom, prix, categorie)
        gestion_achats.enregistrer_achat(nouvel_achat)
        
        flash(f"Achat '{nom}' enregistré avec succès !")
        return redirect(url_for('index'))
    
    return render_template('ajouter.html')

@app.route('/statistiques')
def statistiques():
    historique = gestion_achats.consulter_historique()
    noms_produits = [achat.nom for achat in historique]
    top = obtenir_top_produit(noms_produits)
    return render_template('statistiques.html', top_produit=top)

if __name__ == '__main__':
    app.run(debug=True)
