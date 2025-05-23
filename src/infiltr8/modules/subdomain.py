import requests

def run(domain, console):
    console.print(f"[cyan][*] Enumerating subdomains for {domain}...[/cyan]")
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        res = requests.get(url, timeout=10)
        subdomains = set()
        for entry in res.json():
            name = entry.get("name_value", "")
            for sub in name.splitlines():
                if domain in sub:
                    subdomains.add(sub.strip())
        for sub in sorted(subdomains):
            console.print(f"[green][+] {sub}[/green]")
    except Exception as e:
        console.print(f"[red][!] Error: {e}[/red]")