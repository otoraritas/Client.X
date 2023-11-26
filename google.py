from googlesearch import search
import time
from termcolor import colored
from pyfiglet import Figlet
import os
import sys
import signal
from datetime import datetime


waktu_sekarang = datetime.now()

hari =  waktu_sekarang.strftime("%A")
tanggal =  waktu_sekarang.strftime("%Y-%m-%d")
jam =  waktu_sekarang.strftime("%H")
menit =  waktu_sekarang.strftime("%M")
detik =waktu_sekarang.strftime("%S")

logo = """
░██████╗░░█████╗░░█████╗░░█████╗░░██████╗░██╗░░░░░███████╗
██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔════╝░██║░░░░░██╔════╝
██║░░██╗░██║░░██║██║░░██║██║░░██║██║░░██╗░██║░░░░░█████╗░░
██║░░╚██╗██║░░██║██║░░██║██║░░██║██║░░╚██╗██║░░░░░██╔══╝░░
╚██████╔╝╚█████╔╝╚█████╔╝╚█████╔╝╚██████╔╝███████╗███████╗
░╚═════╝░░╚════╝░░╚════╝░░╚════╝░░╚═════╝░╚══════╝╚══════╝Cod3d By: DC401
Tools Owner D.S.A
"""

def signal_handler(sig, frame):
    print(colored("\nDiterima sinyal Ctrl+C. Program berhenti.", "red"))
    sys.exit(0)

def setup_signal_handler():
    signal.signal(signal.SIGINT, signal_handler)

def print_color_banner(text, color, font='slant'):
    f = Figlet(font=font)
    banner = f.renderText(text)
    print(colored(banner, color))

def search_google(query, max_results, delay_seconds):
    print_color_banner("GOOGLE-DC401", "magenta")
    print(colored(f"SEARCHING FOR: {query}", "yellow"))
    print(colored(f"Max Results: {max_results}", "yellow"))

    if delay_seconds > 0:
        print(colored(f"Delay per URL: {delay_seconds} seconds", "yellow"))
    else:
        print(colored("No delay between URLs.", "yellow"))

    try:
        with open("result.txt", "r") as file:
            visited_urls = set(line.strip() for line in file)
    except FileNotFoundError:
        visited_urls = set()

    print(colored("Searching...", "cyan"))

    results_count = 0
    try:
        for url in search(query, num=max_results, stop=max_results, pause=delay_seconds if delay_seconds > 0 else None):
            if url not in visited_urls:
                print(colored(f"Result {results_count + 1}:", "green"), colored(url, "cyan"))
                results_count += 1
                visited_urls.add(url)
                if delay_seconds > 0:
                    time.sleep(delay_seconds)
    except KeyboardInterrupt:
        print(colored("\nDiterima sinyal Ctrl+C. Program berhenti.", "red"))
        sys.exit(0)

    print(colored("Search completed.", "green"))
    print(colored(f"Selesai: {hari}:{tanggal}:{jam}:{menit}:{detik}","yellow"))

    with open("result.txt", "a") as file:
        for url in visited_urls:
            file.write(f'{hari}:{tanggal}:{jam}:{menit}:{detik}\n')
            file.write(url + '\n')

def main():
    setup_signal_handler()
    while True:
        os.system("clear")
        print(colored(f"{logo}","magenta"))
        query = input(colored("Masukkan query Google: ","yellow"))
        max_results = int(input(colored("Masukkan jumlah maksimal hasil yang ingin Anda tampilkan: ","yellow")))
        delay_seconds = int(input(colored("Masukkan jeda waktu (detik setiap URL dilarang 0): ","yellow")))

        search_google(query, max_results, delay_seconds)

        input("Tekan Enter untuk melanjutkan...")
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
