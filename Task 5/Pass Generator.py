'''Password Generator

1.The program should prompt the user to specify the desired password length.

2.The user should be able to choose whether to include uppercase letters, lowercase letters, digits, and/or special characters in the generated password.

3.Based on the user's choices, the program should generate a random password that meets the specified criteria.

4.The generated password should be displayed to the user.

5.The program should provide an option to generate a new password or exit.

provide a python program'''

import random
import string

def generate_password(length, include_uppercase, include_lowercase, include_digits, include_special_chars):
    characters = ''
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    if characters == '':
        print("Error")
        return None

    generated_password = ''.join(random.choice(characters) for _ in range(length))
    return generated_password

def password_generator():
    while True:
        print("\nPassword Generator")
        try:
            length = int(input("Enter password length: "))
            if length <= 0:
                raise ValueError("Password length must be a positive integer.")
        except ValueError as e:
            print("Invalid input:", e)
            continue

        include_uppercase = input("Include uppercase letters? (yes/no): ").lower().strip() == 'y'
        include_lowercase = input("Include lowercase letters? (yes/no): ").lower().strip() == 'y'
        include_digits = input("Include digits? (yes/no): ").lower().strip() == 'y'
        include_special_chars = input("Include special characters? (yes/no): ").lower().strip() == 'y'

        generated_password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_special_chars)
        if generated_password:
            print("Generated Password:", generated_password)

        if input("Generate another password? (yes/no): ").lower().strip() != 'y':
            break

if __name__ == "__main__":
    password_generator()