import math
import secrets


alpha = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
special = "@#$%&*"


def generate_pass(length, array, is_alpha=False):
    characters = []

    for i in range(length):
        index = secrets.randbelow(len(array))
        character = array[index]

        if is_alpha:
            case = secrets.randbelow(2)

            if case == 1:
                character = character.upper()

        characters.append(character)

    return characters


def generate_password(pass_len):
    alpha_len = pass_len // 2
    num_len = math.ceil(pass_len * 30 / 100)
    special_len = pass_len - (alpha_len + num_len)

    password = []

    password += generate_pass(alpha_len, alpha, True)
    password += generate_pass(num_len, num)
    password += generate_pass(special_len, special)

    secrets.SystemRandom().shuffle(password)

    return "".join(password)


while True:
    try:
        pass_len = int(input("Enter Password Length: "))

        if pass_len < 4:
            print("Password length must be at least 4.")
            continue

        break

    except ValueError:
        print("Please enter a valid number.")


gen_password = generate_password(pass_len)

print(f"Generated Password: {gen_password}")