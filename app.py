import streamlit as st

from password_generator import generate_password, calculate_strength


st.title("🔐 Password Generator")

st.write("Create a secure password with customizable options.")

st.divider()

st.subheader("Password Settings")


length = st.slider(
    "Password Length",
    min_value=4,
    max_value=50,
    value=12
)

col1, col2, col3 = st.columns(3)

with col1:
    use_uppercase = st.checkbox("Uppercase", value=True)

with col2:
    use_numbers = st.checkbox("Numbers", value=True)

with col3:
    use_special = st.checkbox("Special", value=True)


if st.button("Generate Password", use_container_width=True):
    password = generate_password(
        length,
        use_uppercase,
        use_numbers,
        use_special
    )

    strength = calculate_strength(password)

    st.divider()

    st.subheader("Generated Password")

    st.code(password, language=None)

    st.markdown(f"**Password Strength:** `{strength}`")