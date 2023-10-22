import socket
import subprocess
import webbrowser

def main():
    var1 = input("Please enter the website name without http. ")

    print("""
    Please choose a method:
    
    (1) DNS bruteforce (Output saved in the out.txt file)
    (2) NMAP
    (3) Netcraft Toolbar
    """)

    m1 = input("Enter the method number: ")

    if m1 == '1':
        print("""
        mail, forum, direct, direct-connect, ftp, cpanel, blog, dev, m, support, webmail, ssl, record, dns, help will be checked for possible IP.
        """)

        dns = '198.61.167.32'

        def resolve_ip(domain):
            try:
                ip = socket.gethostbyname(domain)
                return ip
            except socket.gaierror:
                return None

        def check_and_save_ip(subdomain, domain):
            ip = resolve_ip(f"{subdomain}.{domain}")
            if ip is not None:
                print(f"{subdomain}.{domain} IP is {ip}")
                with open('out.txt', 'a') as file:
                    file.write(f"{subdomain}.{domain} IP is {ip}\n")
            else:
                print(f"{subdomain}.{domain} NOT FOUND.")

        check_and_save_ip('mail', var1)
        check_and_save_ip('forum', var1)
        check_and_save_ip('direct', var1)
        check_and_save_ip('direct-connect', var1)
        check_and_save_ip('ftp', var1)
        check_and_save_ip('cpanel', var1)
        check_and_save_ip('blog', var1)
        check_and_save_ip('dev', var1)
        check_and_save_ip('m', var1)
        check_and_save_ip('support', var1)
        check_and_save_ip('webmail', var1)
        check_and_save_ip('ssl', var1)
        check_and_save_ip('record', var1)
        check_and_save_ip('dns', var1)
        check_and_save_ip('help', var1)

        print("Please open out.txt file for possible IPs.")

    elif m1 == '2':
        try:
            subprocess.run(["nmap", "--script", "dns-brute", "-sn", var1])
        except FileNotFoundError:
            print("NMAP is not installed. Please install NMAP to use this feature.")

    elif m1 == '3':
        print("Open a new browser window in Firefox and then view Hosting History.")
        webbrowser.open_new_tab(f"http://toolbar.netcraft.com/site_report?url={var1}")

    else:
        print("Invalid method number. Please choose a valid method.")

if __name__ == '__main__':
    main()
