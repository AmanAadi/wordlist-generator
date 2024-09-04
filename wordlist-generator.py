# importing modules
import random
import string as st

# getting inputs
password_characters = input("\nWhat you want in your password, Type:- \n[d] for digits\n[l] for lowercase\n[u] for uppercase\n[p] for punctuation\n[a] to use all\n>>> ")
password_length = int(input("\n[+] Enter length of password: "))
no_of_passwords = int(input("\n[+] Enter number of passwords you want to generate: "))
print("\n")


# creating function to generate a single random password as per user choice.
def password():
    characters = []
    digit = st.digits
    lower = st.ascii_lowercase
    upper = st.ascii_uppercase
    punctuation = st.punctuation

    if "d" in password_characters:
        characters += digit
    if "l" in password_characters:
        characters += lower
    if "u" in password_characters:
        characters += upper
    if "p" in password_characters:
        characters += punctuation
    if "a" in password_characters:
        characters += (digit + lower + upper + punctuation)

    random.shuffle(characters)
    password = ''.join(characters[:password_length])
    return password


# creating a list of passwords that contain the number of passwords that user wants.
password_list = []
for i in range(no_of_passwords):
    password_list.append(password())

# As we know that python data type set does not contain duplicate elements so we are converting that password list into set so that no two passwords are same.
unique_passwords = set(password_list)

# Iterating over the set and saving each password in a passwords.txt file at the given path location.
# with open("C:/Users/amant/Desktop/passwods.txt", 'w') as t:
#     for pas in unique_passwords:
#         t.write(f"{pas}\n")

# printing all passwords one by one
for pasw in unique_passwords:
    print(pasw)

print("\n")
