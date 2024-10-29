#Bienvenue sur Nastyca-Tools !

#Outil Python à But Éducatif :
#Cet outil a été créé dans un but éducatif.
#Veuillez l'utiliser uniquement à des fins d'apprentissage et de formation.

#---------------------------------------------------------------------------------------------

import os
import json
import re

from colorama import Fore, init

folder_path = input(f"{Fore.LIGHTMAGENTA_EX}Chemin du dossier ->{Fore.RESET} ")
output_file = 'emails.json'

print(f"\n[/] Veuillez patienter...")

def extraction(data):
    emails = []
    if isinstance(data, dict):
        for key, value in data.items():
            emails.extend(extraction(value))
    elif isinstance(data, list):
        for item in data:
            emails.extend(extraction(item))
    elif isinstance(data, str):
        emails.extend(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", data))
    return emails

def tri(folder_path):
    all_emails = set()
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    try:
                        data = json.load(f)
                        emails = extraction(data)
                        all_emails.update(emails)
                    except json.JSONDecodeError:
                        print(f"{Fore.RED}\n[-] Erreur de lecture JSON dans le fichier '{Fore.RESET}{file_path}{Fore.RED}'{Fore.RESET}")
                    except UnicodeDecodeError:
                        print(f"{Fore.RED}\n[-] Erreur d'encodage dans le fichier '{Fore.RESET}{file_path}{Fore.RED}'{Fore.RESET}")
    return list(all_emails)

def sauvegarde(emails):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(emails, f, indent=4)
    print(f"\n{Fore.GREEN}[+] Emails enregistrés dans '{Fore.RESET}{output_file}{Fore.GREEN}'{Fore.RESET}")

emails = tri(folder_path)
sauvegarde(emails)

#---------------------------------------------------------------------------------------------
