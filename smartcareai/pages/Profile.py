import streamlit as st
import pymongo

# MongoDB Connection
conn = pymongo.MongoClient(
    "mongodb://127.0.0.1:27017/"
)

mydb = conn["smartcareai"]
users = mydb["users"]

st.set_page_config(
    page_title="My Profile",
    page_icon="👤",
    layout="wide"
)

st.logo("assets/logo.png")

# Login Check
if "user" not in st.session_state:
    st.warning("Please login first")
    st.stop()

user = st.session_state["user"]

st.title("👤 My Profile")
st.success(f"Welcome {user['name']}")
st.divider()


# =========================
# Profile Dialog
# =========================
@st.dialog("👤 Personal Information")
def show_profile():

    st.write(f"**Name:** {user['name']}")
    st.write(f"**Phone:** {user['phone']}")
    st.write(f"**Email:** {user['email']}")
    st.write(f"**Gender:** {user['gender']}")
    st.write(f"**Age:** {user['age']}")
    st.write(f"**Blood Group:** {user['blood_group']}")
    st.write(f"**Height:** {user['height']} cm")
    st.write(f"**Weight:** {user['weight']} kg")


# =========================
# Change Password Dialog
# =========================
@st.dialog("🔒 Change Password")
def change_password_dialog():

    old_password = st.text_input(
        "Current Password",
        type="password"
    )

    new_password = st.text_input(
        "New Password",
        type="password"
    )

    confirm_password = st.text_input(
        "Confirm New Password",
        type="password"
    )

    if st.button("Update Password"):

        db_user = users.find_one({
            "phone": user["phone"]
        })

        if not db_user:

            st.error("User not found")

        elif db_user["password"] != old_password:

            st.error("Current Password is Incorrect")

        elif new_password != confirm_password:

            st.error("Passwords do not match")

        elif len(new_password) < 6:

            st.error(
                "Password must be at least 6 characters"
            )

        else:

            users.update_one(
                {"phone": user["phone"]},
                {
                    "$set": {
                        "password": new_password
                    }
                }
            )

            st.session_state["user"]["password"] = new_password

            st.success(
                "✅ Password Updated Successfully"
            )


# Buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("👤 View Profile"):
        show_profile()

with col2:
    if st.button("🔒 Change Password"):
        change_password_dialog()

st.divider()


# Dashboard Summary
st.header("Dashboard Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("🩺 Symptom Checker")

with col2:
    st.info("🤖 Disease Prediction")

with col3:
    st.info("💬 AI Health Assistant")

st.divider()


# Latest Prediction
st.header("Latest Health Analysis")

if "latest_prediction" in st.session_state:

    prediction = st.session_state["latest_prediction"]

    st.write(
        f"**Symptoms:** {', '.join(prediction['symptoms'])}"
    )

    st.write(
        f"**Disease:** {prediction['disease']}"
    )

    st.write(
        f"**Risk Level:** {prediction['risk']}"
    )

else:
    st.info("No prediction available")

st.divider()


# Logout
if st.button("🚪 Logout"):

    st.session_state.clear()
    st.switch_page("main.py")

st.divider()

st.caption("🏥 Smart Care AI")
st.caption("Project By  Md Farhan Ansari & Sejal Verma")
