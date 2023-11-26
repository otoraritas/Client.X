import socket
import threading
import os
import signal
import sys
import time

def signal_handler(sig, frame):
    print(neon_text("\nClient Telah Berhenti...", bright=True))
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

os.system("clear")

logo = """
───────────▄██████████████▄
───────▄████░░░░░░░░█▀────█▄
──────██░░░░░░░░░░░█▀──────█▄
─────██░░░░░░░░░░░█▀────────█▄
────██░░░░░░░░░░░░█──────────██
───██░░░░░░░░░░░░░█──────██──██
──██░░░░░░░░░░░░░░█▄─────██──██
─████████████░░░░░░██────────██
██░░░░░░░░░░░██░░░░░█████████████
██░░░░░░░░░░░██░░░░█▓▓▓▓▓▓▓▓▓▓▓▓▓█
██░░░░░░░░░░░██░░░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
─▀███████████▒▒▒▒█▓▓▓███████████▀
────██▒▒▒▒▒▒▒▒▒▒▒▒█▓▓▓▓▓▓▓▓▓▓▓▓█
─────██▒▒▒▒▒▒▒▒▒▒▒▒██▓▓▓▓▓▓▓▓▓▓█
──────█████▒▒▒▒▒▒▒▒▒▒██████████
─────────▀███████████▀

COD3D BY: DCM.X-505
FOR: CLIENT.X
Note:
/exit Untuk keluar
/clear untuk menghapus pesan
"""

def neon_text(text, bright=False):
    color_code = '\033[1;' if bright else '\033[0;'
    neon_color = '38;5;207m'
    reset_color = '\033[0m'
    return f"{color_code}{neon_color}{text}{reset_color}"

def color_text(text, color):
    colors = {
        'black': '\033[0;30m',
        'red': '\033[0;31m',
        'green': '\033[0;32m',
        'yellow': '\033[0;33m',
        'blue': '\033[0;34m',
        'magenta': '\033[0;35m',
        'cyan': '\033[0;36m',
        'white': '\033[0;37m',
        'bright_black': '\033[1;30m',
        'bright_red': '\033[1;31m',
        'bright_green': '\033[1;32m',
        'bright_yellow': '\033[1;33m',
        'bright_blue': '\033[1;34m',
        'bright_magenta': '\033[1;35m',
        'bright_cyan': '\033[1;36m',
        'bright_white': '\033[1;37m',
        'reset': '\033[0m'
    }

    if color in colors:
        return f"{colors[color]}{text}{colors['reset']}"
    else:
        return text

def get_formatted_time():
    current_time = time.localtime()
    formatted_time = time.strftime("%H %M %S", current_time)
    return formatted_time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('0.0.0.0', 5050)

try:
    client_socket.connect(server_address)
except ConnectionRefusedError:
    print(color_text("Server sedang offline, coba lagi nanti.", "red"))
    exit(1)

username = input(color_text("Masukkan username yang akan digunakan: ", "bright_cyan"))
client_socket.send(username.encode())
os.system("clear")
print(color_text(logo, "bright_blue"))

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            formatted_time = get_formatted_time()
            print(neon_text(f"\n{formatted_time} - {message}"))
        except:
            print(neon_text("Terputus dari server.", bright=True))
            client_socket.close()
            break

def send_messages():
    while True:
        message = input(neon_text("Kirim pesan: "))
        if message.strip():
            if message == '/exit':
                client_socket.send(message.encode())
                os.kill(os.getpid(), signal.SIGINT)
                break
            elif message == '/clear':
                os.system("clear")
                print(color_text("/exit Untuk Keluar \n/clear Untuk Clear Terminal", "blue"))
            elif message == '/ping':
                start_time = time.time()
                client_socket.send(message.encode())
                end_time = time.time()
                ping_time = round((end_time - start_time) * 1000, 2)
                print(neon_text(f"\nPing ke server: {ping_time} ms"))
            else:
                client_socket.send(f"Kirim pesan: {message}".encode())

receive_thread = threading.Thread(target=receive_messages)
send_thread = threading.Thread(target=send_messages)

receive_thread.start()
send_thread.start()
