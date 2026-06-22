import streamlit as st
import streamlit.components.v1 as com
import pymongo

# MongoDB Connection
conn = pymongo.MongoClient(
    "mongodb://127.0.0.1:27017/"
)

mydb = conn["smartcareai"]
users = mydb["users"]

 


st.title("🔐 Login")

with st.form("login_form"):
    com.iframe(
        "https://lottie.host/embed/55bc33c7-9ba7-4d9b-9716-219960a85fbd/dYVC0xsrbu.lottie",
        height=200
    )

    phone = st.text_input(
        "📱 Phone Number"
    )

    password = st.text_input(
        "🔒 Password",
        type="password"
    )

    login_btn = st.form_submit_button(
        "Login"
    )

if login_btn:

    user = users.find_one({
        "phone": phone,
        "password": password
    })

    if user:

        # Session
        st.session_state["user"] = {
            "name": user["name"],
            "phone": user["phone"],
            "email": user["email"],
            "age": user["age"],
            "gender": user["gender"],
            "blood_group": user["blood_group"],
            "height": user["height"],
            "weight": user["weight"],
            "password": user["password"]
        }

        st.success(
            f"Welcome {user['name']}"
        )

        st.switch_page(
            "pages/dashboard.py"
        )

    else:

        st.error(
            "Invalid Phone Number or Password"
        )
