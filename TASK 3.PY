import random
import string

def generate_password(length, complexity=4):
    """
    Generates a random password based on the specified length and complexity.
    complexity:
      1 - Only lowercase letters
      2 - Lowercase + uppercase letters
      3 - Lowercase + uppercase + digits
      4 - Lowercase + uppercase + digits + special characters
    """

    if complexity == 1:
        characters = string.ascii_lowercase
    elif complexity == 2:
        characters = string.ascii_letters
    elif complexity == 3:
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    # Prompt the user for input
    try:
        length = int(input("Enter the desired password length: "))
    except ValueError:
        print("Invalid input! Please enter a valid integer for the password length.")
        return

    print("\nSelect password complexity:")
    print("1. Lowercase letters only")
    print("2. Lowercase + Uppercase letters")
    print("3. Lowercase + Uppercase + Digits")
    print("4. Lowercase + Uppercase + Digits + Special characters")

    try:
        complexity = int(input("Enter your choice (1/2/3/4): "))
        if complexity not in [1, 2, 3, 4]:
            print("Invalid choice! Please select a valid complexity level (1/2/3/4).")
            return
    except ValueError:
        print("Invalid input! Please enter a valid number for complexity.")
        return

    # Generate and display the password
    password = generate_password(length, complexity)
    print("\nGenerated Password: ", password)

if __name__ == "__main__":
    main()
