#1. Perulangan For

# contoh 1 
nama = "Renal"

for item in nama :
    print(item)

print("=============")    

# contoh 2
nomor = [1, 2, 3, 4, 5]

for ini in nomor :
    print(ini * 3) 

print("================")

# contoh 3

for itu in range(3):
    print (itu)    

print("================")


# contoh 4

for sana in range( 2, 12, 3): #paramter ke - 3 yaitu step atau naiknya berapa 
    print (sana)    

#2. List

# contoh 1

list_nama = ["Renal", "Kei", "Romero", "Tony", 'Syunsuke']

print(list_nama)

# contoh 2

nama = ["Renal", "Kei", "Romero", "Tony", 'Syunsuke']

print(nama[1:3])

# contoh 3

name = ["Renal", "Kei", "Romero", "Tony", 'Syunsuke']

print(name[-3])

# contoh 4

namae = ["Renal", "Kei", "Romero", "Tony", 'Syunsuke']

for ini in namae:
    print(f"Nama : {ini}")

#3. List Method

nomor = [2, 3, 1, 8, 7]
print(nomor)

nomor.append(99)
print(nomor)

nomor.insert(4, 100) 
print(nomor)

nomor.pop(2)
print(nomor)

nomor.remove(8)
print(nomor)

nomor.sort()
print(nomor)

#4. menjumlahkan List

nomor = [2, 3, 1, 7, 8]

init_number = 0

for number in nomor:
    init_number = init_number + number

print (init_number)

#5. Mencari angka Max

# contoh 1
nomor = [2, 3, 1, 7, 8]

max_nomor = max(nomor)
print(max_nomor)

# contoh 2
nomer = [2, 3, 1, 7, 8]

nomer.sort()
max_nomer = nomer[-2]

print(max_nomer)

# contoh 3
number = [2, 3, 1, 7, 8]

max_number = number[0]

for ini in number:
    if ini > max_number:
        max_number = ini

print(max_number)

#6. Tuple

nomor = (2, 3, 1, 7, 8)
print(nomor[2])

#7. Unpack

nomor = [1, 2, 3]

# x = nomor [0]
# y = nomor [1]
# z = nomor [2]

x, y, z = nomor

print(x)

#8. Dictionary

# contoh 1
renal = {
    "Nama" : "Reynaldo Romero",
    "umur": 20,
    "verifikasi" : True 
}

nama = renal["umur"]

print("")
print(nama)

# contoh 2
romero = {
    "Nama" : "Reynaldo Romero",
    "umur": 20,
    "verifikasi" : True 
}
romero["Username"] = "Kei Syunsuke"
romero["nama"] = "Kei S."

temp = romero.get("Username")

print("")
print(temp)
