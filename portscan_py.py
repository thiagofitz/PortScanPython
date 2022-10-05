import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)

host = input("[*] Especifique o Host para o Scan: ")

def portscanner(port):
    if sock.connect_ex((host,port)):
        print(("[-] Porta %d esta fechada" % (port), 'red'))
    else:
        print(("[+] Porta %d esta aberta" % (port), 'green'))

for port in range (1, 1000):
    portscanner(port);
