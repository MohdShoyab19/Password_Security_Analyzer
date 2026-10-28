# =========================================================
# Module 3: Analytics & Data Visualization
# Data Analysis & Plotting Logic: Contributed by Team Member (Priyansh Sharma)
# UI Integration & Logic Wiring: Developed by Mohd Shoyab
# =========================================================

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

@st.cache_data
def load_dataset():
    # Load Dataset and Clean it.
    df = pd.read_csv("data.csv", on_bad_lines="skip")
    df = df.dropna().drop_duplicates()
    df["password"] = df["password"].astype(str)

    # Calculate the features
    df["length"] = df["password"].str.len()
    df["has_digit"] = df["password"].str.contains(r"\d")
    df["has_upper"] = df["password"].str.contains(r"[A-Z]")
    df["has_symbol"] = df["password"].str.contains(r"[^A-Za-z0-9]")

    return df

def render_analytics_dashboard():
    st.subheader("Data Analytics & Insights Dashboard")

    # Fetching Dataset
    df = load_dataset()

    # Graph 1: Password Strength Distribuition
    fig1, ax1 = plt.subplots(figsize=(6,4))
    counts = df["strength"].value_counts().sort_index()
    counts.index = ["Weak (0)", "Medium (1)", "Strong (2)"]
    counts.plot(kind="bar",color=["red", "orange", "green"], ax = ax1)
    ax1.set_title("Password Strength Distribuition")
    ax1.set_ylabel("Count")
    st.pyplot(fig1)

    # Graph 2: Average Password Length
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    avg_len = df.groupby("strength")["length"].mean()
    avg_len.index = ["Weak (0)", "Medium (1)", "Strong (2)"]
    avg_len.plot(kind="bar", color="skyblue", ax=ax2)
    ax2.set_title("Average Password Length by Strength")
    ax2.set_ylabel("Average Length (Characters)")
    st.pyplot(fig2)

    # Graph 3: Character Types Usage (%)
    fig3, ax3 = plt.subplots(figsize=(6,4))
    char_types = (
        df.groupby("strength")[["has_digit", "has_upper", "has_symbol"]].mean()
        * 100
    )
    char_types.index = ["Weak (0)", "Medium (1)", "Strong (2)"]
    char_types.plot(kind="bar", ax=ax3)
    ax3.set_title("Character Types Usage (%)")
    ax3.set_ylabel("Percentage (%)")
    st.pyplot(fig3)