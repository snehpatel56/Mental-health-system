import streamlit as st
import pandas as pd
import numpy as np
import os
import time
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import joblib

# -------------------------------
# Page Config
st.set_page_config(page_title="Mental Health Assessment", layout="centered")
st.title("Mental Health Assessment & Recommendation System")

# -------------------------------
# PHQ-9 + GAD-7 Questions
questions = {
    "PHQ-9 Depression Questions": [
        "Little interest or pleasure in doing things?",
        "Feeling down, depressed, or hopeless?",
        "Trouble falling or staying asleep, or sleeping too much?",
        "Feeling tired or having little energy?",
        "Poor appetite or overeating?",
        "Feeling bad about yourself — or that you are a failure?",
        "Trouble concentrating on things?",
        "Moving or speaking slowly — or the opposite?",
        "Thoughts that you would be better off dead or hurting yourself?"
    ],
    "GAD-7 Anxiety Questions": [
        "Feeling nervous, anxious, or on edge?",
        "Not being able to stop or control worrying?",
        "Worrying too much about different things?",
        "Trouble relaxing?",
        "Being so restless that it's hard to sit still?",
        "Becoming easily annoyed or irritable?",
        "Feeling afraid something awful might happen?"
    ]
}

options = {
    "Not at all": 0,
    "Several days": 1,
    "More than half the days": 2,
    "Nearly every day": 3
}

# -------------------------------
# Train Dummy Model if not exists
def train_and_save_model():
    data = []
    for _ in range(300):
        phq = np.random.randint(0, 4, size=9)
        gad = np.random.randint(0, 4, size=7)
        total = sum(phq) + sum(gad)
        label = "High" if total > 20 else "Moderate" if total > 10 else "Low"
        data.append(list(phq) + list(gad) + [label])
    df = pd.DataFrame(data, columns=[f"q{i+1}" for i in range(16)] + ["label"])

    X = df.drop("label", axis=1)
    le = LabelEncoder()
    y = le.fit_transform(df["label"])
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    joblib.dump((model, le), "mental_model.pkl")

# -------------------------------
# Load or Cache Model
@st.cache_resource
def load_model():
    if not os.path.exists("mental_model.pkl"):
        train_and_save_model()
    return joblib.load("mental_model.pkl")

model, label_encoder = load_model()

# -------------------------------
# Questionnaire UI
st.subheader("Answer the following questions:")
responses = []

with st.form("mental_health_form"):
    for section, qs in questions.items():
        st.markdown(f"**{section}**")
        for q in qs:
            choice = st.radio(q, list(options.keys()), key=q)
            responses.append(options[choice])
    submitted = st.form_submit_button("Submit")

# -------------------------------
# Predict & Recommend
if submitted:
    with st.spinner("Analyzing your responses..."):
        time.sleep(1.5)
        prediction = model.predict([responses])[0]
        label = label_encoder.inverse_transform([prediction])[0]

    st.success(f"**Your Mental Health Risk Level: {label}**")

    st.subheader("Personalized Recommendations")
    if label == "Low":
        st.write("Keep up your healthy habits! Practice mindfulness and maintain work-life balance.")
    elif label == "Moderate":
        st.write("Try relaxation techniques, talk to a friend or counselor, and improve sleep & diet.")
    else:
        st.write("Consider seeking professional help. Visit trusted sites like [BetterHelp](https://www.betterhelp.com) or [TherapyRoute](https://www.therapyroute.com).")

# -------------------------------
# Footer
st.markdown("---")
st.caption("Built with using Streamlit · Not a substitute for clinical diagnosis.")
