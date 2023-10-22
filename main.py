import os
print("\---VulnShot---/")
print('''1)XSS
         2)SQL INJECTION
         3)FILE UPLOAD
         4)Cloudflare Bypass IP
         5)LFI
         6)Nmap Scanner and CMS Detector''')
choice = input(">>> ")
if choice == '1':
  os.system('python xssfile.py')
if choice == '2':
  os.system('python sqlfile.py')
if choice == '3':
  os.system('python fileup.py')
if choice == '4':
  os.system('python cloudflarebypass.py')
if choice == '5':
  os.system('python lfi.py')
if choice == '6':
  os.system('python detector.py')
