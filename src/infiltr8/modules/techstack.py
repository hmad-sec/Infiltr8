import requests
from bs4 import BeautifulSoup
from rich import print
from rich.panel import Panel

def fingerprint_tech(url):
    try:
        response = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        headers = response.headers
        tech_found = []

        # Check headers
        if "X-Powered-By" in headers:
            tech_found.append(f"[bold yellow]X-Powered-By:[/bold yellow] {headers['X-Powered-By']}")
        if "Server" in headers:
            tech_found.append(f"[bold yellow]Server:[/bold yellow] {headers['Server']}")

        # Check cookies
        if "Set-Cookie" in headers:
            if "PHPSESSID" in headers["Set-Cookie"]:
                tech_found.append("[bold yellow]Detected:[/bold yellow] PHP session")
            if "ASP.NET_SessionId" in headers["Set-Cookie"]:
                tech_found.append("[bold yellow]Detected:[/bold yellow] ASP.NET")

        # Check HTML meta tags
        soup = BeautifulSoup(response.text, "html.parser")
        generator = soup.find("meta", attrs={"name": "generator"})
        if generator and generator.get("content"):
            tech_found.append(f"[bold yellow]Meta Generator:[/bold yellow] {generator['content']}")

        print(Panel.fit("\n".join(tech_found) if tech_found else "[red]No obvious tech stack indicators found.", title="Tech Stack Fingerprint"))

    except Exception as e:
        print(f"[red]Error during fingerprinting: {e}[/red]")
