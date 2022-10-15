#1. Kubus

print("Masukkan Nilai R : ")
r = int(input())
luas = 6 * r * r
volume = r * r * r
print("Luas Kubus : " + str(luas))
print("Volume Kubus : " + str(volume))

#2. Balok

print("Masukkan Nilai p : ")
p = int(input())
print("Masukkan Nilai l : ")
l = int(input())
print("Masukkan Nilai t : ")
t = int(input())
luas = 2 * p * l + 2 * p * t + 2 * l * t
volume = p * l * t
print("Luas balok : " + str(luas))
print("Volume balok : " + str(volume))

#3. Limas Segi Empat

print("Masukkan sisi : ")
sisi = int(input())
print("Masukkan nilai a : ")
a = int(input())
print("Masukkan nilai t : ")
t = int(input())
luas = sisi * sisi + 4 * (float(1) / 2 * a * t)
volume = float(1) / 3 * (sisi * sisi) * t
print("Luas limas segi empat : " + str(luas))
print("Volume limas segi empat : " + str(volume))

#4. Prisma Segitiga

print("Masukkan nilai a : ")
a = float(input())
print("Masukkan nilai b : ")
b = float(input())
print("Masukkan nilai c : ")
c = float(input())
print("Masukkan nilai t : ")
t = float(input())
print("Masukkan Tinggi Prisma : ")
tprisma = float(input())
ls = 2 * (a + b + c) * tprisma
lp = 3 * (a + b + c) * tprisma + a * t
volume = float(1) / 2 * a * t * t
print("Hasil Ls Prisma Segitiga : " + str(ls))
print("Hasil Lp Prisma Segitiga : " + str(lp))
print("Hasil Volume Prisma Segitiga : " + str(volume))

#5. Limas Segitiga

print("Masukkan nilai a : ")
a = float(input())
print("Masukkan nilai b : ")
b = float(input())
print("Masukkan nilai c : ")
c = float(input())
print("Masukkan nilai t : ")
t = float(input())
print("Masukkan nilai Tlimas : ")
tlimas = float(input())
luas = 4 * (a + b + c)
volume = float(1) / 6 * a * t * tlimas
print("Hasil Luas Limas Segitiga : " + str(luas))
print("Hasil Volume Limas Segitiga : " + str(volume))

#6. Tabung

phi = 3.14
print("Masukkan nilai r : ")
r = int(input())
print("Masukkan nilai T : ")
t = int(input())
ls = 2 * phi * r * t
lp = 2 * phi * r * t + 2 * phi * r * r
volume = phi * r * r * t
print("Hasil luas selimut Tabung : " + str(ls))
print("Hasil Luas Permukaan Tabung : " + str(lp))
print("Hasil volume tabung : " + str(volume))

#7. Kerucut

phi = 3.14
print("Masukkan nilai r : ")
r = float(input())
print("Masukkan nilai s : ")
s = float(input())
print("Masukkan nilai T : ")
t = float(input())
ls = phi * r * s
lp = phi * r * s + phi * r * r
volume = float(1) / 3 * phi * r * r * t
print("Hasil Luas Selimut kerucut : " + str(ls))
print("Hasil Luas Permukaan Kerucut : " + str(lp))
print("Hasil Volume Kerucut : " + str(volume))

#8. Bola

phi = 3.14
print("Masukkan Nilai r : ")
r = float(input())
luas = 4 * phi * r * r
volume = float(4) / 3 * phi * r * r * r
print("Hasil Luas Bola  : " + str(luas))
print("Hasil Volume Bola : " + str(volume))
