password = input("enter a password : ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

for char in password:

    if char.islower():
        has_lower = True
    elif char.isupper():
        has_upper = True
    elif char.isdigit():
        has_digit = True
    elif char in special_chars:
        has_special = True

if (len(password) >= 8 and 
    has_upper and
    has_lower and 
    has_digit and 
    has_special):

    print("strong password.")

else:
    print("weak password")

if len(password) < 8 :
    print("password must be 8 characters long!")
elif not has_upper :
    print("atleast one uppercase letter")
elif not has_lower :
    print("altleast one lowercase letter")
elif not has_upper :
    print("atleast one digit")
elif not has_upper :
    print("atleast one special character")
