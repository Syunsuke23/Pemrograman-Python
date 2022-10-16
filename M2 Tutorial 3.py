# 1. percabangan IF

# contoh 1 :
arknights = True

if arknights :
    print ("anda bermain arknights")

else :
    print ("Anda tidak bermain Arknights")

print ("Semoga harimu menyenangkan")
print("=================================")

#contoh 2 :

Gesnhin = False

if Gesnhin :
    print ("anda bermain Genshin")

else :
    print ("Anda tidak bermain Genshin")

print ("Marilah Login")
print("=======================================")

#contoh 3 :

Gesnhin = False
Honkai = True

if Gesnhin :
    print ("anda bermain Genshin")

elif Honkai :
    print ("anda bermain Honkai")

else :
    print ("anda memainkan game lainnya")

print ("Semoga anda menikmati permainannya")

# 2. Operator Perbandingan

sama = 1 == 1
print (sama)
kurang = 1<= 2
print (kurang)
lebih = 1 >= 2
print (lebih)
tidak = 1!= 1
print (tidak)

print("================")

grade = 7

if grade >=8:
    print ("Nilai anda adalah A")

elif grade >=7:
    print ("Nilai anda adalah B")

elif grade >=6:
    print ("Nilai anda adalah C") 

else :
    print ("Belajar sana, masih ada tugas lainnya") 

# 3. Operator Logika

 # contoh 1
nama = "Reynaldo Romero"

if len(nama) >3:
    print ("Youkoso Soul Society")

else :
    print ("nama anda terlalu pendek")

# contoh 2
name = "Reynaldo Romero"

if len(name) <3 :
    print ("Youkoso Soul Society")

else :
    print ("nama anda terlalu pendek")

# contoh 3
namae = "Syunsuke"
validasi = False

if len(namae) <3 and validasi :
    print ("Youkoso Soul Society")

else :
    print ("nama anda kepanjangan")

    #note
    #False or True = True
    #True or False = True
    #True and False = False
    #False and True = False
    #True and True = True

# 4. Perulangan While

# contoh 1
jojo = 1

while jojo <= 7:
    print("ORA!!")
    jojo = jojo + 1
 
print("ORA!!!")
print("===============")

# contoh 2
angka = 1

while angka <= 7:
    print("*" * angka)
    angka = angka + 1
 
print("Itu sih")

# 5. Game tebak angka

coba = 0
nomor_benar = 3
batas = 4

while coba < batas:
    tebak_angka = input("Masukkan angka (1-6) : ")
    tebak_angka = int(tebak_angka)

    if tebak_angka == nomor_benar:
        print("iya dha, betul itu")
        break

    coba = coba + 1 

# 6. Aplikasi kalkulator

command = ""

while command != "keluar":
    command = input("Masukkan Perintah (+,-,*,/, keluar) : ")

    if command == "keluar":
        break

    if command != "+" and command != "-" and command != "*" and command != "/":
        print("perintah tidak dikenali, coba lagi")
        continue

    a = int (input("Masukkan angka pertama : "))
    b = int (input("Masukkan angka kedua : "))

    if command == "+":
       result = a + b

    elif command == "-":
       result = a-b

    elif command == "*":
       result = a*b
 
    elif command == "/":
       result = a/b

    print(f"Hasil : {result}")

print("Terima kasih, semoga harimu hari senin")  
