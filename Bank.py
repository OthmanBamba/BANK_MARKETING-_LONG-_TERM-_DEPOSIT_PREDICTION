import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import numpy as np

#  Dossier des modèles
models_directory = "/Users/benothmane/Documents/Streamlite/models"

#  modèles
models = {
    "logistic_regression": os.path.join(models_directory, "logistic_regression_model.pkl"),
    "arbre_de_décisions_model": os.path.join(models_directory, "arbre_de_décisions_model.pkl"),
    "random_forest": os.path.join(models_directory, "random_forest_model.pkl"),
    "xgradient_boosting": os.path.join(models_directory, "xgradient_boosting_model.pkl")
}

# charger un modèle
def load_model(model_path):
    try:
        return joblib.load(model_path)
    except Exception as e:
        st.sidebar.error(f"Erreur lors du chargement du modèle: {e}")
        return None

# Interface utilisateur
st.sidebar.title("Configuration")
uploaded_file = st.sidebar.file_uploader("Importer un fichier CSV", type=["csv"])

# Charger le dataset
df = None
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.sidebar.success("Dataset chargé avec succès !")

    # données avant toute prédiction
    st.write("### Données d'entrée")
    st.dataframe(df)

# Sélection du modèle
selected_model = st.sidebar.selectbox("Sélectionner un modèle", list(models.keys()))
model = load_model(models[selected_model])

# Vérification du modèle et des features
if model and hasattr(model, "predict") and df is not None:

    #  features attendues par le modèle
    if hasattr(model, "feature_names_in_"):
        expected_features = list(model.feature_names_in_)
    else:
        st.sidebar.error("Impossible de récupérer les features attendues par le modèle.")
        expected_features = None

    if expected_features:
        # colonnes attendues sont présentes
        missing_columns = [col for col in expected_features if col not in df.columns]
        if missing_columns:
            st.sidebar.error(f"Colonnes manquantes : {', '.join(missing_columns)}")
        else:
            # Bouton pour lancer la prédiction
            if st.sidebar.button("Prédire"):
                # Extraire les données d'entrée
                input_data = df[expected_features]

                # Faire la prédiction
                df["Prédiction"] = model.predict(input_data)

                # Affichage des résultats
                st.write("### Résultats des prédictions sur les decisions d'offre de DAT (O pour refus/ 1 pour acceptation)")
                st.dataframe(df[expected_features + ["Prédiction"]])

                # Visualisation des prédictions
                st.write("### Distribution des prédictions  sur les decisions d'offre de DAT (O pour refus/ 1 pour acceptation)")
                fig, ax = plt.subplots()
                sns.countplot(x=df["Prédiction"], ax=ax)
                st.pyplot(fig)


                #  Visualisation des variables impactantes
                st.write("### Impact  des variables sur les decisions d'offre de DAT")
                fig, ax = plt.subplots()

                if hasattr(model, "feature_importances_"):
                    importances = model.feature_importances_
                elif hasattr(model, "coef_"):
                    importances = np.abs(model.coef_).flatten()
                else:
                    st.warning("L'importance des variables n'est pas disponible pour ce modèle.")
                    importances = None

                if importances is not None:
                   feature_importance_df = pd.DataFrame(
                       {"Variable": expected_features, "Importance": importances}
                   ).sort_values(by="Importance", ascending=False)

                   # Graphique avec les variables sur l'axe Y et l'importance sur l'axe X
                   fig, ax = plt.subplots(figsize=(14, 12))
                   sns.barplot(y="Importance", x="Variable", data=feature_importance_df.head(10), ax=ax)

                   ax.set_xlabel("Importance")
                   ax.set_ylabel("Variable")
                   ax.set_title("variables les plus importantes")

                   st.pyplot(fig)
               # **Ajout des KPI après les prédictions et les variables impactantes**
                st.write("###  Indicateurs Clés de Performance (KPI)")

                # Calcul des KPI
                total_clients = len(df)
                acceptations = df["Prédiction"].sum()
                refus = total_clients - acceptations
                taux_acceptation = (acceptations / total_clients) * 100
                taux_refus = (refus / total_clients) * 100

                #  KPI
                st.metric(label="Nombre total de clients ciblés ", value=total_clients)
                st.metric(label="Taux d'acceptation (%)", value=f"{taux_acceptation:.2f}%")
                st.metric(label="Taux de refus (%)", value=f"{taux_refus:.2f}%")

                # taux d'acceptation et de refus
                fig, ax = plt.subplots()
                ax.pie([acceptations, refus], labels=["Acceptations", "Refus"], autopct="%1.1f%%", colors=["green", "red"])
                ax.set_title("Répartition des décisions des clients")
                st.pyplot(fig)
                # **KPI Nombre total de clients ciblés par mois**
                st.write("###  Nombre total de clients ciblés par mois")
                # Calcul du nombre total de clients par mois
                clients_par_mois = df["month"].value_counts().sort_index()
                # Graphique du nombre de clients par mois
                fig, ax = plt.subplots(figsize=(10, 6))
                clients_par_mois.plot(kind="bar", color="skyblue", ax=ax)
                ax.set_xlabel("Mois")
                ax.set_ylabel("Nombre de clients")
                ax.set_title(" Clients ciblés par mois")

                st.pyplot(fig)
else:
    st.sidebar.error("Veuillez importer un dataset et choisir un modèle valide.")
