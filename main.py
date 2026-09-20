from password_generator import generate_password, calculate_strength


def get_yes_no(prompt):
    while True:
        answer = input(prompt).lower()

        if answer in ("y", "yes"):
            return True

        if answer in ("n", "no"):
            return False

        print("Please enter yes or no.")


while True:
    try:
        pass_len = int(input("Enter Password Length: "))

        if pass_len < 4:
            print("Password length must be at least 4.")
            continue

        break

    except ValueError:
        print("Please enter a valid number.")


use_uppercase = get_yes_no("Include uppercase letters? (y/n): ")
use_numbers = get_yes_no("Include numbers? (y/n): ")
use_special = get_yes_no("Include special characters? (y/n): ")

selected_categories = 1

if use_uppercase:
    selected_categories += 1

if use_numbers:
    selected_categories += 1

if use_special:
    selected_categories += 1

if pass_len < selected_categories:
    print(
        f"Password length must be at least {selected_categories} "
        "for the selected options."
    )
    exit()
while True:
    gen_password = generate_password(
        pass_len,
        use_uppercase,
        use_numbers,
        use_special
    )

    strength = calculate_strength(gen_password)

    print(f"\nGenerated Password: {gen_password}")
    print(f"Password Strength: {strength}")

    generate_again = get_yes_no("Generate another password? (y/n): ")

    if not generate_again:
        print("Goodbye!")
        break