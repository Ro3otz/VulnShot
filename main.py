import os
print("\---VulnShot---/")
print('''1)XSS
         2)SQL
         3)FILE UPLOAD''')
choice = input(">>> ")
if choice == '1':
  os.system('python xssfile.py')
if choice == '2':
  os.system('python sqlfile.py')
if choice == '3':
  os.system('python fileup.py')
