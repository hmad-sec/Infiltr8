import requests

def run(url, wordlist_path):
    print(f"[+] Starting directory brute-force on {url}")
    try:
        with open(wordlist_path, "r") as file:
            for line in file:
                directory = line.strip()
                full_url = url.rstrip("/") + "/" + directory
                try:
                    res = requests.get(full_url, timeout=5)
                    if res.status_code == 200:
                        print(f"[FOUND] {full_url}")
                except requests.RequestException:
                    continue
    except FileNotFoundError:
        print(f"[!] Wordlist not found: {wordlist_path}")