
import pyfiglet
import socket
from termcolor import colored

def scan(target, ports):
    print(colored('\n' + 'Starting scan for ' + str(target), "yellow"))
    for port in range(1,ports):
        scan_port(target, port)

def scan_port(ip_address, port):
   
    try:
        sock  = socket.socket()
        sock.connect((ip_address, port))
        print(colored("[+] Port Opened " + str(port), "green"))
        sock.close()
    except: 
        pass

def parse_input():
    if ',' in targets:
        print(colored("[*] Scanning multiple targets", "green"))
        for ip_addr in targets.split(','):
            scan(ip_addr.strip(' '),ports)
    else:
        print(colored("[*] Scanning target", "green"))
        scan(targets, ports)


#print("\n" + colored(pyfiglet.figlet_format("SQUID SCAN", font="computer", width=120), 'magenta'))
#print("\n" + colored(pyfiglet.figlet_format("SQUID SCAN", font="isometric1", width=120), 'magenta'))
#print("\n" + colored(pyfiglet.figlet_format("SQUID SCAN", font="poison", width=120), 'magenta'))
print("\n" + colored(pyfiglet.figlet_format("SQUID SCAN", font="cricket", width=120), 'magenta'))
targets = input("[*] Enter IP address(es) to scan (split multiple ip addresses with a comma): ")
ports = int(input("[*] Enter how many ports you want to scan: "))
parse_input()



