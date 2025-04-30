# 🧠 Mental Health Assessment & Recommendation System

This is a simple AI-powered web app built using **Streamlit** to assess mental health risk based on user responses to PHQ-9 and GAD-7 questionnaires. It provides personalized recommendations based on the predicted risk level.

## 🚀 Live Demo

👉 [Click here to try the app](https://your-username.streamlit.app)  
*(Replace with your actual Streamlit Cloud link once deployed)*

---

## 💡 Features

- PHQ-9 and GAD-7 questions combined in one form
- Machine learning model (Random Forest Classifier) trained on synthetic data
- Predicts mental health risk: **Low**, **Moderate**, or **High**
- Offers personalized self-care or professional help recommendations
- Built entirely with Python and Streamlit

---

## 📦 Files

| File             | Description                                  |
|------------------|----------------------------------------------|
| `app.py`         | Main Streamlit app                           |
| `requirements.txt` | Python dependencies                         |
| `README.md`      | Project documentation                        |
| `mental_model.pkl` | ML model saved after training (auto-created) |

---

## 🛠 Installation & Run Locally

1) **Clone the repository**
   ```bash
   git clone https://github.com/your-username/mental-health-app.git
   cd mental-health-app


2) Create a virtual environment (optional but recommended)

python -m venv venv
mac :source venv/bin/activate  # On Windows: venv\Scripts\activate

3)Install dependencies

pip install -r requirements.txt
Run the app


4) streamlit run app.py
📤 Deploy to Streamlit Cloud
Push the project to a GitHub repository

Go to https://streamlit.io/cloud

Click "New app", select your GitHub repo, and deploy!
