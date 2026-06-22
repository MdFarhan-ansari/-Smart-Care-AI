import streamlit as st
from streamlit_autorefresh import st_autorefresh

st.set_page_config(
    page_title="Smart Care AI",
    page_icon="🏥",
    layout="wide"
)
st.markdown("""
<style>

/* Background Animation */
.stApp{
    background: linear-gradient(-45deg,#0B1120,#111827,#1E293B,#0F172A);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
}

@keyframes gradientBG{
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}

/* Title Glow */
h1{
    text-align:center;
   
}

@keyframes glow{
    from{
        text-shadow:0 0 10px #06B6D4;
    }
    to{
        text-shadow:
        0 0 20px #06B6D4,
        0 0 40px #06B6D4;
    }
}

/* Smooth Page Load */
.main{
    animation: slideUp 0.8s ease;
}

@keyframes slideUp{
    from{
        opacity:0;
        transform:translateY(30px);
    }
    to{
        opacity:1;
        transform:translateY(0);
    }
}

/* Info Cards Animation */
div[data-testid="stInfo"]{
    border-radius:20px;
    transition:all 0.3s ease;
}

div[data-testid="stInfo"]:hover{
    transform:translateY(-8px) scale(1.03);
}

/* Buttons Animation */
.stButton > button{
    border-radius:15px;
    font-weight:bold;
    transition:0.3s;
    animation:pulse 2s infinite;
}

.stButton > button:hover{
    transform:scale(1.05);
}

@keyframes pulse{
    0%{
        box-shadow:0 0 0 0 rgba(6,182,212,0.6);
    }
    70%{
        box-shadow:0 0 0 15px rgba(6,182,212,0);
    }
    100%{
        box-shadow:0 0 0 0 rgba(6,182,212,0);
    }
}

/* Banner Hover Effect */
img{
    border-radius:20px;
    transition:0.5s;
}

img:hover{
    transform:scale(1.02);
}

/* Sidebar Slide Animation */
section[data-testid="stSidebar"]{
    animation:sidebarSlide 0.8s ease;
}

@keyframes sidebarSlide{
    from{
        transform:translateX(-100%);
    }
    to{
        transform:translateX(0);
    }
}

</style>
""", unsafe_allow_html=True)
st.title("🏥 Smart Care AI")
col1, col2, col3, col4, col5 = st.columns([6,1,1,1,1])
with col2:
    st.page_link(
        "pages/bmi.py",
        label="⚖️ BMI Calculator"
    )
with col3:
    st.page_link(
        "pages/login.py",
        label="🔐 Login"
    )

with col4:
    st.page_link(
        "pages/register.py",
        label="📝 Register"
    )
with col5:
    st.page_link(
        "pages/profile.py",
        label="📝 Profile"
    )

# Sidebar Logo
st.logo("assets/logo.png")

# Center Logo
col1, col2, col3 = st.columns([1,2,1])
 

 

# Auto Banner Slider
count = st_autorefresh(interval=2000, key="banner")

banners = [
    "assets/banner1.png",
    "assets/banner2.png",
    "assets/banner3.png"
]

st.image(
    banners[count % len(banners)],
    use_container_width=True
)

 
st.subheader("AI-Powered Healthcare Management System")

st.write("""
Smart Care AI helps users monitor their health using Artificial Intelligence.

### Features

✅ User Registration & Login

✅ Personal Health Dashboard

✅ AI Symptom Checker

✅ Disease Prediction

✅ BMI Calculator

✅ Health Risk Analysis

✅ Medical Report Management

✅ AI Health Assistant Chatbot
""")

st.divider()

# Feature Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.info("🩺 Symptom Checker")

with col2:
    st.info("🤖 Disease Prediction")

with col3:
    st.info("💬 AI Health Assistant")

st.divider()

st.header("Quick Access")

col1, col2, col3 , col4= st.columns(4)

with col1:
    st.page_link(
        "pages/login.py",
        label="🔐 Login"
    )

with col2:
    st.page_link(
        "pages/register.py",
        label="📝 Register"
    )

with col3:
    st.page_link(
        "pages/dashboard.py",
        label="📊 Dashboard"
    )
with col4:
    st.page_link(
    "pages/bmi.py",
    label="⚖️ BMI Calculator"
)
st.divider()

st.success("Welcome to Smart Care AI")
st.title("🏥Project Description")
st.image("assets/de.png",width=1370)


 
 
# Footer
st.divider()

st.markdown(
    """
    ---
    <div style='text-align: center;'>
        <h4>🏥 Smart Care AI</h4>
        <p>AI-Powered Healthcare Management System</p>
        <p>© 2026 All Rights Reserved</p>
        <p><b>Project By Md Farhan Ansari & Sejal Verma</b></p>
    </div>
    """,
    unsafe_allow_html=True
)
