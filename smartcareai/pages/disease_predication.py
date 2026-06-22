import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Disease Prediction",
    page_icon="🤖",
    layout="wide"
)

st.logo("assets/logo.png")

if "user" not in st.session_state:
    st.warning("Please login first")
    st.stop()

# Load Dataset
df = pd.read_csv(
    "datasets/D_dataset.csv"
)

# Load Model
try:

    model = joblib.load(
        "models/disease_model.pkl"
    )

    encoder = joblib.load(
        "models/label_encoder.pkl"
    )

    features = joblib.load(
        "models/features.pkl"
    )

except:

    st.error(
        "Model files not found. Train model first."
    )

    st.stop()

symptoms = features

diseases = sorted(
    df["diseases"].unique()
)

st.title("🤖 AI Disease Prediction")

tab1, tab2 = st.tabs(
    [
        "🩺 Predict Disease",
        "🔍 Search Disease"
    ]
)

# -------------------------
# Prediction Tab
# -------------------------

with tab1:

    st.subheader(
        "Select Symptoms"
    )

    selected_symptoms = st.multiselect(
        "Choose Symptoms",
        symptoms
    )

    if st.button(
        "🔍 Predict Disease"
    ):

        if len(selected_symptoms) == 0:

            st.warning(
                "Please select symptoms."
            )

        else:

            input_data = {}

            for feature in features:

                input_data[feature] = (
                    1 if feature in selected_symptoms
                    else 0
                )

            input_df = pd.DataFrame(
                [input_data]
            )

            input_df = input_df[
                features
            ]

            prediction = model.predict(
                input_df
            )

            disease = encoder.inverse_transform(
                prediction
            )[0]

            confidence = max(
                model.predict_proba(
                    input_df
                )[0]
            ) * 100

            st.success(
                f"✅ Predicted Disease: {disease}"
            )

            st.info(
                f"🎯 Confidence Score: {confidence:.2f}%"
            )

            if confidence >= 80:

                st.success(
                    "🟢 High Confidence"
                )

            elif confidence >= 50:

                st.warning(
                    "🟠 Medium Confidence"
                )

            else:

                st.error(
                    "🔴 Low Confidence"
                )

            risk = "Low"

            if len(
                selected_symptoms
            ) >= 8:

                risk = "High"

            elif len(
                selected_symptoms
            ) >= 4:

                risk = "Medium"

            st.session_state[
                "latest_prediction"
            ] = {

                "symptoms":
                selected_symptoms,

                "disease":
                disease,

                "risk":
                risk,

                "confidence":
                round(
                    confidence,
                    2
                )
            }

# -------------------------
# Search Disease Tab
# -------------------------

with tab2:

    search_disease = st.selectbox(
        "Search Disease",
        diseases
    )

    disease_row = df[
        df["diseases"]
        == search_disease
    ]

    if not disease_row.empty:

        st.success(
            search_disease
        )

        st.write(
            "### Common Symptoms"
        )

        row = disease_row.iloc[0]

        for symptom in features:

            if row[symptom] == 1:

                st.write(
                    f"✅ {symptom}"
                )

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.page_link(
        "pages/dashboard.py",
        label="📊 Dashboard"
    )

with col2:

    st.page_link(
        "pages/symptom_checker.py",
        label="🩺 Symptom Checker"
    )

st.divider()

st.caption(
    "🏥 Smart Care AI"
)

st.caption(
    "AI-Powered Healthcare Management System"
)

st.caption(
    "Project By  Md Farhan Ansari & Sejal Verma"
)
