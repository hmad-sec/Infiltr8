import requests

def run(domain):
    print(f"[+] Searching crt.sh for subdomains of {domain}...")
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        response = requests.get(url, timeout=10)
        subdomains = set()
        for entry in response.json():
            name = entry.get("name_value", "")
            for sub in name.splitlines():
                if domain in sub:
                    subdomains.add(sub.strip())
        for sub in sorted(subdomains):
            print(sub)
    except Exception as e:
        print(f"[!] Error: {e}")