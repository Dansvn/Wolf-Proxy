import requests
from bs4 import BeautifulSoup
import time
import random
from colour import Color

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'


ascii_art = """

   ▄█    █▄       ▄████████ ▀████    ▐████▀ ▀████    ▐████▀ ▀████    ▐████▀ 
  ███    ███     ███    ███   ███▌   ████▀    ███▌   ████▀    ███▌   ████▀  
  ███    ███     ███    ███    ███  ▐███       ███  ▐███       ███  ▐███    
 ▄███▄▄▄▄███▄▄   ███    ███    ▀███▄███▀       ▀███▄███▀       ▀███▄███▀    
▀▀███▀▀▀▀███▀  ▀███████████    ████▀██▄        ████▀██▄        ████▀██▄     
  ███    ███     ███    ███   ▐███  ▀███      ▐███  ▀███      ▐███  ▀███    
  ███    ███     ███    ███  ▄███     ███▄   ▄███     ███▄   ▄███     ███▄  
  ███    █▀      ███    █▀  ████       ███▄ ████       ███▄ ████       ███▄ 
             
             我爱你，雷娜塔
- version: 1.0
- github: https://github.com/slyhax

"""

print(Colors.CYAN + ascii_art + Colors.RESET)

valid_proxy_file = "./valid_proxy.txt" 
URL = "https://www.us-proxy.org/"

# def open_file():

def collect_proxies(url):
    print(Colors.YELLOW + "[*] Fetching proxy list..." + Colors.RESET)
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
            print(Colors.GREEN + f"[+] Valid proxy: {proxy}" + Colors.RESET)
            with open(valid_proxy_file, 'a') as file:
                file.write(proxy + '\n')
            return True
        else:
            print(Colors.RED + f"[-] Invalid proxy: {proxy}" + Colors.RESET)
            return False
    except requests.RequestException:
        print(Colors.RED + f"[-] Invalid proxy: {proxy}" + Colors.RESET)
        return False


def main():
    proxies = collect_proxies(URL)

    print(Colors.CYAN + "\n[*] Testing proxies..." + Colors.RESET)
    valid_proxies = []

    for proxy in proxies:
        time.sleep(random.randint(1, 2)) 
        if test_proxy(proxy):
            valid_proxies.append(proxy)


    print(Colors.MAGENTA + "\n[*] Valid proxies found:" + Colors.RESET)
    for proxy in valid_proxies:
        print(Colors.BLUE + f"  {proxy}" + Colors.RESET)

if __name__ == "__main__":
    main()


