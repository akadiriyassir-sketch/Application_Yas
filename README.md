# Projet App Yas - Gestion d'Achats

Une application web simple basée sur l'architecture MVC (Modèle-Vue-Contrôleur) utilisant Python et Flask. Elle permet de gérer un historique d'achats et d'obtenir des statistiques simples.

## Fonctionnalités

*   **Enregistrement d'achats** : Formulaire pour ajouter un produit (Nom, Prix, Catégorie).
*   **Historique** : Visualisation de la liste des achats enregistrés.
*   **Statistiques** : Analyse automatique pour déterminer le produit le plus fréquemment acheté ("Top Produit").

## Architecture Technique

Le projet suit une architecture MVC stricte :
*   **Models/** : Logique métier (gestion des données et calculs statistiques).
*   **Views/** (Templates) : Interface utilisateur HTML/Bootstrap.
*   **Controllers/** (app.py) : Gestion des requêtes Web et orchestration.

## Prérequis

*   Python 3.x
*   Pip (gestionnaire de paquets Python)

## Installation

1.  Cloner le dépôt ou télécharger les fichiers.
2.  Installer les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

## Démarrage

Pour lancer l'application web :

```bash
python app.py
```

L'application sera accessible à l'adresse : `http://127.0.0.1:5000`

## Tests

Des tests unitaires sont disponibles pour valider la logique métier :

```bash
python test_unitaire.py
```
