while True:    #This simulates a Do Loop
    print("Masukkan Operasi : ")
    kode = input()
    if kode == "+":
        print("Masukkan angka pertama : ")
        x = int(input())
        print("Masukkan angka kedua : ")
        y = int(input())
        tambah = x + y
        print("Hasil : " + str(tambah))
    else:
        if kode == "-":
            print("Masukkan angka pertama : ")
            x = int(input())
            print("Masukkan angka kedua : ")
            y = int(input())
            kurang = x - y
            print("Hasil : " + str(kurang))
        else:
            if kode == "x":
                print("Masukkan angka pertama : ")
                x = int(input())
                print("Masukkan angka kedua : ")
                y = int(input())
                kali = x * y
                print("Hasil : " + str(kali))
            else:
                if kode == "/":
                    print("Masukkan angka pertama : ")
                    x = int(input())
                    print("Masukkan angka kedua : ")
                    y = int(input())
                    bagi = float(x) / y
                    print("Hasil : " + str(bagi))
                else:
                    print("Perintah tidak dikenali")
    print("Coba lagi ? (Y/N)")
    var_try = input()
    if not(var_try == "Y"): break   #Exit loop
print("Terima kasih telah menggunakan Aplikasi kami")
