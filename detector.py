import nmap
import requests

def detect_cms(url):
    response = requests.get(url)
    cms = None

    if "joomla" in response.text.lower():
        cms = "Joomla"
        admin_url = url + "/administrator"
        print('Admin Url:' + admin_url)
    elif "wordpress" in response.text.lower():
        cms = "WordPress"
        admin_url = url + "/wp-admin"
        print('Admin Url:' + admin_url)

    return cms

def scan_with_nmap(target):
    nm = nmap.PortScanner()

    print(f"Scanning begins... Target: {target}\n")
    nm.scan(target, arguments="-T4 -A")

    for host in nm.all_hosts():
        print(f"Target IP: {host}")
        print("Open Ports:")

        for port, info in nm[host]["tcp"].items():
            print(f"Port {port}:")
            print(f" - Status: {info['state']}")
            print(f" - Service: {info['name']}")

        cms_url = f"http://{host}"
        detected_cms = detect_cms(cms_url)
        if detected_cms:
            print(f"Detected CMS: {detected_cms}")
        
        print("\n")

if __name__ == "__main__":
    target = input("Please enter the target IP address or IP range: ")
    scan_with_nmap(target)
