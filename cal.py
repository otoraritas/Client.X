from datetime import datetime
from colorama import init, Fore
from pyfiglet import Figlet
import os
import socket

def get_user_ip():
    try:
        host_name = socket.gethostname()
        user_ip = socket.gethostbyname(host_name)
        return user_ip
    except Exception as e:
        return f"Error retrieving IP address: {e}"


user_ip = get_user_ip()

init(autoreset=True)

def hitung_umur(tahun_lahir, bulan_lahir, tanggal_lahir):
    tanggal_sekarang = datetime.now()
    tanggal_lahir = datetime(tahun_lahir, bulan_lahir, tanggal_lahir)

    selisih = tanggal_sekarang - tanggal_lahir
    tahun = selisih.days // 365
    bulan = (selisih.days % 365) // 30
    return tahun, bulan

def tampilkan_semua_bulan():
    nama_bulan = [
        'Januari', 'Februari', 'Maret', 'April',
        'Mei', 'Juni', 'Juli', 'Agustus',
        'September', 'Oktober', 'November', 'Desember'
    ]

    print(Fore.MAGENTA + "Semua Bulan:")
    for i, bulan in enumerate(nama_bulan, start=1):
        print(f"{i}. {Fore.CYAN + bulan} (Bulan ke-{i})")

def menu_tambah():
    tanggal_sekarang = datetime.now()
    print(Fore.RED + f"Tanggal sekarang: {Fore.YELLOW + tanggal_sekarang.strftime('%Y-%m-%d')}")

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        raise ValueError("Pembagian oleh nol tidak valid.")
    return a / b

def tambah(a, b):
    return a + b

def pohon_factor(n):
    if n < 0:
        raise ValueError("Masukkan bilangan bulat non-negatif.")
    elif n == 0:
        return 1
    else:
        return n * pohon_factor(n - 1)

def hitung_waktu_tujuan(jarak, kecepatan_rata_rata):
    waktu = jarak / kecepatan_rata_rata
    return waktu

fig = Figlet(font='slant')

while True:
    try:
        os.system("clear")
        print(Fore.CYAN + fig.renderText('CALCULATOR'))
        print(Fore.CYAN + "COD3D BY: DC401")
        print(Fore.GREEN + "Menu:")
        print("===========================================")
        print(f"[IP] {user_ip}")
        print("[ 1 ] Tampilkan Semua Bulan")
        print("[ 2 ] Hitung Umur")
        print("[ 3 ] Menu Tambahan")
        print("[ 4 ]i Kali")
        print("[ 5 ] Bagi")
        print("[ 6 ] Tambah")
        print("[ 7 ] Pohon Factor")
        print("[ 8 ] Hitung Waktu Tujuan")
        print("[ 0 ] Keluar")
        print("===========================================")
        pilihan = int(input(Fore.YELLOW + "Pilih Menu:: "))

        if pilihan == 1:
            tampilkan_semua_bulan()
        elif pilihan == 2:
            tahun_lahir = int(input(Fore.CYAN + "Masukkan tahun kelahiran: "))
            bulan_lahir = int(input("Masukkan bulan kelahiran: "))
            tanggal_lahir = int(input("Masukkan tanggal kelahiran: "))

            umur_tahun, umur_bulan = hitung_umur(tahun_lahir, bulan_lahir, tanggal_lahir)

            print(Fore.BLUE + f"Umur Anda sekarang adalah {umur_tahun} tahun dan {umur_bulan} bulan.\n")
        elif pilihan == 3:
            menu_tambah()
        elif pilihan == 4:
            a = float(input(Fore.CYAN + "Masukkan angka pertama: "))
            b = float(input("Masukkan angka kedua: "))
            hasil = kali(a, b)
            print(Fore.MAGENTA + f"Hasil kali: {hasil}\n")
        elif pilihan == 5:
            a = float(input(Fore.CYAN + "Masukkan angka pertama: "))
            b = float(input("Masukkan angka kedua (tidak boleh nol): "))
            hasil = bagi(a, b)
            print(Fore.MAGENTA + f"Hasil bagi: {hasil}\n")
        elif pilihan == 6:
            a = float(input(Fore.CYAN + "Masukkan angka pertama: "))
            b = float(input("Masukkan angka kedua: "))
            hasil = tambah(a, b)
            print(Fore.MAGENTA + f"Hasil tambah: {hasil}\n")
        elif pilihan == 7:
            n = int(input(Fore.CYAN + "Masukkan bilangan bulat non-negatif: "))
            hasil = pohon_factor(n)
            print(Fore.MAGENTA + f"Pohon faktorial dari {n}: {hasil}\n")
        elif pilihan == 8:
            jarak = float(input(Fore.CYAN + "Masukkan jarak tujuan (dalam km): "))
            kecepatan_rata_rata = float(input("Masukkan kecepatan rata-rata (dalam km/jam): "))
            waktu = hitung_waktu_tujuan(jarak, kecepatan_rata_rata)
            print(Fore.MAGENTA + f"Waktu yang dibutuhkan untuk mencapai tujuan: {waktu:.2f} jam\n")
        elif pilihan == 0:
            break
        else:
            print(Fore.RED + "Pilihan menu tidak valid. Pilih 1, 2, 3, 4, 5, 6, 7, 8, atau 0.\n")

        input(Fore.GREEN + "Tekan enter untuk melanjutkan....")
    except ValueError as ve:
        print(Fore.RED + f"Terjadi kesalahan: {ve}\n")
    except Exception as e:
        print(Fore.RED + f"Terjadi kesalahan: {e}\n")

