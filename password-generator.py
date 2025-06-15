import streamlit as st
import random
import string

# App config
st.set_page_config(page_title="Password Generator", page_icon="🔐", layout="centered")
st.title("🔐 Password Generator")
st.markdown("Create strong, secure, and random passwords instantly.")

# Input for length
length = st.slider("Select password length", min_value=4, max_value=50, value=12)

# Complexity options
use_upper = st.checkbox("Include Uppercase Letters (A-Z)", value=True)
use_lower = st.checkbox("Include Lowercase Letters (a-z)", value=True)
use_digits = st.checkbox("Include Numbers (0-9)", value=True)
use_special = st.checkbox("Include Special Characters (!, @, #, etc.)", value=True)

# Button to generate
if st.button("Generate Password"):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        st.error("⚠️ Please select at least one character type.")
    else:
        password = ''.join(random.choice(characters) for _ in range(length))
        st.success("✅ Your secure password:")
        st.code(password, language="text")
