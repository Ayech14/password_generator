import secrets


alpha = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
special = "@#$%&*"



def generate_password(length, use_uppercase, use_numbers, use_special):
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
gen_password = generate_password(
    pass_len,
    use_uppercase,
    use_numbers,
    use_special
)

print(f"Generated Password: {gen_password}")