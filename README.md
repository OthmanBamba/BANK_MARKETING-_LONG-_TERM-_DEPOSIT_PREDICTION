# Dashboard de Prédiction des Décisions d'Offre de DAT avec Streamlit

## Description
Cette application Streamlit permet d'importer un fichier CSV, de sélectionner un modèle de machine learning et de faire des prédictions sur les décisions des offres de Dépôt à Terme (DAT). Elle propose aussi des visualisations interactives pour analyser les résultats et extraire des insights clés.

## Fonctionnalités
- **Importation de fichiers CSV** : L'utilisateur peut charger ses propres données.
- **Sélection d'un modèle de prédiction** : Plusieurs modèles sont disponibles :
  - Régression logistique
  - Arbre de décision
  - Forêt aléatoire
  - XGBoost
- **Prédictions sur les décisions d'offre de DAT** : Le modèle prédit si un client va accepter ou refuser l'offre.
- **Visualisations interactives** :
  - Distribution des prédictions
  - Importance des variables pour la décision
  - KPI clés (taux d'acceptation, nombre total de clients ciblés, etc.)
  - Répartition des décisions des clients
  - Nombre de clients ciblés par mois
  - Évolution du taux d'acceptation au fil des appels

## Installation
1. **Cloner le répertoire** :
   ```sh
   git clone https://github.com/ton-repo.git
   cd ton-repo
   ```

2. **Installer les dépendances** :
   ```sh
   pip install -r requirements.txt
   ```

3. **Lancer l'application Streamlit** :
   ```sh
   streamlit run app.py
   ```

## Utilisation
1. Importer un fichier CSV contenant les données clients.
2. Sélectionner un modèle de machine learning dans la barre latérale.
3. Cliquer sur le bouton "Prédire" pour obtenir les résultats.
4. Explorer les prédictions et les visualisations fournies par l'application.

## Structure du Projet
```
/
|-- models/                      # Dossier contenant les modèles ML
|   |-- logistic_regression_model.pkl
|   |-- arbre_de_décisions_model.pkl
|   |-- random_forest_model.pkl
|   |-- xgradient_boosting_model.pkl
|
|-- app.py                        # Code principal de l'application
|-- requirements.txt               # Liste des dépendances Python
|-- README.md                      # Documentation du projet
```

## Prérequis
- Python 3.7+
- Streamlit
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- XGBoost

## Améliorations Futures
- Ajout d'une interface plus avancée avec des widgets interactifs
- Intégration de nouveaux modèles plus performants
- Ajout d'une option de téléchargement des résultats sous format CSV
- Optimisation de la gestion des erreurs et des messages utilisateur

## Auteur
**BAMBA BEN OTHMANE**  
MSc AI for Business @ Aivancity Paris  
Expert en Machine Learning, Data Analytics et IA Générative

---
N'hésite pas à me contacter pour toute question ou suggestion ! 🚀

