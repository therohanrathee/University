# Password Generator
import random
import string

def generate_password(length, use_uppercase, use_numbers, use_specials):
    """
    Generates a random password based on the user's preferences.

    Parameters:
    - length (int): Length of the password.
    - use_uppercase (bool): Whether to include uppercase letters.
    - use_numbers (bool): Whether to include numbers.
    - use_specials (bool): Whether to include special characters.

    Returns:
    - str: The generated password.
    """
    if length < 4:
        print("Password length should be at least 4 for security.")
        return None

    # Base character set with lowercase letters
    characters = list(string.ascii_lowercase)
    
    if use_uppercase:
        characters += list(string.ascii_uppercase)
    if use_numbers:
        characters += list(string.digits)
    if use_specials:
        characters += list("!@#$%^&*()-_=+[]{}|;:,.<>?/")

    if not characters:
        print("You must select at least one character type.")
        return None

    # Ensure the password includes at least one of each selected type
    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_numbers:
        password.append(random.choice(string.digits))
    if use_specials:
        password.append(random.choice("!@#$%^&*()-_=+[]{}|;:,.<>?/"))

    # Fill the rest of the password length
    while len(password) < length:
        password.append(random.choice(characters))

    # Shuffle the password to ensure randomness
    random.shuffle(password)
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    
    try:
        length = int(input("Enter the desired password length (minimum 4): "))
        use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == "yes"
        use_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
        use_specials = input("Include special characters? (yes/no): ").strip().lower() == "yes"
    except ValueError:
        print("Invalid input. Please enter numeric values where required.")
        return

    password = generate_password(length, use_uppercase, use_numbers, use_specials)
    if password:
        print(f"\nYour generated password is: {password}")
        print("Keep it safe!")

if __name__ == "__main__":
    main()
