import os
from colorama import Fore, init

init(autoreset=True)

os.system('cls' if os.name == 'nt' else 'clear')

print(f'''
{Fore.RED}
██████╗░██╗░█████╗░░█████╗░
██╔══██╗██║██╔══██╗██╔══██╗
██████╔╝██║██║░░╚═╝██║░░██║
██╔══██╗██║██║░░██╗██║░░██║
██║░░██║██║╚█████╔╝╚█████╔╝
╚═╝░░╚═╝╚═╝░╚════╝░░╚════╝░
''')

print(f'{Fore.RED}           ╔══════════════════════════╗')
print(f'{Fore.RED}           ║{Fore.WHITE}   [1] Enter Name Info    {Fore.RED}║')
print(f'{Fore.RED}           ║{Fore.WHITE}   [2] Enter Phone Number {Fore.RED}║')
print(f'{Fore.RED}           ║{Fore.WHITE}   [3] Enter Address Info {Fore.RED}║')
print(f'{Fore.RED}           ║{Fore.WHITE}   [4] Enter IP Info      {Fore.RED}║')
print(f'{Fore.RED}           ╚══════════════════════════╝\n')

menu = input(f'{Fore.YELLOW}[?] Select an option > {Fore.RESET}')

if menu == "1":
    firstname = input("First name: ")
    lastname = input("Last name: ")
    location = input("City/State/Zip: ")
    print(f"\nMock search link: https://example.com/name/{firstname}-{lastname}_{location}")

elif menu == "2":
    part1 = input("First 3 digits: ")
    part2 = input("Next 3 digits: ")
    part3 = input("Last 4 digits: ")
    print(f"\nMock phone search: https://example.com/phone/{part1}-{part2}-{part3}")

elif menu == "3":
    house = input("House number: ")
    street = input("Street: ")
    city = input("City: ")
    state = input("State: ")
    print(f"\nMock address search: https://example.com/address/{house}-{street}_{city}-{state}")

elif menu == "4":
    ip = input("IP address: ")
    print(f"\nMock IP lookup: https://example.com/ip/{ip}")

else:
    print(f"{Fore.RED}[!] Invalid selection.")
