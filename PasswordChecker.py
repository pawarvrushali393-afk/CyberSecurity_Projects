import re

def check_password(password):
    strength = "Weak"

    if len(password) >= 8:
        if re.search("[a-z]", password) and \
           re.search("[A-Z]", password) and \
           re.search("[0-9]", password) and \
           re.search("[@#$%^&*]", password):
            strength = "Strong"
        else:
            strength = "Medium"

    return strength

password = input("Enter password: ")
print("Password Strength:", check_password(password))