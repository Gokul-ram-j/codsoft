import random

generated_password=""
print("|________PASSWORD GENERATOR________|")
password_length=int(input("enter the length of the password:").strip())

for i in range(password_length):
    capital_alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small_alphabet="abcdefghijklmnopqrstuvwxyz"
    numbers="123456789"
    symbol=".,*?!@#^&%"
    character_type=random.choice([capital_alphabet,small_alphabet,numbers,symbol])
    character=random.choice(character_type)
    generated_password+=character
print("--------------------")
print("THE PASSWORD GENERATED IS :",generated_password)
print("--------------------")
