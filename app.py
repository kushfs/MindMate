import streamlit as st
import joblib
import numpy as np
from streamlit_lottie import st_lottie
from streamlit_player import st_player
import requests

# Load ML model
model = joblib.load("model/mental_health_model.pkl")
st.set_page_config(page_title="MindMate – Home", layout="centered", page_icon="🧠")

# --- Sidebar ---
st.sidebar.title("Go to")
page = st.sidebar.radio("", ["Home", "About Us", "Donate Us"])

# --- CSS Styling ---
st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f7f8fa;
        }

        .stButton > button {
            background-color: #6C63FF;
            color: white;
            font-weight: 600;
            border-radius: 10px;
            padding: 0.6em 1.2em;
            border: none;
            transition: background-color 0.3s ease;
        }

        .stButton > button:hover {
            background-color: #5a52d4;
        }

        hr {
            margin: 2rem 0;
            border-top: 1px solid #e0e0e0;
        }

        .center {
            text-align: center;
        }

        section[data-testid="stSidebar"] {
            min-width: 230px !important;
            max-width: 230px !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- Helper: Load Lottie Animation ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ========== HOME PAGE ==========
if page == "Home":
    st_lottie(load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_jcikwtux.json"), height=200, key="header")
    st.markdown("<h2 style='text-align:center;'>MindMate</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Answer a few questions to know your mental health risk.</p>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    st.subheader("Personal & Work Info")
    age = st.slider("Your Age", 18, 65, 25)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    self_employed = st.selectbox("Are you self-employed?", ["Yes", "No"])
    family_history = st.selectbox("Family history of mental illness?", ["Yes", "No"])
    no_of_employees = st.selectbox("Company size", ["1-5", "6-25", "26-100", "100-500", "500-1000", "More than 1000"])
    remote_work = st.selectbox("Do you work remotely?", ["Yes", "No"])
    tech_company = st.selectbox("Is it a tech company?", ["Yes", "No"])

    st.subheader("Workplace Support")
    benefits = st.selectbox("Employer provides mental health benefits?", ["Yes", "No", "Don't know"])
    care_options = st.selectbox("Access to mental health care options?", ["Yes", "No", "Not sure"])
    wellness_program = st.selectbox("Are wellness programs available?", ["Yes", "No", "Don't know"])
    seek_help = st.selectbox("Is help-seeking encouraged?", ["Yes", "No", "Don't know"])
    anonymity = st.selectbox("Is anonymity protected?", ["Yes", "No", "Don't know"])
    leave = st.selectbox("Ease of taking mental health leave?", ["Very easy", "Somewhat easy", "Somewhat difficult", "Very difficult", "Don't know"])
    mental_health_interview = st.selectbox("Would you discuss MH in interview?", ["Yes", "No", "Maybe"])
    phys_health_interview = st.selectbox("Would you discuss physical health?", ["Yes", "No", "Maybe"])

    st.subheader("Attitudes & Impact")
    work_interfere = st.selectbox("Does mental health interfere with work?", ["Never", "Rarely", "Sometimes", "Often"])
    mental_health_consequence = st.selectbox("Mental health affects career?", ["Yes", "No", "Maybe"])
    phys_health_consequence = st.selectbox("Physical health affects career?", ["Yes", "No", "Maybe"])
    coworkers = st.selectbox("Comfortable with coworkers?", ["Yes", "No", "Some of them"])
    supervisor = st.selectbox("Comfortable with supervisor?", ["Yes", "No", "Some of them"])
    mental_vs_physical = st.selectbox("Is mental health as important as physical?", ["Yes", "No", "Don't know"])
    obs_consequence = st.selectbox("Observed MH consequences at work?", ["Yes", "No", "Maybe"])

    def encode(val, mapping): return mapping.get(val, 0)

    input_data = [
        age,
        encode(gender, {"Male": 0, "Female": 1, "Other": 2}),
        encode(self_employed, {"Yes": 1, "No": 0}),
        encode(family_history, {"Yes": 1, "No": 0}),
        encode(no_of_employees, {
            "1-5": 0, "6-25": 1, "26-100": 2, "100-500": 3,
            "500-1000": 4, "More than 1000": 5
        }),
        encode(remote_work, {"Yes": 1, "No": 0}),
        encode(tech_company, {"Yes": 1, "No": 0}),
        encode(benefits, {"Yes": 1, "No": 0, "Don't know": 2}),
        encode(care_options, {"Yes": 1, "No": 0, "Not sure": 2}),
        encode(wellness_program, {"Yes": 1, "No": 0, "Don't know": 2}),
        encode(seek_help, {"Yes": 1, "No": 0, "Don't know": 2}),
        encode(anonymity, {"Yes": 1, "No": 0, "Don't know": 2}),
        encode(leave, {
            "Very easy": 3, "Somewhat easy": 2,
            "Somewhat difficult": 1, "Very difficult": 0,
            "Don't know": 2
        }),
        encode(mental_health_interview, {"Yes": 2, "Maybe": 1, "No": 0}),
        encode(phys_health_interview, {"Yes": 2, "Maybe": 1, "No": 0}),
        encode(work_interfere, {"Never": 0, "Rarely": 1, "Sometimes": 2, "Often": 3}),
        encode(mental_health_consequence, {"Yes": 2, "Maybe": 1, "No": 0}),
        encode(phys_health_consequence, {"Yes": 2, "Maybe": 1, "No": 0}),
        encode(coworkers, {"Yes": 2, "Some of them": 1, "No": 0}),
        encode(supervisor, {"Yes": 2, "Some of them": 1, "No": 0}),
        encode(mental_vs_physical, {"Yes": 2, "Don't know": 1, "No": 0}),
        encode(obs_consequence, {"Yes": 2, "Maybe": 1, "No": 0})
    ]

    if st.button("Check My Mental Health"):
        prediction = model.predict([input_data])[0]
        st.markdown("<hr>", unsafe_allow_html=True)

        if prediction == 1:
            st.error("⚠️ You may be at risk.")
            st.markdown("### Recommended Actions")
            st.markdown("- Practice mindfulness or meditation")
            st.markdown("- Journal your thoughts daily")
            st.markdown("- Talk to a trusted friend or counselor")
            st.markdown("- Consider therapy if you're overwhelmed")
            st.markdown("### Helpful Video")
            st_player("https://www.youtube.com/watch?v=inpok4MKVLM")
        else:
            st.success("✅ You're likely mentally well!")
            st.markdown("### Wellness Tips")
            st.markdown("- Maintain a good work-life balance")
            st.markdown("- Sleep 7–8 hours daily")
            st.markdown("- Stay socially connected")
            st.markdown("- Eat nutritious meals and exercise")
            st.markdown("### Recommended Videos")
            st_player("https://www.youtube.com/watch?v=ZToicYcHIOU")
            st_player("https://www.youtube.com/watch?v=gedoSfZvBgE")
            st_player("https://www.youtube.com/watch?v=UNQhuFL6CWg")

# ========== ABOUT PAGE ==========
elif page == "About Us":
    st.markdown("<h2 style='text-align:center;'>About MindMate</h2>", unsafe_allow_html=True)
    st.write("MindMate is a free mental health screening tool designed to help people assess their mental wellness and get simple tips to improve it.")
    st.markdown("---")
    st.subheader("Links")
    st.markdown("- [GitHub – kushfs](https://github.com/kushfs)")
    st.markdown("- [Portfolio – kushagras.netlify.app](https://kushagras.netlify.app)")
    st.markdown("- Built with ❤️ using Streamlit + Scikit-learn")

# ========== DONATE PAGE ==========
elif page == "Donate Us":
    st.markdown("<h2 style='text-align:center;'>Support Our Work</h2>", unsafe_allow_html=True)
    st.write("If you found this tool helpful and want to support its continued development, you can donate using the UPI ID below:")
    st.markdown("""
    <div class='center'>
        <h3>📱 UPI ID</h3>
        <p style='font-size:1.3rem; font-weight:bold; background:#6C63FF; color:white; padding:0.5rem 1rem; border-radius:10px; display:inline-block;'>kushagrasinha140@okicici</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.info("Any small contribution helps us keep this project free and open to all. Thank you! 🙏")

# --- Hide Streamlit Default Menu ---
hide_streamlit_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
