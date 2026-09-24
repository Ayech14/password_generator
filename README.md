# 🔐 Password Generator

A secure and customizable password generator built with Python and Streamlit.

The application allows users to generate passwords based on their preferred
length and character types, while also providing a password strength indicator.

## Features

- Custom password length from 4 to 50 characters
- Uppercase letter option
- Number option
- Special character option
- Cryptographically secure random generation
- Password strength indicator
- Copy generated passwords directly from the interface
- Interactive Streamlit web interface
- Command-line version included

## Technologies

- Python
- Streamlit
- `secrets`
- Git
- GitHub

## How It Works

The password generator uses Python's `secrets` module for random character
selection rather than the standard `random` module.

Users can customize:

- Password length
- Uppercase letters
- Numbers
- Special characters

The application guarantees at least one character from each selected category.

## Project Structure

```text
password-generator/
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
├── password_generator.py
└── app.py