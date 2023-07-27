import random
password = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@~#$%^&*()[]{}-_<>"
length_password = int(input("Entre the length of password:"))
a = "".join(random.sample(password,length_password))
print(f"Your password is {a}")


