import requests
from rich import print
from urllib.parse import urljoin

def run(url, wordlist_path, console):
    try:
        with open(wordlist_path, "r") as f:
            words = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        console.print(f"[bold red]Error:[/bold red] Wordlist file not found: {wordlist_path}")
        return

    console.print(f"\n[bold blue][*] Scanning directories at {url}...[/bold blue]\n")

    for word in words:
        full_url = urljoin(url, word)
        try:
            response = requests.get(full_url)
            if response.status_code == 200:
                print(f"[green][+] Found:[/green] {full_url}")
        except requests.RequestException:
            print(f"[yellow][-] Skipped (unreachable):[/yellow] {full_url}")