4.9 Input Data Mahasiswa

#Kodingan

a="Universitas Teknologi Sumbawa"

new_a = a.rjust(25)

new_a = new_a.center(50)

print(f"{new_a}")

b="Jln. Olat Maras"

new_b = b.rjust(10)

new_b = new_b.center(50)

print(f"{new_b}")

print("_"*50)

nama = str(input("\n\tNama \t\t: "))

nim = int(input("\tNIM \t\t: "))

prodi = str(input("\tProdi \t\t: "))

fakultas = str(input("\tFakultas \t: "))

print("_"*50)

#output

<img width="312" alt="M2 B1 4 9" src="https://user-images.githubusercontent.com/105592890/197342389-8c9ae418-caac-4b23-bd6d-0c9a350d4eba.png">


4.10.1 Data Kecepatan Mobil

#Kodingan

a="DATA KECEPATAN MOBIL"

new_a = a.rjust(20)

new_a = new_a.center(70)

print(f"{new_a}")

print("_"*70)

kecepatan = int(input("\n\tMasukkan kecepatan rata - rata (km/jam) \t: "))

waktu = int(input("\tMasukkan waktu yang ditempuh (jam) \t\t: "))

jarak_tempuh = kecepatan*waktu

#output

<img width="411" alt="M2 B1 4 10 1" src="https://user-images.githubusercontent.com/105592890/197342420-57264602-056b-4015-a3f6-85ad6ffaeefd.png">

4.10.2 Program Menghitung Pembelian

#Kodingan

a="PROGRAM MENGHUITUNG PEMBELIAN"

new_a = a.rjust(20)

new_a = new_a.center(70)

print(f"{new_a}")

print("_"*70)

hsatuan = int(input("\n\tharga satuan \t\t: Rp."))

jumlah = int(input("\tJumlah Pembelian \t: "))

diskon = int(input("\tDiskon \t\t\t: "))


htotal = (hsatuan*jumlah)

diskon = hsatuan*diskon/100

hasil = htotal-diskon

print ("\tHarga Total \t\t: Rp." + str(hasil))

print("_"*70)

#output



4.10.5 Program Gaji Pegawai

#Kodingan 

import os


judul = "PROGRAM GAJI PEGAWAI"

garis = "-"*100

nama_karyawan = str(input("Masukkan Nama Karyawan\t\t: "))

jumlah_anak = int(input("Masukkan Jumlah Anak\t\t: "))

gaji_pokok = float(input("Masukkan Jumlah Gaji Pokok\t: "))


t_kesejahteraan = gaji_pokok * (20/100)

t_keluarga = gaji_pokok * (20/100)

t_keluarga_perjumlah_anak = jumlah_anak * gaji_pokok * (10/100)

pajak = gaji_pokok * (10/100)

gaji_kotor = (gaji_pokok + t_keluarga + t_keluarga_perjumlah_anak) + pajak

gaji_bersih = gaji_kotor - pajak

judul = judul.center(80)


os.system ('cls')

print(judul)

print(f"\tNama Karyawan\t : {nama_karyawan}")

print(f"\tJumlah Anak\t: {jumlah_anak}")

print(garis)

print(f"\tGaji Pokok\t\t T. Kesejahteraan\t\t T. Keluarga\t\t Pajak\t\t")

print(f"\t{gaji_pokok}\t\t {t_kesejahteraan}\t\t\t {t_keluarga_perjumlah_anak}\t\t {pajak}")

print(garis)


print(f"Gaji Kotor\t: {gaji_kotor}")

print(f"Gaji Kotor\t: {gaji_bersih}")



print ("\tJarak Tempuh\t\t\t\t\t: " + str(jarak_tempuh))

print("_"*70)

#Output

<img width="579" alt="M2 B1 4 10 5" src="https://user-images.githubusercontent.com/105592890/197342625-b516ca78-1a45-4390-84e5-98078a2e7a41.png">
