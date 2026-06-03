# ============================================================
# PROJECT 1: Password Generator & Strength Checker
# By: Subhan Ahmed
# Description: Generates a secure random password based on 
#              user preferences and rates its strength
# ============================================================

# "import" means we are bringing in a pre-built toolkit
# Python comes with these toolkits built in - we don't need to install them

import random   # gives us tools to pick random items
import string   # gives us ready-made sets of characters (letters, digits, symbols)


# ============================================================
# FUNCTION 1: get_valid_length()
# Job: Ask the user for a password length and keep asking
#      until they give us a proper number between 8 and 32
# ============================================================

def get_valid_length():
    # "while True" means: keep looping forever until we tell it to stop
    while True:
        # "try" means: attempt the following code, but if something
        # goes wrong, don't crash - go to "except" instead
        try:
            # input() shows a message and waits for the user to type something
            # int() converts what they typed into a whole number
            # If they type "hello" instead of a number, int() fails
            # and we jump straight to "except"
            length = int(input("\nEnter password length (8-32): "))

            # Now check if the number is in the acceptable range
            if 8 <= length <= 32:
                # "return" sends the value back to whoever called this function
                # and also stops the while loop
                return length
            else:
                # If the number is valid but out of range, tell the user
                print("Please enter a number between 8 and 32.")

        except ValueError:
            # This runs if int() failed because they typed something that
            # isn't a number at all (like letters or symbols)
            print("That wasn't a valid number. Please try again.")


# ============================================================
# FUNCTION 2: get_characters()
# Job: Build a string of all the characters we're allowed to
#      use when generating the password
# Parameters: 4 True/False values the user chose
# ============================================================

def get_characters(use_upper, use_lower, use_numbers, use_symbols):
    # Start with an empty string - we'll add to it based on what the user wants
    characters = ""

    # string.ascii_lowercase is "abcdefghijklmnopqrstuvwxyz" (built into Python)
    # string.ascii_uppercase is "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # string.digits is "0123456789"
    # string.punctuation is all symbols like !@#$%^&*()_+-=

    if use_lower:
        # += means "add this onto the end of what's already in the variable"
        characters += string.ascii_lowercase

    if use_upper:
        characters += string.ascii_uppercase

    if use_numbers:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    # "not characters" checks if the string is still empty
    # This handles the case where the user said no to everything
    if not characters:
        print("\nYou said no to everything - using all character types by default.")
        # We combine all four sets together using + 
        characters = (string.ascii_lowercase + string.ascii_uppercase +
                      string.digits + string.punctuation)

    # Send the finished pool of characters back to whoever called this function
    return characters


# ============================================================
# FUNCTION 3: generate_password()
# Job: Pick random characters from the pool to build the password
# Parameters: how long the password should be, which characters to use
# ============================================================

def generate_password(length, characters):
    # Start with an empty string
    password = ""

    # range(length) counts from 0 up to (but not including) length
    # So if length is 12, this loop runs exactly 12 times
    for i in range(length):
        # random.choice() picks one random item from a sequence
        # Here it picks one random character from our characters string
        # += adds that character onto the end of our growing password
        password += random.choice(characters)

    # Send the finished password back
    return password


# ============================================================
# FUNCTION 4: check_strength()
# Job: Look at the finished password and decide if it's
#      weak, medium, or strong
# Parameter: the completed password string
# ============================================================

def check_strength(password):
    # any() returns True if at least ONE item in a sequence meets the condition
    # c.isupper() checks if a single character is an uppercase letter
    # So this line checks: "does the password contain at least one uppercase letter?"
    has_upper = any(c.isupper() for c in password)

    # c.islower() checks if a character is a lowercase letter
    has_lower = any(c.islower() for c in password)

    # c.isdigit() checks if a character is a number (0-9)
    has_number = any(c.isdigit() for c in password)

    # "c in string.punctuation" checks if a character is a symbol
    has_symbol = any(c in string.punctuation for c in password)

    # sum() on a list of True/False values counts how many are True
    # True counts as 1, False counts as 0
    # So if has_upper=True, has_lower=True, has_number=False, has_symbol=True
    # the score would be 3
    score = sum([has_upper, has_lower, has_number, has_symbol])

    # len() counts the number of characters in the password
    # This checks if the password is 12 or more characters long
    is_long_enough = len(password) >= 12

    # Now decide the rating based on the score and length
    if score == 4 and is_long_enough:
        return "Strong - Excellent password!"
    elif score >= 3:
        return "Medium - Could be stronger"
    elif score >= 2:
        return "Weak - Consider adding more variety"
    else:
        return "Very Weak - Not recommended"


# ============================================================
# MAIN FUNCTION
# Job: The manager. Runs everything in the right order.
# This is where the program actually starts doing things.
# ============================================================

def main():
    # Print the header. The "=" * 40 creates 40 equals signs in a row
    print("=" * 40)
    print("       PASSWORD GENERATOR")
    print("=" * 40)

    # Step 1: Get the password length from the user
    # We call get_valid_length() and store whatever number it returns
    length = get_valid_length()

    # Step 2: Ask what character types to include
    # .lower() converts whatever they type to lowercase
    # so "Y", "y", and "yes" all become "y"
    # == 'y' checks if what they typed (after lowercasing) equals the letter y
    # The whole thing gives us True or False
    print("\nWhat should your password include?")
    use_upper   = input("Uppercase letters (A-Z)?   (y/n): ").lower() == 'y'
    use_lower   = input("Lowercase letters (a-z)?   (y/n): ").lower() == 'y'
    use_numbers = input("Numbers (0-9)?              (y/n): ").lower() == 'y'
    use_symbols = input("Symbols (!@#$...)?          (y/n): ").lower() == 'y'

    # Step 3: Build the character pool using those True/False answers
    characters = get_characters(use_upper, use_lower, use_numbers, use_symbols)

    # Step 4: Generate the actual password
    password = generate_password(length, characters)

    # Step 5: Check how strong it is
    strength = check_strength(password)

    # Step 6: Display the results
    # \n creates a blank line. f"..." is an f-string - it lets you drop
    # variables directly into text using curly braces {variable_name}
    print("\n" + "=" * 40)
    print(f"  Your Password : {password}")
    print(f"  Strength      : {strength}")
    print(f"  Length        : {len(password)} characters")
    print("=" * 40)

    # Step 7: Ask if they want to generate another one
    again = input("\nGenerate another password? (y/n): ").lower()
    if again == 'y':
        # Calling main() inside main() starts the whole program again from the top
        main()
    else:
        print("\nThanks for using Password Generator. Stay safe!")


# ============================================================
# THIS IS THE ENTRY POINT
# This line means: "only run main() if this file is being
# run directly, not imported by another file"
# You will see this in almost every Python project.
# ============================================================

if __name__ == "__main__":
    main()