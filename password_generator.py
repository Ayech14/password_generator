import secrets


alpha = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
special = "@#$%&*"


def generate_password(length, use_uppercase, use_numbers, use_special):
    """Generate a password based on the selected character options."""
    characters = alpha
    password = []

    if use_uppercase:
        characters += alpha.upper()
        password.append(alpha.upper()[secrets.randbelow(len(alpha))])

    if use_numbers:
        characters += num
        password.append(num[secrets.randbelow(len(num))])

    if use_special:
        characters += special
        password.append(special[secrets.randbelow(len(special))])

    remaining = length - len(password)

    for i in range(remaining):
        index = secrets.randbelow(len(characters))
        password.append(characters[index])

    secrets.SystemRandom().shuffle(password)

    return "".join(password)


def calculate_strength(password):
    """Estimate password strength based on length and character variety."""

    score = 0

    if len(password) >= 8:
        score += 1

    if any(character.islower() for character in password):
        score += 1

    if any(character.isupper() for character in password):
        score += 1

    if any(character.isdigit() for character in password):
        score += 1

    if any(character in special for character in password):
        score += 1

    if score <= 2:
        return "Weak"

    if score <= 4:
        return "Medium"

    return "Strong"