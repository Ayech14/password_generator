import streamlit as st

from password_generator import generate_password, calculate_strength


st.title("🔐 Password Generator")

st.write("Create a secure password with customizable options.")


length = st.slider(
    "Password Length",
    min_value=4,
    max_value=50,
    value=12
)

use_uppercase = st.checkbox("Include uppercase letters", value=True)
use_numbers = st.checkbox("Include numbers", value=True)
use_special = st.checkbox("Include special characters", value=True)


if st.button("Generate Password"):
    password = generate_password(
        length,
        use_uppercase,
        use_numbers,
        use_special
    )

    strength = calculate_strength(password)

    st.subheader("Generated Password")
    st.code(password)

    st.write(f"**Password Strength:** {strength}")