# 🔐 Password Generator

A secure and customizable password generator built with Python and Streamlit.

The application allows users to generate passwords based on their preferred length and character types, while also providing a password strength indicator.

## 🚀 Live Demo

Coming soon: The application will be deployed with Streamlit Community Cloud.

## ✨ Features

- Custom password length from 4 to 50 characters
- Uppercase letter option
- Number option
- Special character option
- Cryptographically secure random generation
- Password strength indicator
- Copy generated passwords directly from the interface
- Interactive Streamlit web interface
- Command-line version included

## 🛠️ Technologies

- Python
- Streamlit
- `secrets`
- Git
- GitHub

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Ayech14/password_generator.git
cd password-generator
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Usage

### Web Application

Run the Streamlit application:

```bash
streamlit run app.py
```

Your browser should open the application automatically.

### Using the Web Application

1. Choose the desired password length using the slider.
2. Select whether to include:
   - Uppercase letters
   - Numbers
   - Special characters
3. Click **Generate Password**.
4. Copy the generated password using the copy button.
5. Review the estimated password strength.
6. Adjust the settings and generate another password whenever needed.

### Command-Line Version

You can also run the command-line version:

```bash
python3 main.py
```

Follow the prompts to select the password length and character types.

## 📁 Project Structure

```text
password-generator/
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
├── password_generator.py
└── app.py
```

### `password_generator.py`

Contains the core password-generation and password-strength logic.

### `main.py`

Provides a command-line interface for the password generator.

### `app.py`

Provides the Streamlit web interface.

## 🔐 How It Works

The password generator uses Python's `secrets` module for cryptographically secure random character selection rather than the standard `random` module.

Users can customize:

- Password length
- Uppercase letters
- Numbers
- Special characters

The generator guarantees at least one character from each selected character category.

## 📊 Password Strength

The application provides a simple password-strength estimate based on:

- Password length
- Lowercase letters
- Uppercase letters
- Numbers
- Special characters

The strength indicator is an educational heuristic and is not a replacement for a dedicated password-strength estimator.

## 🔒 Security Note

This project uses Python's `secrets` module, which is designed for generating cryptographically secure random values.

The application does not store generated passwords.

## 🔮 Future Improvements

- More advanced password-strength estimation
- Optional avoidance of duplicate characters
- Additional password customization options
- Public deployment
- UI enhancements