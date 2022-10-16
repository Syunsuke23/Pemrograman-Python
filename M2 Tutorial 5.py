# 1. Aplikasi Terbilang

nomor = input("Masukkan angka : ")

nomor_napping = {
    "1":"Satu",
    "2":"Dua",
    "3":"Tiga",
    "4":"Empat",
    "5":"Lima",
}

output = ""

for n in nomor:
    terbilang = nomor_napping.get( n, "Invalid")

    output = output + terbilang + " "

print(output)

# 2. Emoji Converter

message = input(">>> ")

emoji_napping = {
    ":)" : "😊",
    ":D" : "😆",
    ":|" : "😐"
}

words = message.split(" ")

output = ""
for w in words:
    output = output + emoji_napping.get(w, w) + " "

print(output)

# 3. Fungsi

def halo_renal():
    print("halo renal")
    print("Selama hari senin")

print("start")
halo_renal( )
print("finish")

# 4. Parameter Fungsi

def halo_renal(nama, level):
    print(f"halo {nama} - {level}")
    print("Besok senin")

print("start")
halo_renal("Renal", 45)
print("===================")
halo_renal("Kei", 1)
print("Finish")

# 5. Keyword Argument

def halo_renal(nama, level):
    print(f"halo {nama} - {level}")
    print("Besok senin")

print("start")
halo_renal(level=45, nama="Kei")
print("finish")

# 6. Return Value

import hashlib


def kuadrat(argument):
    total = argument**2
    print("Nilai kuadrat dari ", argument, "adalah", total)
    return total

hasil = kuadrat(3)
print(hasil)
