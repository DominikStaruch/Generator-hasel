import sys
import string
import random
from random import shuffle

random.choice(string.ascii_letters)

password = []
password_length = int(input("Ile znaków ma mieć hasło? "))
counting_down=password_length

char_left=password_length

if password_length < 5:
    print("Hasło jest zbyt krótkie")
    sys.exit(0)
else:
    pass


lowercase_letters = int(input("Ile małych liter ma mieć hasło? "))
counting_down-=lowercase_letters
print(f"Pozostało {counting_down} znaków")

uppercase_letters = int(input("Ile dużych liter ma mieć hasło? "))
counting_down-=uppercase_letters
print(f"Pozostało {counting_down} znaków")

special_characters = int(input("Ile znakow specjalnych ma mieć hasło? "))
counting_down-=special_characters
print(f"Pozostało {counting_down} znaków")

digits = int(input("Ile cyfr ma mieć hasło? "))
counting_down-=digits

if   lowercase_letters + uppercase_letters + special_characters + digits > password_length:
    print("Niewystarczająca długość hasła")
    sys.exit(0)
elif lowercase_letters + uppercase_letters + special_characters + digits < password_length:
    print("Hasło zbyt długie")
    sys.exit(0)
else:
    pass


def lowecase():
    letters = []
    for i in range(lowercase_letters):
       letters.append(random.choice(string.ascii_lowercase))
    return letters

def uppercase():
    letters = []
    for i in range(uppercase_letters):
       letters.append(random.choice(string.ascii_uppercase))
    return letters

def special():
    letters = []
    for i in range(special_characters):
       letters.append(random.choice(string.punctuation))
    return letters

def digit():
    letters = []
    for i in range(digits):
       letters.append(random.choice(string.digits))
    return letters


wynik = lowecase()+uppercase()+special()+digit()
shuffle(wynik)
łącznik = ''
print(łącznik.join(wynik))