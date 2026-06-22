import streamlit as st

st.set_page_config(
    page_title="Symptom Checker",
    page_icon="🩺",
    layout="wide"
)

st.logo("assets/logo.png")

# Login Check
if "user" not in st.session_state:
    st.warning("Please login first")
    st.stop()

st.title("🩺 AI Symptom Checker")

st.write(
    "Select your symptoms and get an instant health assessment."
)

st.divider()

symptoms = [
    "Fever",
    "Cough",
    "Headache",
    "Fatigue",
    "Sore Throat",
    "Runny Nose",
    "Body Pain",
    "Dizziness",
    "Nausea",
    "Vomiting",
    "Diarrhea",
    "Chest Pain",
    "Shortness of Breath",
    "Loss of Taste",
    "Loss of Smell"
]

selected_symptoms = st.multiselect(
    "Select Symptoms",
    symptoms
)

days = st.slider(
    "How many days have you had these symptoms?",
    1,
    30,
    3
)

st.divider()

if st.button("🔍 Analyze Symptoms"):

    if len(selected_symptoms) == 0:

        st.error(
            "Please select at least one symptom."
        )

    else:

        symptom_count = len(
            selected_symptoms
        )

        # Risk Calculation
        if symptom_count >= 8:

            risk = "High"

        elif symptom_count >= 4:

            risk = "Medium"

        else:

            risk = "Low"

        # Disease Guess
        disease = "General Health Issue"

        if (
            "Fever" in selected_symptoms
            and "Cough" in selected_symptoms
        ):
            disease = "Flu"

        if (
            "Fever" in selected_symptoms
            and "Body Pain" in selected_symptoms
            and "Headache" in selected_symptoms
        ):
            disease = "Viral Fever"

        if (
            "Loss of Taste" in selected_symptoms
            and "Loss of Smell" in selected_symptoms
        ):
            disease = "COVID-19"

        if (
            "Chest Pain" in selected_symptoms
            and "Shortness of Breath" in selected_symptoms
        ):
            disease = "Heart / Lung Related Issue"

        if (
            "Vomiting" in selected_symptoms
            and "Diarrhea" in selected_symptoms
        ):
            disease = "Food Poisoning"

        st.success("Analysis Completed")

        st.subheader("📋 Health Assessment")

        st.write(
            f"**Symptoms Selected:** {len(selected_symptoms)}"
        )

        st.write(
            f"**Possible Condition:** {disease}"
        )

        st.write(
            f"**Risk Level:** {risk}"
        )

        # Dashboard Session
        st.session_state["latest_prediction"] = {
            "symptoms": selected_symptoms,
            "disease": disease,
            "risk": risk
        }

        st.divider()

        st.subheader("💡 Health Advice")

        if risk == "High":

            st.error(
                "Consult a healthcare professional immediately."
            )

        elif risk == "Medium":

            st.warning(
                "Monitor symptoms closely and seek medical advice."
            )

        else:

            st.success(
                "Stay hydrated, rest properly and monitor symptoms."
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
        "pages/disease_predication.py",
        label="🤖 Disease Predication"
    )

st.divider()

st.caption("🏥 Smart Care AI")
st.caption("AI-Powered Healthcare Management System")
st.caption("Project By  Md Farhan Ansari & Sejal Verma")
