import random

symbols = "0qwert1yuiop2asdfgh3jkl4zxc6vbn5mQ7WE8RT9YUIOPASDFGHJKLZXCVBNM"

length = int(input("Enter pas len : "))
count  = int(input("Enter pass count : "))
password =  ""
for i in range(count):
    for j in range(length):
        password += random.choice(symbols)
    print(password, end="\n")
    password = ""