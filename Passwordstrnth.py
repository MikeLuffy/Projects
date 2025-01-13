#Here firstly we creat a function that holds many other small interconnect functions.#

def check_password_strength(password):
    """Check the strength of a password."""
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    
    if not any(char.isupper() for char in password):
        return "Weak: Password must contain at least one uppercase letter."
    
    if not any(char.islower() for char in password):
        return "Weak: Password must contain at least one lowercase letter."
    
    if not any(char.isdigit() for char in password):
        return "Weak: Password must contain at least one digit."
    
    if not any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in password):
        return "Weak: Password must contain at least one special character."
    ##IF user try to input any popular or simple password that attacker can easily guess and perform unethical work so the we warned the user...#
    common_passwords = ["password", "123456", "123456789", "qwerty", "abc123"]
    if password.lower() in common_passwords:
        return "Weak: Password is too common."
   # Otherwise it return strong password#
    return "Strong: Password is strong."

# Example usage to provide overcome of passwordstrenth #
if __name__ == "__main__":
    user_password = input("Enter your password: ")
    strength = check_password_strength(user_password)
    print(strength)