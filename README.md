#Projet de Prise de Décision sur les Données de Stratégie Marketing d'une Banque
Description

Ce projet analyse les données marketing de la banque PortuGBank afin d'optimiser les campagnes de souscription aux dépôts à terme (DAT). L'objectif est d'augmenter le taux d'acceptation des offres tout en minimisant le coût des actions commerciales.

Les données couvrent une période de 4 ans et contiennent 41 188 clients et 21 variables, comprenant des informations socio-démographiques, historiques financières, données de contact, historiques de campagne et variables macroéconomiques.

Objectifs

Identifier les facteurs influençant la souscription au DAT.

Optimiser le ciblage des clients pour réduire les coûts des campagnes marketing.

Utiliser des techniques de data science pour extraire des insights exploitables.

Segmentation des Données

Données socio-démographiques :

Âge, type de job, situation matrimoniale, niveau d'éducation.

Analyse de leur impact sur la souscription au DAT.

Historique financière :

Défaut de paiement, prêt immobilier et personnel.

Influence sur la capacité d'épargne des clients.

Données de contact :

Moyen de contact, mois et jour de la semaine, durée des communications.

Importance de ces facteurs dans la conversion des clients.

Historique de campagne :

Nombre d'appels, délai depuis le dernier appel, résultats de campagnes précédentes.

Impact sur la réussite des actions marketing.

Données macroéconomiques :

Taux de variation de l'emploi, nombre d'employés, inflation, confiance des consommateurs, taux d'intérêts.

Influence sur la décision d'épargne des clients.

Types de Variables

Variables numériques : Age, duration, campaign, pdays, previous, emp.var.rate, cons.price.idx, cons.conf.idx, euribor3m, nr.employed.

Variables catégorielles : job, marital, education, default, housing, loan, contact, month, day_of_week, poutcome, y (variable cible).

Conclusion

Cette analyse vise à fournir des recommandations basées sur les données afin d'améliorer les performances des campagnes marketing de PortuGBank. Les résultats permettront d'affiner le ciblage des clients pour une approche plus efficace et rentable.
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

