import re
import random
import string
import streamlit as st

# Created by Areeba Shabbir - A simple yet powerful password strength meter

# Function to check password strength
def check_password_strength(password):
    """Checks the strength of a given password and provides feedback."""
    
    # List of common weak passwords to reject
    common_passwords = {"password", "123456", "password123", "qwerty", "abc123"}
    if password in common_passwords:
        return "Weak", ["Your password is too common. Choose a more secure one."]
    
    # Scoring system based on password criteria
    score = sum([
        len(password) >= 8,  # Check minimum length
        bool(re.search(r"[A-Z]", password)),  # Check for uppercase letter
        bool(re.search(r"[a-z]", password)),  # Check for lowercase letter
        bool(re.search(r"\d", password)),  # Check for digit
        bool(re.search(r"[!@#$%^&*]", password))  # Check for special character
    ])
    
    # Generate feedback for weak passwords
    feedback = []
    if len(password) < 8:
        feedback.append("Increase length to at least 8 characters.")
    if not re.search(r"[A-Z]", password):
        feedback.append("Add at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        feedback.append("Add at least one lowercase letter.")
    if not re.search(r"\d", password):
        feedback.append("Include at least one digit (0-9).")
    if not re.search(r"[!@#$%^&*]", password):
        feedback.append("Include at least one special character (!@#$%^&*).")
    
    # Determine strength based on score
    return ("Weak", feedback) if score <= 2 else ("Moderate", feedback) if score <= 4 else ("Strong", ["Your password is strong! ✅"])

# Function to generate a strong random password
def generate_strong_password(length=12):
    """Generates a strong random password with letters, digits, and special characters."""
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(length))

# Function to copy the generated password to clipboard
def copy_to_clipboard(password):
    """Copies the generated password to the clipboard (Streamlit workaround)."""
    st.text_input("Copy this password:", password)

# Streamlit UI
st.markdown("""
    <div style='text-align: center; padding: 10px;'>
        <h2 style='color: #4CAF50;'>🔐 Password Strength Meter</h2>
        <h4 style='color: #555;'>by Areeba Shabbir</h4>
        <p style='color: #777;'>Ensure your password is secure and strong.</p>
    </div>
    """, unsafe_allow_html=True)
st.write("A simple tool to evaluate password strength and suggest improvements.")
password = st.text_input("Enter a password to check its strength:", type="password")

# Check password strength when button is clicked
if st.button("Check Strength"):
    if password:
        strength, feedback = check_password_strength(password)
        st.subheader(f"Password Strength: {strength}")
        for suggestion in feedback:
            st.write(f"- {suggestion}")
    else:
        st.warning("Please enter a password.")

# Generate a strong password when button is clicked
if st.button("Generate Strong Password"):
    strong_password = generate_strong_password()
    st.text(f"Suggested Strong Password: {strong_password}")
    copy_to_clipboard(strong_password)
