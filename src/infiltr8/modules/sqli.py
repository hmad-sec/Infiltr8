import requests
from rich import print

def run(url, console):
    payloads = ["'", '"', "'--", "' OR '1'='1", '" OR "1"="1']
    vulnerable = False

    console.print(f"\n[bold blue][*] Testing SQLi payloads on {url}...[/bold blue]\n")

    for payload in payloads:
        test_url = url + payload
        try:
            response = requests.get(test_url)
            errors = ["syntax", "mysql", "warning", "unterminated", "ORA-", "SQL"]
            if any(err.lower() in response.text.lower() for err in errors):
                print(f"[red][!] Possible SQL Injection:[/red] {test_url}")
                vulnerable = True
        except requests.RequestException:
            print(f"[yellow][-] Skipped (error):[/yellow] {test_url}")

    if not vulnerable:
        console.print("[green][+] No obvious SQLi vulnerabilities detected.[/green]")