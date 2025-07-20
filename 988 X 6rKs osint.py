import os
import requests
import webbrowser
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# Clear screen
os.system('cls' if os.name == 'nt' else 'clear')

# Banner
print(f'''
{Fore.MAGENTA}
░█████╗░░█████╗░░█████╗░  ██╗░░██╗  ░█████╗░██████╗░██╗░░██╗░██████╗
██╔══██╗██╔══██╗██╔══██╗  ╚██╗██╔╝  ██╔═══╝░██╔══██╗██║░██╔╝██╔════╝
╚██████║╚█████╔╝╚█████╔╝  ░╚███╔╝░  ██████╗░██████╔╝█████═╝░╚█████╗░
░╚═══██║██╔══██╗██╔══██╗  ░██╔██╗░  ██╔══██╗██╔══██╗██╔═██╗░░╚═══██╗
░█████╔╝╚█████╔╝╚█████╔╝  ██╔╝╚██╗  ╚█████╔╝██║░░██║██║░╚██╗██████╔╝
░╚════╝░░╚════╝░░╚════╝░  ╚═╝░░╚═╝  ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░
''')
print(" Made By Hanako ")

# Menu
print(f'{Fore.CYAN}           ╔══════════════════════════╗')
print(f'{Fore.CYAN}           ║   [1] Enter Name Info    ║')
print(f'{Fore.BLUE}           ║   [2] Enter Phone Number ║')
print(f'{Fore.BLUE}           ║   [3] Enter Address Info ║')
print(f'{Fore.MAGENTA}           ║   [4] Enter IP Info      ║')
print(f'{Fore.MAGENTA}           ║   [5] Enter Email Info   ║')
print(f'{Fore.MAGENTA}           ╚══════════════════════════╝\n')
print(" 1 and 3 will redirect you to the website")

menu = input(f'{Fore.GREEN}[?] Select an option > {Fore.RESET}')

# Name info → redirect
if menu == "1":
    url = f"https://www.beenverified.com/people/"
    print(f"\nOpening: {url}")
    webbrowser.open(url)

# Phone info
elif menu == "2":
    phone = input("Enter phone number (with country code): ").strip()
    api_key = "06b6f2d35967239292125f2cc9a76d35"  # Replace with your actual key
    url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone}"
    try:
        response = requests.get(url)
        data = response.json()
        if data.get("valid"):
            print("\n--- Phone Info ---")
            print(f"Country: {data.get('country_name')}")
            print(f"Location: {data.get('location')}")
            print(f"Carrier: {data.get('carrier')}")
            print(f"Line Type: {data.get('line_type')}")
        else:
            print(f"{Fore.YELLOW}[!] Invalid phone number.")
    except Exception as e:
        print(f"{Fore.RED}Error retrieving phone info: {e}")

# Address info → redirect
elif menu == "3":
    url = f"https://www.beenverified.com/address-lookup/"
    print(f"\nOpening: {url}")
    webbrowser.open(url)

# IP info
elif menu == "4":
    ip = input("Enter IP address (or leave blank for your IP): ").strip()
    if not ip:
        ip = ""
    url = f"https://ipinfo.io/{ip}/json"
    try:
        response = requests.get(url)
        data = response.json()
        print("\n--- IP Info ---")
        for key, value in data.items():
            print(f"{key.title()}: {value}")
    except Exception as e:
        print(f"{Fore.RED}Error retrieving IP info: {e}")

# Email info
elif menu == "5":
    email = input("Enter email address: ").strip()
    mailboxlayer_key = "ab153dcd49b5511b5dab7b16c7c2a8c0"  # Replace with your key
    url = f"http://apilayer.net/api/check?access_key={mailboxlayer_key}&email={email}&smtp=1&format=1"
    try:
        response = requests.get(url)
        data = response.json()
        print("\n--- Email Info ---")
        print(f"Format Valid: {data.get('format_valid')}")
        print(f"MX Found: {data.get('mx_found')}")
        print(f"SMTP Check: {data.get('smtp_check')}")
        print(f"Disposable: {data.get('disposable')}")
        print(f"Domain: {data.get('domain')}")
        print(f"Free Email: {data.get('free')}")
        print(f"Score: {data.get('score')} (0 to 1, higher = more deliverable)")
        if not data.get("format_valid"):
            print(f"{Fore.YELLOW}[!] Invalid email format.")
    except Exception as e:
        print(f"{Fore.RED}Error validating email: {e}")

# Invalid selection
else:
    print(f"{Fore.RED}[!] Invalid selection.")

# Keep window open
input("\nPress Enter to exit...")
