import os
import sys
import time
import threading
import requests
import webbrowser
import base64
import subprocess
import platform
from colorama import Fore, init

init(autoreset=True)
os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def spinner(done_flag):
    symbols = ['|', '/', '-', '\\']
    idx = 0
    while not done_flag[0]:
        print(f'\r{Fore.CYAN}{symbols[idx % len(symbols)]} Loading...', end='')
        idx += 1
        time.sleep(0.1)
    print('\r', end='')

def progress_bar(done_flag, duration=5):
    width = 40
    sys.stdout.write("[" + " " * width + "]")
    sys.stdout.flush()
    sys.stdout.write("\b" * (width + 1))
    for _ in range(width):
        if done_flag[0]:
            break
        time.sleep(duration / width)
        sys.stdout.write("-")
        sys.stdout.flush()
    sys.stdout.write("]\n")

def decrypt_key(encoded_key):
    return base64.b64decode(encoded_key.encode()).decode()

PHONE_API_KEY_ENC = "MDZiNmYyZDM1OTY3MjM5MjkyMTI1ZjJjYzlhNzZkMzU="
EMAIL_API_KEY_ENC = "YWIxNTNkY2Q0OWI1NTExYjVkYWI3YjE2YzdjMmE4YzA="
DNS_API_KEY = "fd2C3hFP53JrglsQFalzLg==p2qiqWdqaUVCNLno"

phone_api_key = decrypt_key(PHONE_API_KEY_ENC)
email_api_key = decrypt_key(EMAIL_API_KEY_ENC)

def ping_ip(ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '10000', ip]
    try:
        typewriter(f"\nPinging {ip}...\n")
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        for line in iter(process.stdout.readline, ''):
            if line.strip():
                print(f"{Fore.GREEN}Pinged IP = {ip} | {line.strip()}")
            time.sleep(0.1)
        process.stdout.close()
        process.wait()
        if process.returncode != 0:
            typewriter(f"{Fore.RED}Ping command failed with return code {process.returncode}")
    except Exception as e:
        typewriter(f"{Fore.RED}An error occurred: {e}")

def print_menu(menu_num):
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = f'''
{Fore.CYAN}  ,ad88PPP88ba,      ad888888b,                  ad88888ba                                        88  
{Fore.CYAN} d8"  .ama.a "8a  d8"     "88             d8"     "88     ,d                              88  
{Fore.BLUE}d8'  ,8P"88"  88          a8P               8P       88       88                              88  
{Fore.BLUE}88  .8P  8P   88       ,d8P"   8b,dPPYba,   Y8,    ,d88     MM88MMM  ,adPPYba,    ,adPPYba,   88  
{Fore.CYAN}88  88   8'   8P     a8P"     88P'   `"8a "PPPPPP"88      88    a8"     "8a a8"     "8a  88  
{Fore.CYAN}88  8B ,d8 ,ad8'   a8P'        88       88           8P       88    8b       d8  8b       d8  88  
{Fore.BLUE}"8a "88P"888P" d8"        88       88  8b,    a8P        88,   "8a,   ,a8""8a,   ,a8"  88  
{Fore.BLUE} `Y8aaaaaaaad8P   88888888888  88       88  `"Y8888P'         "Y888  `"YbbdP"' `"YbbdP"'   88  
{Fore.CYAN}                                                                                            
{Fore.BLUE} Made By Hanako
'''
    print(banner)

    if menu_num == 1:
        menu_content = f'''
{Fore.CYAN} [0] Exit
{Fore.CYAN} [1] Enter Name Info    
{Fore.BLUE} [2] Enter Phone Number
{Fore.BLUE} [3] Enter Address Info  
{Fore.CYAN} [4] Enter IP Info
'''
    elif menu_num == 2:
        menu_content = f'''
{Fore.CYAN} [5] Enter Email Info
{Fore.CYAN} [6] DNS Lookup
{Fore.BLUE} [7] Ping IP
{Fore.BLUE} [8] See website code
{Fore.CYAN} [9] Join The Discord
'''
    elif menu_num == 3:
        menu_content = f'''
{Fore.CYAN} [10] Unknown
{Fore.CYAN} [11] Unknown
{Fore.BLUE} [12] Unknown
{Fore.BLUE} [13] Unknown
{Fore.CYAN} [14] Unknown
'''
    print(menu_content)

current_menu = 1

while True:
    print_menu(current_menu)
    menu = input(Fore.CYAN + "Select an option or type 'next or back': ").strip().lower()

    if menu == "next":
        current_menu = min(current_menu + 1, 3)
        continue

    if menu == "back":
        current_menu = max(current_menu - 1, 1)
        continue

    if menu == "0":
        break

    if current_menu == 1:
        if menu == "1":
            url = "https://www.beenverified.com"
            print(f"\nOpening: {url}")
            webbrowser.open(url)

        elif menu == "2":
            phone = input("Enter phone number (with country code): ").strip()
            url = f"https://apilayer.net/api/validate?access_key={phone_api_key}&number={phone}"
            done_flag = [False]
            t_spinner = threading.Thread(target=spinner, args=(done_flag,))
            t_progress = threading.Thread(target=progress_bar, args=(done_flag, 5))
            t_spinner.start()
            t_progress.start()
            try:
                response = requests.get(url)
                done_flag[0] = True
                t_spinner.join()
                t_progress.join()
                data = response.json()
                if data.get("valid"):
                    output = (
                        f"\n--- Phone Info ---\n"
                        f"Country: {data.get('country_name')}\n"
                        f"Location: {data.get('location')}\n"
                        f"Carrier: {data.get('carrier')}\n"
                        f"Line Type: {data.get('line_type')}\n"
                    )
                    typewriter(output)
                else:
                    typewriter(f"{Fore.YELLOW}[!] Invalid phone number.")
            except Exception as e:
                done_flag[0] = True
                typewriter(f"{Fore.RED}Error retrieving phone info: {e}")

        elif menu == "3":
            # --- Global Address API Integration ---
            street = input("Enter street line (e.g., Gießener Str. 30): ").strip()
            city = input("Enter city: ").strip()
            country = input("Enter country code (e.g., DEU): ").strip()
            postal = input("Enter postal code: ").strip()

            url = "https://global-address.p.rapidapi.com/V3/WEB/GlobalAddress/doGlobalAddress"

            querystring = {
                "format": "json",
                "ctry": country,
                "a1": street,
                "a2": city,
                "postal": postal,
                "DeliveryLines": "Off"
            }

            headers = {
                "x-rapidapi-key": "8caa5b6988msh96637e37a7d9659p1d4024jsna618c6d0e04c",
                "x-rapidapi-host": "global-address.p.rapidapi.com"
            }

            done_flag = [False]
            t_spinner = threading.Thread(target=spinner, args=(done_flag,))
            t_progress = threading.Thread(target=progress_bar, args=(done_flag, 5))
            t_spinner.start()
            t_progress.start()

            try:
                response = requests.get(url, headers=headers, params=querystring)
                done_flag[0] = True
                t_spinner.join()
                t_progress.join()
                data = response.json()

                output = "\n--- Address Lookup Info ---\n"
                for item in data.get("Addresses", []):
                    for key, value in item.items():
                        output += f"{key}: {value}\n"
                    output += "-"*30 + "\n"

                typewriter(output)

            except Exception as e:
                done_flag[0] = True
                typewriter(f"{Fore.RED}Error retrieving address info: {e}")

        elif menu == "4":
            ip = input("Enter IP address (or leave blank for your IP): ").strip()
            url = f"https://ipinfo.io/{ip}/json" if ip else "https://ipinfo.io/json"
            done_flag = [False]
            t_spinner = threading.Thread(target=spinner, args=(done_flag,))
            t_progress = threading.Thread(target=progress_bar, args=(done_flag, 5))
            t_spinner.start()
            t_progress.start()
            try:
                response = requests.get(url)
                done_flag[0] = True
                t_spinner.join()
                t_progress.join()
                data = response.json()
                output = "\n--- IP Info ---\n"
                for key, value in data.items():
                    output += f"{key.title()}: {value}\n"
                typewriter(output)
            except Exception as e:
                done_flag[0] = True
                typewriter(f"{Fore.RED}Error retrieving IP info: {e}")

        else:
            typewriter(f"{Fore.RED}[!] Invalid selection.")

    else:  # menu 2 options 5-9
        if menu == "5":
            email = input("Enter email address: ").strip()
            url = f"https://apilayer.net/api/check?access_key={email_api_key}&email={email}&smtp=1&format=1"
            done_flag = [False]
            t_spinner = threading.Thread(target=spinner, args=(done_flag,))
            t_progress = threading.Thread(target=progress_bar, args=(done_flag, 5))
            t_spinner.start()
            t_progress.start()
            try:
                response = requests.get(url)
                done_flag[0] = True
                t_spinner.join()
                t_progress.join()
                data = response.json()
                output = (
                    f"\n--- Email Info ---\n"
                    f"Format Valid: {data.get('format_valid')}\n"
                    f"MX Found: {data.get('mx_found')}\n"
                    f"SMTP Check: {data.get('smtp_check')}\n"
                    f"Disposable: {data.get('disposable')}\n"
                    f"Domain: {data.get('domain')}\n"
                    f"Free Email: {data.get('free')}\n"
                    f"Score: {data.get('score')} (0 to 1, higher = more deliverable)\n"
                )
                if not data.get("format_valid"):
                    output += f"{Fore.YELLOW}[!] Invalid email format.\n"
                typewriter(output)
            except Exception as e:
                done_flag[0] = True
                typewriter(f"{Fore.RED}Error validating email: {e}")

        elif menu == "6":
            domain = input("Enter domain (e.g. example.com): ").strip()
            api_url = f'https://api.api-ninjas.com/v1/dnslookup?domain={domain}'
            headers = {'X-Api-Key': DNS_API_KEY}
            done_flag = [False]
            t_spinner = threading.Thread(target=spinner, args=(done_flag,))
            t_progress = threading.Thread(target=progress_bar, args=(done_flag, 5))
            t_spinner.start()
            t_progress.start()
            try:
                response = requests.get(api_url, headers=headers)
                done_flag[0] = True
                t_spinner.join()
                t_progress.join()
                if response.status_code == 200:
                    typewriter(f"\n--- DNS Records for {domain} ---\n{response.text}")
                else:
                    typewriter(f"{Fore.RED}Error {response.status_code}: {response.text}")
            except Exception as e:
                done_flag[0] = True
                typewriter(f"{Fore.RED}Exception during DNS lookup: {e}")

        elif menu == "7":
            ip = input("Enter IP address to ping: ").strip()
            if ip:
                ping_ip(ip)
            else:
                typewriter(f"{Fore.YELLOW}[!] No IP entered.")

        elif menu == "8":
            url = "https://www.view-page-source.com/"
            print(f"\nOpening: {url}")
            webbrowser.open(url)

        elif menu == "9":
            url = "https://discord.gg/tjdgK3pF"
            print(f"\nOpening: {url}")
            webbrowser.open(url)

        else:
            typewriter(f"{Fore.RED}[!] Invalid selection.")

    input(f"\n{Fore.CYAN}Press Enter to return to menu...")
