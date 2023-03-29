#untuk perhitungan FPB
def hitung_fpb(a, b):
    while b != 0: 
        a, b = b, a % b
    return a

#untuk perhitungan KPK
def hitung_kpk(a, b): 
    if a == 0 or b == 0:
        return 0
    kpk = max(a, b)
    while True:
        if kpk % a == 0 and kpk % b == 0:
            return kpk
        kpk += 1

def show_menu(): #Menampilkan menu pilihan
    print("=== Pilih Menu Perhitungan ===")
    print("1. Menghitung FPB")
    print("2. Menghitung KPK")
    print("3. Keluar")
    pilihan = input("Pilih nomor menu : ")

    if pilihan == "1": #pilihan untuk menghitung FPB
        print(" ")
        a = int(input("Masukkan bilangan Pertama : ")) 
        b = int(input("Masukkan bilangan Kedua : ")) 
        fpb = hitung_fpb(a, b)
        print("------------------------------------------------------")
        print("FPB dari", a, "dan", b, "adalah", fpb) 
        print("------------------------------------------------------")
        print(" ")

    elif pilihan == "2": #pilihan untuk menghitung KPK
        print(" ")
        a = int(input("Masukkan bilangan Pertama : "))
        b = int(input("Masukkan bilangan Kedua : "))
        kpk = hitung_kpk(a, b)
        print("------------------------------------------------------")
        print("KPK dari", a, "dan", b, "adalah", kpk)
        print("------------------------------------------------------")
        print(" ")

    elif pilihan == "3": #Pilihan untuk keluar dari perulangan
        print("------------------------------------------------------")
        print("Terima Kasih telah menggunakan program ini")
        print("------------------------------------------------------")
        exit()
    else: 
        print("------------------------------------------------------")
        print("Input data tidak valid, mohon input nomor dengan benar")
        print("------------------------------------------------------")

#Mengecek apakah program dijalankan sebagai sebuah modul atau sebagai program utama.
#Jika program dijalankan sebagai program utama, maka fungsi show_menu() akan dipanggil secara terus menerus 
#dalam perulangan while(True) sampai pengguna memilih untuk keluar dari program.
if __name__ == '__main__':
    while(True):
        show_menu()