#1. Exception

try:
    level = input("Level Genhin kamu : ")
    level = int(level)
    print(level)
except ValueError:
    print("Yang anda masukkan itu bukan angka")


#2. General Exception

try:
    level = input("Level Genhin kamu : ")
    level = int(level)
    level = level / 0
    print(level)
except:
  print("terjadi kesalahan")

#3. Membaca file

#contoh 1 :
#users = open("test.txt")

#print(users.read())

#users.close()

# contoh 2 :
#users = open("test.txt")

#array = users.readlines()

#for user in array:
#    print(user)

#users.close()

# contoh 3
users = open("test.txt")

array = users.readlines()

index = 1
for user in array:
    print(f"{index} - {user}")
    index += 1

users.close()

#4. Menulis File

# (a = append ) apabila ingin menambahkan tulisan pada teks

users = open("test.txt", "a")

users.write("\n ini-itu")

users.close()
 
#apabila ingin menghapus semua data pada teks

# users = open("test.txt", "w")

# users.write("\n ini-itu")

# users.close()

#apabila ingin membuat teks baru

#users = open("users_baru.txt", "w")

#users.write("Ini -itu")

#users.close()

#isi teks.txt

Reynaldo Romero - reynaldoromero - admin
Kei Syunsuke - syunsuke - moderator
Tony Romero - Tony - Userini-itu
