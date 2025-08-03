import os
import sys
import time
import threading
import requests
import webbrowser
import base64
from colorama import Fore, init

init(autoreset=True)
os.system('cls' if os.name == 'nt' else 'clear')

# Typewriter effect function
def typewriter(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Spinner function
def spinner(done_flag):
    symbols = ['|', '/', '-', '\\']
    idx = 0
    while not done_flag[0]:
        print(f'\r{Fore.CYAN}{symbols[idx % len(symbols)]} Loading...', end='')
        idx += 1
        time.sleep(0.1)
    print('\r', end='')  # Clear line when done

# Progress bar function
def progress_bar(done_flag, duration=5):
    toolbar_width = 40
    sys.stdout.write("[{}]".format(" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width + 1))

    increments = toolbar_width
    sleep_time = duration / increments

    for _ in range(increments):
        if done_flag[0]:
            break
        time.sleep(sleep_time)
        sys.stdout.write("-")
        sys.stdout.flush()

    sys.stdout.write("]\n")

# Base64 key decoder
def decrypt_key(encoded_key):
    return base64.b64decode(encoded_key.encode()).decode()

# Your encoded API keys here
PHONE_API_KEY_ENC = "MDZiNmYyZDM1OTY3MjM5MjkyMTI1ZjJjYzlhNzZkMzU="
EMAIL_API_KEY_ENC = "YWIxNTNkY2Q0OWI1NTExYjVkYWI3YjE2YzdjMmE4YzA="

phone_api_key = decrypt_key(PHONE_API_KEY_ENC)
email_api_key = decrypt_key(EMAIL_API_KEY_ENC)

# Display menu
content = f'''
{Fore.MAGENTA}
ooooo   ooooo               .   oooo   o8o                               .oooooo.             o8o                  .   
`888'   `888'             .o8   `888   `"'                              d8P'  `Y8b            `"'                .o8   
 888     888   .ooooo.  .o888oo  888  oooo  ooo. .oo.    .ooooo.       888      888  .oooo.o oooo  ooo. .oo.   .o888oo 
 888ooooo888  d88' `88b   888    888  `888  `888P"Y88b  d88' `88b      888      888 d88(  "8 `888  `888P"Y88b    888   
 888     888  888   888   888    888   888   888   888  888ooo888      888      888 `"Y88b.   888   888   888    888   
 888     888  888   888   888 .  888   888   888   888  888    .o      `88b    d88' o.  )88b  888   888   888    888 . 
o888o   o888o `Y8bod8P'   "888" o888o o888o o888o o888o `Y8bod8P'       `Y8bood8P'  8""888P' o888o o888o o888o   "888"                                                                                                                                                                                                                                                                                                                                                                  =                                                                                                                                                                                                                                                                                                                              
{Fore.RED} Made By Hanako
{Fore.RED} 1 and 3 will redirect you to the website                                                                                                                       

{Fore.CYAN} [１] Ｅｎｔｅｒ Ｎａｍｅ Ｉｎｆｏ    
{Fore.CYAN} [２] Ｅｎｔｅｒ Ｐｈｏｎｅ Ｎｕｍｂｅｒ
{Fore.BLUE} [３] Ｅｎｔｅｒ Ａｄｄｒｅｓｓ Ｉｎｆｏ  
{Fore.BLUE} [４] Ｅｎｔｅｒ ＩＰ Ｉｎｆｏ
{Fore.MAGENTA} [５] Ｅｎｔｅｒ Ｅｍａｉｌ Ｉｎｆｏ
{Fore.MAGENTA} [６] Ｄｎｓ ｌｏｏｋｕｐ

'''

print(Fore.GREEN + content)
menu = input(Fore.GREEN + "Select an option [1-5]: ").strip()

if menu == "1":
    firstname = input("First name: ").strip().replace(" ", "+")
    lastname = input("Last name: ").strip().replace(" ", "+")
    location = input("City/State/Zip: ").strip().replace(" ", "+")
    query = f"{firstname}+{lastname}+{location}"
    url = f"https://www.beenverified.com/people/{query}/"
    print(f"\nOpening: {url}")
    webbrowser.open(url)

elif menu == "2":
    phone = input("Enter phone number (with country code): ").strip()
    url = f"http://apilayer.net/api/validate?access_key={phone_api_key}&number={phone}"

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
    house = input("House number: ").strip().replace(" ", "+")
    street = input("Street name: ").strip().replace(" ", "+")
    city = input("City: ").strip().replace(" ", "+")
    state = input("State abbreviation: ").strip().upper()
    url = f"https://www.beenverified.com/address-lookup/{house}+{street}+{city}+{state}/"
    print(f"\nOpening: {url}")
    webbrowser.open(url)

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

elif menu == "5":
    email = input("Enter email address: ").strip()
    url = f"http://apilayer.net/api/check?access_key={email_api_key}&email={email}&smtp=1&format=1"

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

if menu == "6":
    domain = 'example.com'
    api_url = 'https://api.api-ninjas.com/v1/dnslookup?domain={}'.format(domain)
    response = requests.get(api_url, headers={'X-Api-Key': 'fd2C3hFP53JrglsQFalzLg==p2qiqWdqaUVCNLno
'})
    if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)


else:
    print(f"{Fore.RED}[!] Invalid selection.")

input("\nPress Enter to exit...")
