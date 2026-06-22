import streamlit as st
import streamlit.components.v1 as com
import pymongo

# MongoDB Connection
conn = pymongo.MongoClient(
    "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.3"
)

mydb = conn["smartcareai"]
users = mydb["users"]

# Page Config
st.set_page_config(
    page_title="Register - Smart Care AI",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Smart Care AI")
st.subheader("Create Your Account")

# Layout
col1, col2 = st.columns([1, 2])

with col1:
    com.iframe(
        "https://lottie.host/embed/7467ad87-9159-4b91-9408-315468cde80d/sEHVpSU2at.lottie",
        height=450
    )

with col2:
    

    with st.form("register_form"):

        st.subheader("👤 User Registration")

        name = st.text_input(
            "👤 Full Name"
        )

        phone = st.text_input(
            "📱 Phone Number"
        )

        age = st.slider(
            "🎂 Age",
            min_value=1,
            max_value=100,
            value=18
        )

        gender = st.selectbox(
            "🚻 Gender",
            [
                "Male",
                "Female",
                "Other"
            ]
        )

        blood_group = st.selectbox(
            "🩸 Blood Group",
            [
                "A+",
                "A-",
                "B+",
                "B-",
                "AB+",
                "AB-",
                "O+",
                "O-"
            ]
        )

        height = st.number_input(
            "📏 Height (cm)",
            min_value=50,
            max_value=250,
            value=170
        )

        weight = st.number_input(
            "⚖ Weight (kg)",
            min_value=10,
            max_value=300,
            value=60
        )

        email = st.text_input(
            "📧 Email Address"
        )

        password = st.text_input(
            "🔒 Password",
            type="password"
        )

        confirm_password = st.text_input(
            "🔒 Confirm Password",
            type="password"
        )

        terms = st.checkbox(
            "I Agree To Terms & Conditions"
        )

        register_btn = st.form_submit_button(
            "📝 Register"
        )
        st.page_link("pages/login.py",label="🔐 Already Have An Account? Login"
                     )
        
 

# Registration Logic
if register_btn:

    if not name or not phone or not email or not password:
        st.error(
            "Please Fill All Fields"
        )

    elif password != confirm_password:
        st.error(
            "Passwords Do Not Match"
        )

    elif not terms:
        st.warning(
            "Please Accept Terms & Conditions"
        )

    else:

        existing_user = users.find_one(
            {"phone": phone}
        )

        if existing_user:

            st.warning(
                "Phone Number Already Registered"
            )

        else:

            users.insert_one({

                "name": name,
                "phone": phone,
                "age": age,
                "gender": gender,
                "blood_group": blood_group,
                "height": height,
                "weight": weight,
                "email": email,
                "password": password

            })

            st.success(
                "✅ Registration Successful"
            )
        

            st.balloons()
            st.divider()

 

st.divider()

st.caption("🏥 Smart Care AI")
st.caption("Project By  Md Farhan Ansari & Sejal Verma")
