import streamlit as st

st.set_page_config(
    page_title="Dashboard - Smart Care AI",
    page_icon="🏥",
    layout="wide"
)

st.logo("assets/logo.png")

# Login Check
if "user" not in st.session_state:
    st.warning("Please login first.")
    st.stop()

user = st.session_state["user"]

st.title("📊 Smart Care AI Dashboard")

st.success(f"Welcome {user['name']} 👋")
@st.dialog("👤 Personal Information")
def show_profile():

    st.write(f"**Name:** {user['name']}")
    st.write(f"**Phone:** {user['phone']}")
    st.write(f"**Email:** {user['email']}")
    st.write(f"**Gender:** {user['gender']}")
    st.write(f"**Age:** {user['age']}")
    st.write(f"**Blood Group:** {user['blood_group']}")
    st.write(f"**Weight:** {user['weight']}")

if st.button("👤 View Profile"):
    show_profile()

st.divider()

 
# BMI Calculator
st.header("⚖️ Live BMI Calculator")

col1, col2 = st.columns(2)

with col1:
    height = st.slider(
        "📏 Height (cm)",
        100,
        250,
        int(user["height"])
    )

with col2:
    weight = st.slider(
        "⚖️ Weight (kg)",
        20,
        200,
        int(user["weight"])
    )

height_m = height / 100

bmi = round(
    weight / (height_m ** 2),
    2
)

st.metric(
    "BMI Score",
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

# Latest Health Analysis
st.header("🩺 Latest Health Analysis")

if "latest_prediction" in st.session_state:

    prediction = st.session_state["latest_prediction"]

    st.write(
        f"**Symptoms:** {', '.join(prediction['symptoms'])}"
    )

    st.write(
        f"**Predicted Disease:** {prediction['disease']}"
    )

    st.write(
        f"**Risk Level:** {prediction['risk']}"
    )

else:
    st.info(
        "No health analysis available. Please use Symptom Checker."
    )

st.divider()

# AI Features
st.header("🤖 AI Services")

col1, col2 = st.columns(2)

with col1:
    st.page_link(
        "pages/symptom_checker.py",
        label="🩺 Symptom Checker"
    )

with col2:
    st.page_link(
        "pages/disease_predication.py",
        label="🤖 Disease Prediction"
    )


st.divider()

# Health Tips
st.header("💡 Health Tips")

st.info(
    """
    • Drink at least 2-3 litres of water daily.
    
    • Exercise for 30 minutes every day.
    
    • Get 7-8 hours of sleep.
    
    • Eat a balanced diet rich in fruits and vegetables.
    """
)

st.divider()

# Logout
if st.button("🚪 Logout"):
    st.session_state.clear()
    st.switch_page("main.py")

st.divider()

# Footer
st.caption("🏥 Smart Care AI")
st.caption("AI-Powered Healthcare Management System")
st.caption("Powered by Artificial Intelligence")
st.caption("© 2026 All Rights Reserved")
st.caption("Project By  Md Farhan Ansari & Sejal Verma")
