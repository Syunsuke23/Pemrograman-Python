#1. Persegi

print("Masukkan Sisi : ")
sisi = int(input())
keliling = 4 * sisi
luas = sisi * sisi
print("Hasil keliling persegi = " + str(keliling))
print("Hasil Luas Persegi = " + str(luas))

#2. Persegi Panjang

print("Masukkan Panjang : ")
panjang = int(input())
print("Masukkan Lebar : ")
lebar = int(input())
keliling = 2 * (panjang * lebar)
luas = panjang * lebar
print("Keliling Persegi panjang adalah : " + str(keliling))
print("Luas Persegi Panjang adalah : " + str(luas))

#3. Jajar Genjang

print("Masukkan Nilai a : ")
a = int(input())
print("Masukkan Nilai b : ")
b = int(input())
print("Masukkan Nilai c : ")
c = int(input())
print("Masukkan Nilai d : ")
d = int(input())
print("Masukkan Nilai t : ")
t = int(input())
keliling = a + b + c + d
luas = a * t
print("Keliling Jajar Genjang : " + str(keliling))
print("Luas Jajar Genjang : " + str(luas))

#4. Segitiga

print("Masukkan Nilai a : ")
a = int(input())
print("Masukkan Nilai b : ")
b = int(input())
print("Masukkan Nilai c : ")
c = int(input())
print("Masukkan Nilai t : ")
t = int(input())
keliling = a + b + c
luas = float(1) / 2 * a * t
print("Keliling Segitiga : " + str(keliling))
print("Luas Segitiga : " + str(luas))

#5. Belah Ketupat

print("Masukkan Nilai a : ")
a = int(input())
print("Masukkan Nilai b : ")
b = int(input())
print("Masukkan Nilai c : ")
c = int(input())
print("Masukkan Nilai d : ")
d = int(input())
print("Masukkan Nilai diagonal 1 : ")
d1 = int(input())
print("Masukkan Nilai diagonal 2 : ")
d2 = int(input())
keliling = a + b + c + d
luas = float(1) / 2 * d1 * d2
print("Keliling Belah Ketupat : " + str(keliling))
print("Luas Belah Ketupat : " + str(luas))

#6. Layang - Layang

print("Masukkan Nilai a : ")
a = int(input())
print("Masukkan Nilai b : ")
b = int(input())
print("Masukkan Nilai c : ")
c = int(input())
print("Masukkan Nilai d : ")
d = int(input())
print("Masukkan Nilai diagonal 1 : ")
d1 = int(input())
print("Masukkan Nilai diagonal 2 : ")
d2 = int(input())
keliling = a + b + c + d
luas = float(1) / 2 * d1 * d2
print("Keliling Layang - Layang : " + str(keliling))
print("Luas Layang - Layang : " + str(luas))

#7. Trapesium

print("Masukkan Nilai a : ")
a = int(input())
print("Masukkan Nilai b : ")
b = int(input())
print("Masukkan Nilai c : ")
c = int(input())
print("Masukkan Nilai d : ")
d = int(input())
print("Masukkan Nilai t : ")
t = int(input())
keliling = a + b + c + d
luas = float(a + b) / 2 * t
print("Keliling Trapesium : " + str(keliling))
print("Luas Trapesium : " + str(luas))

#8. Lingkaran

phi = 3.14
print("Masukkan Nilai r : ")
r = float(input())
keliling = 2 * phi * r
luas = phi * r * r
print("Keliling Lingkaran : " + str(keliling))
print("Luas Lingkaran : " + str(luas))
