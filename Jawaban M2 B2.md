5.7.4 Program Menghitung Berat badan ideal

#kodingan

nama = str(input("\n\tNama Anda \t\t: "))

tinggi = int(input("\tTinggi \t\t\t: "))


berat_ideal = tinggi - 100


print("Saudara " + str(nama) + ", berat ideal anda adalah " + str(berat_ideal) + " kg")

#output

<img width="380" alt="M2 B2 5 7 4" src="https://user-images.githubusercontent.com/105592890/197345851-10cfbff2-f69f-409f-8079-ddc0ceda3d7c.png">


5.7.5 Menghitung Nilai Akhir

#Kodingan

from re import A


a="DATA NILAI MAHASISWA"

new_a = a.rjust(20)

new_a = new_a.center(70)

print(f"{new_a}")


garis = "_"*70

print(garis)


nama = str(input("\n\tNama \t\t: "))

tugas = int(input("\tTugas \t\t: "))\

uts = int(input("\tUTS \t\t: "))

uas = int(input("\tUAS \t\t: "))

print(garis)


na = (25/100) * tugas + (35/100) * uts + (40/100) * uas


if na >= 75:

  grade = 'A'


elif 60 <= na < 75:

    grade = 'B'


elif 45 <= na < 60:

    grade = 'C'


elif na < 45 :

    grade = 'D'



print ("\n\n \t\t\tNILAI AKHIR DAN GRADE")

print(garis)

print(f"\n\tNama\t\t: {nama}")

print(f"\tNilai Akhir\t: {na}")

print(f"\tGrade\t\t: {grade}")

print(garis)


#output

<img width="400" alt="M2 B2 5 7 5" src="https://user-images.githubusercontent.com/105592890/197345880-d3f9c77e-39ec-42af-a03f-92f8b66f796a.png">
