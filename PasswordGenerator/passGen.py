import random
import string
from pathlib import Path

# lower_alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# upper_alphabet = [i.upper() for i in lower_alphabet]
# numbers = [0,1,2,3,4,5,6,7,8,9]
# symbols = ["`","~","!","@","#","$","%","^","&","*","(",")","_","-","=","+","[","]","{","}","|",";",":","'",'"',"<",">","/","\\","?",".",","]

# lst = [lower_alphabet,upper_alphabet,numbers,symbols]

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
        length = 16

    if length <= 4:
        print("Length should be more than 4.")
        return 

    password_generated = f"{random.choice(string.ascii_lowercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.digits)}{random.choice(string.punctuation)}"
    for _ in range(length-4):
        # choose = random.choice(lst)
        password_generated += random.choice(char) # char already is a string to we dont have to typecast it to str
    
    pass_list = list(password_generated)
    random.shuffle(pass_list) # because we cannot shuffle string so we converted it into a list 

    password_generated = "".join(pass_list)

    password_path = Path("PassGen/passwords.txt")
    password_path.touch(exist_ok=True)

    with open("PassGen/passwords.txt","a") as f:
        f.write(password_generated+"\n")

    return password_generated

print(password())