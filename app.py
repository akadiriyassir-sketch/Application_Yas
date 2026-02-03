from flask import Flask, render_template, request, redirect, url_for, flash
from Models.achat_model import GestionAchats, Achat, obtenir_top_produit

app = Flask(__name__)
app.secret_key = 'cle_secrete_pour_flash'

# Instance globale (Simule la DB)
gestion_achats = GestionAchats()

@app.route('/')
def index():
    historique = gestion_achats.consulter_historique()
    # On récupère le top_produit s'il a été passé en paramètre GET (via redirect)
    top_produit = request.args.get('top_produit')
    return render_template('index.html', historique=historique, top_produit=top_produit)

@app.route('/ajouter', methods=['POST'])
def ajouter():
    nom = request.form.get('nom')
    try:
        prix = float(request.form.get('prix'))
    except (ValueError, TypeError):
        flash("Erreur : Le prix doit être un nombre valide.")
        return redirect(url_for('index'))
        
    categorie = request.form.get('categorie')
    
    if nom and prix is not None and categorie:
        nouvel_achat = Achat(nom, prix, categorie)
        gestion_achats.enregistrer_achat(nouvel_achat)
        flash(f"Achat '{nom}' ajouté avec succès !", "success")
    else:
        flash("Erreur : Tous les champs sont obligatoires.", "danger")
        
    return redirect(url_for('index'))

@app.route('/top-produit', methods=['POST'])
def top_produit():
    historique = gestion_achats.consulter_historique()
    noms_produits = [achat.nom for achat in historique]
    top = obtenir_top_produit(noms_produits)
    
    if top:
        flash(f"Le produit le plus fréquent est : {top}", "info")
        return redirect(url_for('index', top_produit=top))
    else:
        flash("Pas assez de données pour déterminer le top produit.", "warning")
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
