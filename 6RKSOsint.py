import os
import webbrowser
from colorama import Fore, init

init(autoreset=True)

os.system('cls' if os.name == 'nt' else 'clear')

print(f'''
{Fore.RED}
░█████╗░██████╗░██╗░░██╗░██████╗
██╔═══╝░██╔══██╗██║░██╔╝██╔════╝
██████╗░██████╔╝█████═╝░╚█████╗░
██╔══██╗██╔══██╗██╔═██╗░░╚═══██╗
╚█████╔╝██║░░██║██║░╚██╗██████╔╝
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░
{Fore.RESET}
''')

print(f'{Fore.RED}           ╔══════════════════════════╗')
print(f'{Fore.RED}           ║   [1] Enter Name Info    ║')
print(f'{Fore.RED}           ║   [2] Enter Phone Number ║')
print(f'{Fore.RED}           ║   [3] Enter Address Info ║')
print(f'{Fore.RED}           ║   [4] Enter IP Info      ║')
print(f'{Fore.RED}           ╚══════════════════════════╝\n')

menu = input(f'{Fore.CYAN}[?] Select an option > {Fore.RESET}')

if menu == "1":
    firstname = input("First name: ")
    lastname = input("Last name: ")
    location = input("City/State/Zip: ")
    url = f"https://example.com/name/{firstname}-{lastname}_{location}"
    print(f"\nOpening: {url}")
    webbrowser.open(url)

elif menu == "2":
    part1 = input("First 3 digits: ")
    part2 = input("Next 3 digits: ")
    part3 = input("Last 4 digits: ")
    url = f"https://example.com/phone/{part1}-{part2}-{part3}"
    print(f"\nOpening: {url}")
    webbrowser.open(url)

elif menu == "3":
    house = input("House number: ")
    street = input("Street: ")
    city = input("City: ")
    state = input("State: ")
    url = f"https://example.com/address/{house}-{street}_{city}-{state}"
    print(f"\nOpening: {url}")
    webbrowser.open(url)

elif menu == "4":
    ip = input("IP address: ")
    url = f"https://example.com/ip/{ip}"
    print(f"\nOpening: {url}")
    webbrowser.open(url)

else:
    print(f"{Fore.RED}[!] Invalid selection.")

input("\nPress Enter to exit...")
