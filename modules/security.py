# =========================================================
# Module 1: Rule-Based Password Analysis
# Core Rule Logic: Contributed by Team Member (Jayati Shivam)
# UI Integration & Refactoring: Developed by Mohd Shoyab
# =========================================================
import string

def check_password_security(password):
    # Security Improvement: Common weak passwords catch karna
    common_passwords = ["123456", "password", "qwerty", "12345678", "admin", "123456789"]
    
    if password.lower() in common_passwords:
        return "weak", 0, ["Ye password extremely common hai! Kripya secure password chunein."]

    # Teammate (Member 1) ka main 5-rule dictionary logic
    rules = {
        "Length kam se kam 8 characters honi chahiye": len(password) >= 8,
        "Kam se kam ek Uppercase letter (A-Z) add karein": any(a.isupper() for a in password),
        "Kam se kam ek Lowercase letter (a-z) add karein": any(a.islower() for a in password),
        "Kam se kam ek Number (0-9) include karein": any(a.isdigit() for a in password),
        "Special character (!@#$%^&*) include karein": any(a in string.punctuation for a in password)
    }

    # Missing suggestions list generate karna
    suggestions = [msg for msg, passed in rules.items() if not passed]
    score = 5 - len(suggestions)

    # Password strength determine karna
    if score == 5:
        strength = "strong"
    elif score >= 3:
        strength = "medium"
    else:
        strength = "weak"

    return strength, score, suggestions