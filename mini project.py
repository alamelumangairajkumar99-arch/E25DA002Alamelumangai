#first week project
import re 
password=input("Enter your password:")
length=len(password)>=8
up=any(char.isupper() for char in password)
low=any(char.islower() for char in password)
digi=any(char.isdigit() for char in password)
special=any(char in "!@#$%^&*" for char in password)
score=sum([length,up,low,digi,special])
if score==5:
    stren="strong password"
elif score>=3:
    stren="moderate password"
else:
    stren="weak password"
print("password strength:",stren)
print("length>=8 characters" if length else "too short(minimum 8 characters)")
print("contains uppercase letter" if up else "no uppercase letters")
print("contains lowercase letter" if low else "no lowercase letters")
print("contains digits" if digi else "no digits")
print("contains special charcters" if special else "no special charcters")
