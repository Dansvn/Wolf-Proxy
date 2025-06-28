import requests
from bs4 import BeautifulSoup
import time
import random
from colorama import init, Fore, Style
init(autoreset=True)

class Colors:
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    MAGENTA = Fore.MAGENTA
    CYAN = Fore.CYAN
    RESET = Style.RESET_ALL

ascii_art = f"""

   ▄█    █▄       ▄████████ ▀████    ▐████▀ ▀████    ▐████▀ ▀████    ▐████▀ 
  ███    ███     ███    ███   ███▌   ████▀    ███▌   ████▀    ███▌   ████▀  
  ███    ███     ███    ███    ███  ▐███       ███  ▐███       ███  ▐███    
 ▄███▄▄▄▄███▄▄   ███    ███    ▀███▄███▀       ▀███▄███▀       ▀███▄███▀    
▀▀███▀▀▀▀███▀  ▀███████████    ████▀██▄        ████▀██▄        ████▀██▄     
  ███    ███     ███    ███   ▐███  ▀███      ▐███  ▀███      ▐███  ▀███    
  ███    ███     ███    ███  ▄███     ███▄   ▄███     ███▄   ▄███     ███▄  
  ███    █▀      ███    █▀  ████       ███▄ ████       ███▄ ████       ███▄ 
              
- version: 1.0
- github: https://github.com/emptyhax

"""

print(Colors.CYAN + ascii_art)

valid_proxy_file = "./valid_proxy.txt"
URL = "https://www.us-proxy.org/"

def collect_proxies(url):
    print(Colors.YELLOW + "[*] Fetching proxy list...")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', {'class': 'table table-striped table-bordered'})
    proxies = []

    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        ip = cols[0].text
        port = cols[1].text
        proxies.append(f"{ip}:{port}")
    
    return proxies

def test_proxy(proxy):
    url = "http://www.google.com"
    proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}

    try:
        response = requests.get(url, proxies=proxies, timeout=3)
        if response.status_code == 200:
            print(Colors.GREEN + f"[+] Valid proxy: {proxy}")
            with open(valid_proxy_file, 'a') as file:
                file.write(proxy + '\n')
            return True
        else:
            print(Colors.RED + f"[-] Invalid proxy: {proxy}")
            return False
    except requests.RequestException:
        print(Colors.RED + f"[-] Invalid proxy: {proxy}")
        return False

def main():
    proxies = collect_proxies(URL)

    print(Colors.CYAN + "\n[*] Testing proxies...")
    valid_proxies = []

    for proxy in proxies:
        time.sleep(random.randint(1, 2))
        if test_proxy(proxy):
            valid_proxies.append(proxy)

    print(Colors.MAGENTA + "\n[*] Valid proxies found:")
    for proxy in valid_proxies:
        print(Colors.BLUE + f"  {proxy}")

if __name__ == "__main__":
    main()

