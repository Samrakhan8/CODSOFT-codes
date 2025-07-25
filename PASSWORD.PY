import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    # Character sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    # Ensure password has at least one of each type
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Fill the rest of the password length with random choices
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to avoid predictable pattern
    random.shuffle(password)

    return ''.join(password)

# Main program
try:
    length = int(input("Enter the desired password length: "))
    password = generate_password(length)
    print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number.")
