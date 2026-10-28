# =========================================================
# Module 2: Machine Learning Password Classifier
# Model Training & Vectorizer: Contributed by Team Member (Sarv Shreshth)
# UI Integration & Integration Logic: Developed by Mohd Shoyab
# =========================================================

import joblib

# 1. Loading Saved Files into memory.
model = joblib.load("password_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

labels = {0: "Weak", 1: "Medium", 2: "Strong"}

def predict_password_ml(password):
    if not password:
        return "No input"

    # 2. Changing Text Password to Numbers.
    vec = vectorizer.transform([password])

    # 3. Asking the Model for the outpits 0,1 and 2.
    pred = model.predict(vec)[0]

    # 4. Changing Numbers to readable Text("Weak"/"Medium"/"Strong") and return.
    return labels.get(pred, "Unknown")