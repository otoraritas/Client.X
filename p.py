import socket
import time
import sys
import signal
import os

os.system("clear")

elapsed_times = {}

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

def check_domain_exists(url):
    try:
        socket.gethostbyname(url)
        return True
    except socket.error:
        return False

def get_ip_and_ports(url, all_ports):
    try:
        if url.startswith("http://") or url.startswith("https://"):
            print(color_text("Dilarang Menggunakan http:// atau https://", 'red'))
            return

        if not check_domain_exists(url):
            print(color_text(f"Sepertinya Domain: {url} Tidak Ada/Server Down", 'red'))
            return

        ip_address = socket.gethostbyname(url)

        def signal_handler(sig, frame):
            print(color_text("\nMenampilkan statistik:", 'green'))
            print(color_text(f"IP: {ip_address}", 'green'))
            print(color_text(f"URL: {url}",'green'))

            for port, times in elapsed_times.items():
                print(color_text(f"Port: {port}", 'green'))
                if times:
                    print(color_text(f"Ms Terbesar (Port {port}): {max(times)} ms", 'red'))
                    print(color_text(f"Ms Terkecil (Port {port}): {min(times)} ms", 'bright_yellow'))
                else:
                    print(color_text(f"Port {port} tidak terbuka", 'red'))

            sys.exit(0)

        signal.signal(signal.SIGINT, signal_handler)

        while True:
            for port in all_ports:
                start_time = time.time()
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                result = sock.connect_ex((ip_address, port))
                elapsed_time = int((time.time() - start_time) * 1000)
                port_info = color_text(f"Port {port} terbuka ({elapsed_time} ms)" if result == 0 else f"Port {port} tertutup", 'cyan')
                sock.close()

                if port not in elapsed_times:
                    elapsed_times[port] = []
                elapsed_times[port].append(elapsed_time)

                print(color_text(f"IP: {ip_address} {port_info}", "bright_yellow"))

            for i in range(0, len(all_ports)-1, 2):
                port_pair = (all_ports[i], all_ports[i+1])
                print(color_text(f"Scanning Ports: {port_pair[0]}:{port_pair[1]}...", "yellow"))
                time.sleep(1)

            time.sleep(2)

    except socket.error as e:
        return f"Gagal mendapatkan informasi: {e}"

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(color_text("Cara penggunaan: python pindai.py <URL> <Port1> <Port2>", 'cyan'))
        print(color_text("Example: python pindai.py www.dpr.go.id 80 443",'yellow'))
    else:
        url_input = sys.argv[1]

        if not check_domain_exists(url_input):
            print(color_text(f"Sepertinya Domain: {url_input} Tidak Ada/Server Down", 'red'))
        else:
            ports_input = [int(port) for port in sys.argv[2:]]
            get_ip_and_ports(url_input, ports_input)


os.system("clear")
