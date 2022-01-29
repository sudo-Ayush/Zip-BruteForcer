from zipfile import ZipFile
from os import system, name
from colorama import Fore
from ast import For
import colorama
import time
import os

colorama.init(autoreset=True)

if name == 'nt':
	_ = system('cls')

else:
	_ = system('clear')

print(f'{Fore.YELLOW}STARTING Zip-BruteForcer...')
time.sleep(2)

if name == 'nt':
	_ = system('cls')

else:
	_ = system('clear')

print(f"""{Fore.BLUE}
 _____ _                ____                _         _____                            
|__  /(_) _ __         | __ )  _ __  _   _ | |_  ___ |  ___|___   _ __  ___  ___  _ __ 
  / / | || '_ \  _____ |  _ \ | '__|| | | || __|/ _ \| |_  / _ \ | '__|/ __|/ _ \| '__|
 / /_ | || |_) ||_____|| |_) || |   | |_| || |_|  __/|  _|| (_) || |  | (__|  __/| |   
/____||_|| .__/        |____/ |_|    \__,_| \__|\___||_|   \___/ |_|   \___|\___||_|   
         |_|
""")

print(f"{Fore.LIGHTCYAN_EX}[*] Make sure <ZIP file> and <Password list>, both present in the currect directory or wirte the absolute path of the file.")

name = input(f"{Fore.YELLOW}[*] Enter the name of the ZIP file: ")
password_list = input(f"{Fore.YELLOW}[*] Enter the name of the Password List: ")

if name == 'nt':
	_ = system('cls')

else:
	_ = system('clear')

with open(password_list, 'r') as passwd:
    passwords = passwd.read().splitlines()


with ZipFile(name, 'r') as zip:
    for password in passwords:
        try:
            zip.extractall(pwd= bytes(password, 'utf-8'))

        except:
            continue

        else:
            print(f"{Fore.GREEN}[+]Password found : {password}")
            break
        exit()
    
    else:
        print(f'{Fore.RED}[x] Password not found! Use different password list')
        n_name = name.split(".")
        n_name = n_name[0]
        delete = f'rm -rf {n_name}'
        os.system(delete)
