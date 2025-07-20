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
    firstname = input("First name: ")
    lastname = input("Last name: ")
    location = input("City/State/Zip: ")
    url = f"https://www.beenverified.com/?utm_source=brave&utm_medium=cpc&utm_campaign=BV_PPL_SEA_PRP_PPS_Brave_Peace_Of_Mind&utm_querytype=nonbrand{firstname}-{lastname}_{location}"
    print(f"\nOpening: {url}")
    webbrowser.open(url)

elif menu == "2":
    part1 = input("First 3 digits: ")
    part2 = input("Next 3 digits: ")
    part3 = input("Last 4 digits: ")
    url = f"https://www.beenverified.com/reverse-phone/"
    print(f"\nOpening: {url}")
    webbrowser.open(url)

elif menu == "3":
    house = input("House number: ")
    street = input("Street: ")
    city = input("City: ")
    state = input("State: ")
    url = f"https://www.beenverified.com/reverse-address-lookup/"
    print(f"\nOpening: {url}")
    webbrowser.open(url)

elif menu == "4":
    ip = input("IP ")
    url = f"https://www.iplocation.net/ip-lookup"
    print(f"\nOpening: {url}")
    webbrowser.open(url)

elif menu == "5":
    ip = input("Email ")
    url = f"https://www.beenverified.com/email-search/"
    print(f"\nOpening: {url}")
    webbrowser.open(url)

else:
    print(f"{Fore.RED}[!] Invalid selection.")

input("\nPress Enter to exit...")
