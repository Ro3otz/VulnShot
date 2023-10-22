import requests
target_url = input("Target Url: ")

file_path = input("File: ")
files = {'file': open(file_path, 'rb')}

upload_response = requests.post(target_url, files=files)

if upload_response.status_code == 200:
    script_url = target_url + '/scripts.php'
    script_response = requests.get(script_url)
    if script_response.status_code == 200:
    	print("[INFO] File Injection Found")
    else:
    	print("[CRITICAL] File Injection Not Found")
