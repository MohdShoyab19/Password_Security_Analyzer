import streamlit as st
from modules.security import check_password_security

st.set_page_config(page_title="Password Security Analyzer",layout="wide")
st.title("🔒 Intelligent Password Security Analyzer")
st.write("Real-time password security analysis system.")

st.sidebar.title("Navigation")
choice = st.sidebar.radio("Go to:",["Password Tester","Analytics Dashboard"])

if choice == "Password Tester":
    st.header("Password Testing Panel")
    pwd = st.text_input("Enter password to text:",type="password")

    if pwd:
        # Security Module function call
        status, score, tips = check_password_security(pwd)

        st.subheader("Rule-Based Analysis Results")

        # 5-point score bar
        st.progress(score / 5.0)

        # Color feedback according to status output
        if status == "weak":
            st.error(f"Strength: Weak ({score}/5)")
        elif status == "medium":
            st.warning(f"Strength: Medium ({score}/5)")
        else:
            st.success(f"Strength: Strong ({score}/5)")

        # Render Suggestions
        if tips:
            st.markdown("**Recommendations:**")
            for tip in tips:
                st.write(f"-{tip}") 

elif choice == "Analytics Dashboard":
    st.header("Analytics Visualizations")
    st.write("Charts will be shown")
