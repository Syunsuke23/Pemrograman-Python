 #ini ada file user.csv
  Reynaldo,reynaldo,admin
Syunsuke,syunsuke,,moderator
Kei,kei,user

#1. membaca SCV  
  import csv

users = open("user.csv", "r")

user_csv = csv.reader(users, delimiter=",")

for row in user_csv:
    print(f"Name : {row[0]}, Username : {row[1]}, Role : {row[-1]}")

users.close()

#2. With Block

import csv

with open("user.csv","r")  as users:
    users_csv = csv.reader(users, delimiter=",")

    for row in users_csv:
        print(f"Name : {row[0]},Role : {row[-1]}")

#3. Module

#import matematika
from matematika import plus

result = plus(10,8)
print(result)

result = plus(10, 10)
print(result)

#4. Package
#kondisinya ketika file matematika.py dipindahkan ke folder bernama marketplace
from marketplace.matematika import plus, minus

result = plus(10, 8)
print(result)

result = minus(10, 8)
print(result)

#5. Random

import random

users = ['Agung', 'Renal', 'Kei', 'Tony', 'Romero']

winner = random.choice(users)
print(winner)

#6. PIP dan Virtualenv

import cowsay

cowsay.dragon("saya bermain Arknights")
