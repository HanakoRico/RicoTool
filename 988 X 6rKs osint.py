import os
import webbrowser
from colorama import Fore, init

init(autoreset=True)

os.system('cls' if os.name == 'nt' else 'clear')

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

print(f'{Fore.CYAN}           ╔══════════════════════════╗')
print(f'{Fore.CYAN}           ║   [1] Enter Name Info    ║')
print(f'{Fore.BLUE}           ║   [2] Enter Phone Number ║')
print(f'{Fore.BLUE}           ║   [3] Enter Address Info ║')
print(f'{Fore.MAGENTA}           ║   [4] Enter IP Info      ║')
print(f'{Fore.MAGENTA}           ║   [5] Enter Email Info   ║')
print(f'{Fore.MAGENTA}           ╚══════════════════════════╝\n')

menu = input(f'{Fore.GREEN}[?] Select an option > {Fore.RESET}')

if menu == "1":
    firstname = input("First name: ").strip().replace(" ", "+")
    lastname = input("Last name: ").strip().replace(" ", "+")
    location = input("City/State/Zip: ").strip().replace(" ", "+")
    query = f"{firstname}+{lastname}+{location}"
    url = f"https://www.beenverified.com/people/{query}/"
    print(f"\nOpening: {url}")
    webbrowser.open(url)

elif menu == "2":
    phone = input("Enter full phone number (digits only): ").strip()
    url = f"https://www.beenverified.com/phone/{phone}/"
    print(f"\nOpening: {url}")
    webbrowser.open(url)

elif menu == "3":
    house = input("House number: ").strip().replace(" ", "+")
    street = input("Street name: ").strip().replace(" ", "+")
    city = input("City: ").strip().replace(" ", "+")
    state = input("State abbreviation: ").strip().upper()
    url = f"https://www.beenverified.com/address-lookup/{house}+{street}+{city}+{state}/"
    print(f"\nOpening: {url}")
    webbrowser.open(url)

elif menu == "4":
    ip = input("IP address: ").strip()
    url = f"https://www.iplocation.net/ip-lookup?query={ip}"
    print(f"\nOpening: {url}")
    webbrowser.open(url)

elif menu == "5":
    email = input("Email address: ").strip()
    url = f"https://www.beenverified.com/email/{email}/"
    print(f"\nOpening: {url}")
    webbrowser.open(url)

else:
    print(f"{Fore.RED}[!] Invalid selection.")

input("\nPress Enter to exit...")
