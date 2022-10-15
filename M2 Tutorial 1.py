# 1. Program python pertama

print("Reynaldo")
print(3)
print("Kurangi")
print("Renal" *3)

# 2. Tipe Data

#int
price = 10000
print(price)

#float
diskon = 0.3
print(diskon)

price = price * diskon
print(price)

#string
nama_game = "Arknights"
print(nama_game)

jika_diskon = True
print(jika_diskon)

# 3. input data

nama = input("Siapa nama anda ?")
game = input("apa game favorit anda ?")

print(nama + ", game favorit anda adalah " + game)

# 4. Type Conservation

tahun = input("Tahun anda bermain game Arknights : ")
print(type(tahun))

tahun = int(tahun)
print (type(tahun))

umur = 2022 - tahun

print("Anda sudah bermain game arknights selama " +str(umur) + " tahun") 
