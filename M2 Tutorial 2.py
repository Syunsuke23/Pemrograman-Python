# 1. String 
nama = "Reynaldo Romero"
print(nama[-2])

nama = "Reynaldo Romero"
print(nama[2])

nama = "Reynaldo Romero"
print(nama[0:8])

nama = "Reynaldo Romero"
print(nama[9:15])

nama = "Reynaldo Romero"
print(nama[0:])

# 2. Formatted String

nama_depan = "Reynaldo"
nama_belakang = "Romero"

isi = nama_depan + "["+ nama_belakang +"]  "
isi = f"{nama_depan} [{nama_belakang}]"

print(isi)

umur = 20

pesan = f"Umur kamu {umur}"

print(pesan)

# 3. String Method

teks = "Bermain Arknights bareng Kei Syunsuke"
length = len(teks)

print(length)

course = "Bermain Arknights bareng Kei Syunsuke"
print(course.upper())
course_capital = course.upper()

print(course)
print(course_capital)

test = "Bermain Arknights bareng Kei Syunsuke"
print(test.capitalize())
print(test.title())

coba = "Bermain Arknights bareng Kei Syunsuke"
print(coba.replace("Arknights", "Genshin Impact"))

apalagi = "Bermain Arknights bareng Kei Syunsuke"
bahasa = "Arknights"

print (bahasa in apalagi)

ini = "Bermain Arknights bareng Kei Syunsuke"
language = "Genshin Impact"

print (language in ini)

# 4. Matematika

x = 20
y = 3

#tambah
print (x+y)

#kali
print (x*y)

#pangkat
print (x**y)

#kurang
print (x-y)

#bagi 
print (x/y)

#bulatkan angka desimal
print (x//y)

#persen
print (x%y)

print("===============")
a = 20
a = a + 10 #atau bisa menggunakan seperti yang dibawah ini
# a += 10
print(a)

b = 20
b = b - 10 #atau bisa menggunakan seperti yang dibawah ini
# b -= 10
print(b)

# 5. Operator Precedence
angka = (2 + 3) * 2 ** 2
print(angka)

#urutan eksekusi dalam matematika
#1. tanda kurung
#2. Perpangkatan
#3. Perkalian atau pembagian
#4. Penjumlahan dan Pengurangan

# 6. Math Module

import math

angka = 2.7
angka = round(angka)
print(angka)

number = 2.4
number = round(number)
print(number)

ini = 2.4
ini = math.ceil(ini) #dipaksa dibulatkan ke atas

print(ini)

itu = 2.9
itu = math.floor(itu) #dipksa dibulatkan ke bawah

print(itu)
