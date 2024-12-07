#!/usr/bin/python3
import socket, sys
import time, queue
from colorama import Fore, init
import threading,requests
import argparse
init()
#  Defining color

red = Fore.RED
green = Fore.GREEN
reset = Fore.RESET

# help module

argparse = argparse.ArgumentParser(description="this is a basic port scanner tool like nmap ",
                                   usage="python3 port_scanner.py -d DOMAIN/IP -s START_PORT -e END_PORT -t THREADS")

argparse.add_argument("-d", "--domain", help="Enter the domain/ip  (ex: -d example.com)", required=True)
argparse.add_argument("-s", "--start_port", help="Enter start port number", required=True)
argparse.add_argument("-e", "--end_port", help="Enter end port number", required=True)
argparse.add_argument("-t", "--threads", help="Enter thread number", required=True)
argparse.add_argument("-o", "--outfile", help="Enter the file name to write output")

args = argparse.parse_args()
outfile = args.outfile
usage = f"{green} python3 port_scanner.py TARGET START_PORT END_PORT THREADS  {reset} "

# banner
print(f"{red}*{reset}" * 75)
ascii_banner = ''' {}
 _____                                                                        _____ 
( ___ )                                                                      ( ___ )
 |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
 |   |  ____   ___  ____ _____   ____   ____    _    _   _ _   _ _____ ____   |   | 
 |   | |  _ \\ / _ \\|  _ \\_   _| / ___| / ___|  / \\  | \\ | | \\ | | ____|  _ \\  |   | 
 |   | | |_) | | | | |_) || |   \\___ \\| |     / _ \\ |  \\| |  \\| |  _| | |_) | |   | 
 |   | |  __/| |_| |  _ < | |    ___) | |___ / ___ \\| |\\  | |\\  | |___|  _ <  |   | 
 |   | |_|    \\__/|_| \\_\\|_|   |____/ \\____/_/   \\_\\_| \\_|_| \\|_____|_| \\_\\ |   | 
 |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
(_____)                                                                      (_____)

------------------------------------------------------------------------------------
                                                        Crafted by sidharth
                                                        Twitter: kidnapshadow_kd
------------------------------------------------------------------------------------
'''.format(green)
print(ascii_banner)
print(f"{red}*{reset}" * 75)

target = args.domain
try:
    target = socket.gethostbyname(target)
except:
    print("[-] Host Resolution Failed")
start_port = int(args.start_port)
end_port = int(args.end_port)
thread_no = int(args.threads)

result = f"{red} [+] Result: \nPORT \t STATE \t SERVICE \n {reset}"

print("IP for scanning : {} ".format(target))
if not target or not str(start_port) or not end_port or not thread_no:
    print(usage)
    exit()

q = queue.Queue()

def get_banner(port, s):
    if(port == 80):
        response = requests.get("http://" + target)
        return response.headers['server']
    try:
        return s.recv(1024).decode()
    except:
        return 'Not Found'

def scan_port(t_no):
    global result
    while not q.empty():
        port = q.get()
        print("scanning for port {} ".format(port))
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            conn = s.connect_ex((target, port))
            if not conn:
                banner = get_banner(port, s)
                banner = ''.join(banner.splitlines())
                result += f" {green}{port} \t OPEN \t {banner} {reset}\n"
        except:
            pass
        s.close()
        q.task_done()


start_time = time.time()

for j in range(start_port, end_port + 1):
    q.put(j)

for i in range(thread_no):
    t = threading.Thread(target=scan_port, args=(i,))
    t.start()

q.join()

end_time = time.time()
print(result)
print("Time taken : {}".format(end_time - start_time))

if(outfile):
    with open(outfile,'w') as file:
        file.write(f"Port Scanning Result for target:  {target}\n")
        file.write(result)

