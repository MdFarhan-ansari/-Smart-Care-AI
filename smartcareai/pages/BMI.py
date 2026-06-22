import streamlit as st

st.set_page_config(
    page_title="BMI Calculator",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ BMI Calculator")
st.subheader("Check Your Body Mass Index")

st.divider()

col1, col2 = st.columns(2)

with col1:
    height = st.slider(
        "📏 Height (cm)",
        min_value=100,
        max_value=250,
        value=170
    )

with col2:
    weight = st.slider(
        "⚖️ Weight (kg)",
        min_value=20,
        max_value=200,
        value=70
    )

st.divider()

if st.button("🧮 Calculate BMI"):

    height_m = height / 100

    bmi = round(
        weight / (height_m ** 2),
        2
    )

    st.metric(
        "Your BMI",
        bmi
    )

    if bmi < 18.5:
        st.warning("🟡 Underweight")

    elif bmi < 25:
        st.success("🟢 Normal Weight")

    elif bmi < 30:
        st.warning("🟠 Overweight")

    else:
        st.error("🔴 Obese")

    st.divider()

    st.subheader("BMI Categories")

    st.write("""
    🔹 Below 18.5 → Underweight

    🔹 18.5 - 24.9 → Normal Weight

    🔹 25 - 29.9 → Overweight

    🔹 30 and Above → Obese
    """)

st.divider()

st.caption("🏥 Smart Care AI")
st.caption("Project By  Md Farhan Ansari & Sejal Verma")
