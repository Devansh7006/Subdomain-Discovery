try:
    import requests
except ModuleNotFoundError:
    import subprocess, sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

domain = input("Enter the base domain (e.g., example.com): ").strip()

try:
    with open("wordlist.txt", "r") as file:
        subdomains = file.read().splitlines()
except FileNotFoundError:
    print("Error: 'subdomains.txt' file not found in current directory.")
    exit()

for sub in subdomains:
    url = f"http://{sub}.{domain}"
    try:
        response = requests.get(url, timeout=3)
        if response.status_code < 400:
            print(f"[+] Valid domain: {url}")
    except requests.ConnectionError:
        pass
    except requests.exceptions.RequestException as e:
        print(f"[-] Error checking {url}: {e}")
