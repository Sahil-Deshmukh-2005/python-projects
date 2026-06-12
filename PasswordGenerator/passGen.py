import random
import string
from pathlib import Path

char = (
    string.ascii_lowercase +
    string.ascii_uppercase +
    string.digits +
    string.punctuation
)

def password():

    try:
        length = int(input("Enter the length of your password (Default 16): "))
    except:
        print("Invalid Input, Default length selected.")
        length = 16

    if length <= 4:
        print("Length should be more than 4.")
        return 

    password_generated = f"{random.choice(string.ascii_lowercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.digits)}{random.choice(string.punctuation)}"
    for _ in range(length-4):
        password_generated += random.choice(char)
    
    pass_list = list(password_generated)
    random.shuffle(pass_list)

    password_generated = "".join(pass_list)

    password_path = Path("passwords.txt")
    password_path.touch(exist_ok=True)

    with open("passwords.txt","a") as f:
        f.write(password_generated+"\n")

    return password_generated

print(password())
