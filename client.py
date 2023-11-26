import random
import useragent
import socket
import threading
import os
import signal
import sys
import time
import platform
import psutil
import string
from pyfiglet import Figlet

text = "CLIENT.X"
fig = Figlet(font='slant')
result = fig.renderText(text)

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
██░░░░░░░░░░░██░░░░█▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
─▀███████████▒▒▒▒█▓▓▓███████████▀
────██▒▒▒▒▒▒▒▒▒▒▒▒█▓▓▓▓▓▓▓▓▓▓▓▓█
─────██▒▒▒▒▒▒▒▒▒▒▒▒██▓▓▓▓▓▓▓▓▓▓█
──────█████▒▒▒▒▒▒▒▒▒▒██████████
─────────▀███████████▀
COD3D BY: DC401
FOR: CLIENT.X
Note: TIDAK ADA WKWK
/menu = menampilkan semua menu
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

server_address = ('0.0.0.0', 5051)

try:
    client_socket.connect(server_address)
except ConnectionRefusedError:
    print(color_text("Server sedang offline, coba lagi nanti.", "red"))
    exit(1)

username = input(color_text("Masukkan username yang akan digunakan: ", "bright_cyan"))
client_socket.send(username.encode())
os.system("clear")
print(color_text(result, "bright_blue"))
print(color_text("/menu = menampilkan semua menu","brighr_blue"))

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            formatted_time = get_formatted_time()

            if message.startswith("Kirim pesan grup"):
                if group_id and f"({group_id}):" in message:
                    print(neon_text(f"\n{formatted_time} - {message[28:]}", bright=True))
                elif not group_id and "(" not in message:
                    print(neon_text(f"\n{formatted_time} - {message}", bright=True))
            else:
                print(neon_text(f"\n{formatted_time} - {message}"))

        except:
            print(neon_text("Terputus dari server.", bright=True))
            client_socket.close()
            break

def ddos():
    ip = input(color_text("Masukan IP: ","yellow"))
    port = input(color_text("Masukan Port: ","yellow"))
    packet = input(color_text("Packet/s: ","yellow"))
    th = input(color_text("Threading: ","yellow"))
    os.system(f"python3 ddos.py -s {ip} -p {port} -c {packet} -th {th}")

def pindai():
    print(color_text("Jangan pake http:// atau https:// contoh; www.dpr.go.id","blue"))
    web = input(color_text("Masukan target web:","yellow"))
    port = input(color_text("Port dipisahkan dengan spasi (contoh: 80 443): ","yellow"))
    os.system(f"python p.py {web} {port}")

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
                print(color_text(f"{logo}","blue"))
            elif message == '/ping':
                start_time = time.time()
                client_socket.send(message.encode())
                end_time = time.time()
                ping_time = round((end_time - start_time) * 1000, 2)
                print(neon_text(f"\nPing ke server: {ping_time} ms"))
            elif message == '/ddos':
                ddos()
            elif message == '/pindai':
                pindai()
            elif message == '/ram-server':
                get_ram_usage()
            elif message == '/user':
                get_connected_users()
            elif message == '/menu':
                print(color_text("/pindai = memindai suatu website \n/ddos = ddos website \n/ping = melihat kecepatan internet \n/clear = menghapus semua text dalam terminal \n/exit = keluar dari server \n/ram-server = melihat ram server \n/dump = dump database \n/google = google search \n/calculator = calculator serbaguna \n/track-ip = mencari informasi IP \n/grup = link grup D.S.A","yellow"))
            elif message == '/dump':
                target = input(color_text("Masukan domain target website: ","bright_blue"))
                os.system(f"bash das -t {target} -e doc,docx,docm,dot,dotx,dotm,ppt,pptx,pps,ppsx,ppsm,pptm,potm,pot,csv,pdf,xls,xlsx,xslsm,xlt,xltx,xltm,sql,txt,7z,zip,rar,tar,tar.gz,tar.xz ")
            elif message == '/google':
                os.system("python google.py")
            elif message == '/calculator':
                os.system("python cal.py")
            elif message == '/track-ip':
                os.system("python2 i.py")
            elif message == '/grup':
                os.system("xdg-open https://chat.whatsapp.com/EzJ10ofbCHfFg8cOyZattP")
            else:
                client_socket.send(f"Kirim pesan: {message}".encode())

def get_ram_usage():
    client_socket.send('/ram-server'.encode())

def get_connected_users():
    client_socket.send('/user'.encode())

def handle_client(client_socket):
    try:
        username = client_socket.recv(1024).decode()

        if not username or username.isspace():
            client_socket.send(color_text("\nUsername tidak valid. Silakan coba lagi.", 'red').encode())
            remove_client(client_socket)
        elif username in connected_users:
            client_socket.send(color_text("\nUsername sudah digunakan. Silakan coba lagi.", 'red').encode())
            remove_client(client_socket)
        else:
            save_username(username)
            clients[client_socket] = username
            addresses[client_socket] = client_socket.getpeername()
            connected_users.add(username)
            message = "\n{}".format(color_text("\nUser {} telah bergabung ke dalam chat!".format(username), 'yellow'))
            broadcast(message.encode(), client_socket)

            used_storage_mb += 100
            if used_storage_mb > available_storage_gb * 1024:
                print(color_text("\nPenyimpanan penuh. Server berhenti.", 'red'))
                signal_handler(signal.SIGINT, None)

            chat(client_socket, username)

    except:
        remove_client(client_socket)

def chat(client_socket, username):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                remove_client(client_socket)
                break

            message_str = message.decode()
            if message_str.startswith("Kirim pesan: "):
                formatted_message = f"\n{color_text('Pesan ' + username + ': ' + message_str[12:], 'cyan')}"
                broadcast(formatted_message.encode(), client_socket)
                log_message(formatted_message)
            else:
                client_socket.send(color_text("\n", 'red').encode())

        except Exception as e:
            print(f"\nError handling message from {username}: {str(e)}")
            remove_client(client_socket)

def save_chat_log():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_filename = f"chat_log.txt"
    with open(log_filename, 'w') as log_file:
        log_file.writelines(chat_log)

def log_message(message):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    chat_log.append(f"{timestamp} {message}\n")

def save_username(username):
    with open("usernames.txt", "a") as username_file:
        username_file.write(username + "\n")

def save_remaining_ram():
    remaining_ram = psutil.virtual_memory().available
    with open("cache.txt", "w") as cache_file:
        cache_file.write(f"Sisa RAM: {remaining_ram} bytes\n")

receive_thread = threading.Thread(target=receive_messages)
send_thread = threading.Thread(target=send_messages)

receive_thread.start()
send_thread.start()

