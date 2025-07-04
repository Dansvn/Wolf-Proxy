import os
import requests
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


user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:70.0) Gecko/20100101 Firefox/70.0",
]

ascii_art = f"""                                                                      

                                                 
              ▒▒              ▒▒                              
            ▒▒░░▒▒▒▒      ▒▒▒▒░░▒▒                            
          ▓▓░░  ░░░░▒▒▓▓▒▒░░░░  ░░▒▒                          
          ▓▓░░  ░░░░░░░░░░░░░░  ░░▒▒                          
          ▒▒░░    ░░░░░░░░░░    ░░▒▒                          
          ▒▒░░  ░░░░░░░░░░░░░░  ░░▒▒                          
            ▒▒░░░░  ░░░░░░  ░░░░▒▒                            
          ▒▒░░░░      ░░    ░░░░▒▒▒▒░░    ▒▒                  
          ▒▒░░    ██      ▓▓    ▒▒▓▓      ▒▒       _    _       _  __   _____                     
        ▒▒░░░░                  ░░░░▒▒    ▒▒  ▒▒  | |  | |     | |/ _| | ___ \                            
          ▒▒░░      ██████      ░░▒▒    ▒▒░░  ▒▒  | |  | | ___ | | |_  | |_/ / __ _____  ___   _          
            ▒▒░░      ██      ▒▒▓▓    ▒▒░░░░  ░░  | |/\| |/ _ \| |  _| |  __/ '__/ _ \ \/ / | | |          
          ▒▒░░▒▒░░          ░░▒▒░░▒▒▒▒░░░░░░▒▒    \  /\  / (_) | | |   | |  | | | (_) >  <| |_| |          
          ▒▒  ░░              ▓▓░░░░▒▒▒▒▒▒▒▒░░     \/  \/ \___/|_|_|   \_|  |_|  \___/_/\_\\__, |          
        ▒▒░░                ░░░░░░░░░░░░▒▒                                                  __/ |          
        ▒▒▒▒▒▒            ░░░░▒▒▒▒▒▒░░░░▒▒                                                 |___/        
        ▒▒░░░░▓▓      ▒▒  ░░░░▒▒░░░░░░░░▒▒                    
        ▒▒░░░░▒▒      ▒▒  ░░░░▒▒  ░░░░░░▒▒                    
        ▒▒░░    ▓▓  ▒▒      ░░▒▒      ▒▒     - version: 1.2               
          ▒▒      ▒▒          ▒▒  ▒▒  ▒▒     - github: https://github.com/6hax/proxy-hax                
        ▒▒  ▒▒  ▒▒  ▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒       - made by hax and dan
        ▒▒▓▓▒▒▒▒    ▓▓▒▒▒▒▒▒        

"""

print(Colors.CYAN + ascii_art)

valid_proxy_file = "./valid_proxy.txt"
proxy_urls_file = "./proxy_urls.txt"

if os.path.exists(valid_proxy_file):
    os.remove(valid_proxy_file)


def load_proxy_urls(file_path):
    if not os.path.exists(file_path):
        print(Colors.RED + f"[-] File {file_path} not found!")
        return []
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def fetch_proxies_from_url(url):
    print(Colors.YELLOW + "[*] Fetching proxy list...")
    headers = {"User-Agent": random.choice(user_agents)}
    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            proxies = [p.strip() for p in response.text.splitlines() if p.strip()]
            print(Colors.CYAN + f"  {len(proxies)} obtained proxies")
            return proxies
        else:
            print(
                Colors.RED
                + f"  Failed to download {url} (status {response.status_code})"
            )
    except Exception as e:
        print(Colors.RED + f"  Error when downloading  {url}: {e}")
    return []


def test_proxy(proxy):
    url = "https://httpbin.org/ip"
    proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
    try:
        headers = {"User-Agent": random.choice(user_agents)}
        response = requests.get(url, proxies=proxies, headers=headers, timeout=5)
        if response.status_code == 200:
            print(Colors.GREEN + f"[+] Valid proxy: {proxy}")
            with open(valid_proxy_file, "a") as f:
                f.write(proxy + "\n")
            return True
        else:
            print(Colors.RED + f"[-] Invalid proxy: {proxy}")
    except requests.RequestException:
        print(Colors.RED + f"[-] Invalid proxy: {proxy}")
    return False


def main():
    urls = load_proxy_urls(proxy_urls_file)
    if not urls:
        print(Colors.RED + "[-] No proxy URL to download.")
        return

    all_proxies = set()
    for url in urls:
        proxies = fetch_proxies_from_url(url)
        if proxies:
            all_proxies.update(proxies)

    print(Colors.CYAN + "\n[*] Testing proxies...")
    valid_proxies = []

    for proxy in all_proxies:
        time.sleep(random.uniform(1, 2))
        if test_proxy(proxy):
            valid_proxies.append(proxy)

    print(Colors.MAGENTA + "\n[*] Valid proxies found:")
    for proxy in valid_proxies:
        print(Colors.BLUE + f"  {proxy}")


if __name__ == "__main__":
    main()
