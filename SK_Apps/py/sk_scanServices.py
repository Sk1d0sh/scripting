import socket
import sys

def banner(ip, puerto):
    s= socket.socket()
    s.connect((ip,puerto))
    print(str(s.recv(1024)))

def main():
    ip = '10.10.95.199'#input("Ingresa la ip: ") #192.168.0.2
    port= 80#int(input("Ingresa el puerto: ")) #22
    banner(ip,port)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt():
        sys.exit()

