import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from rich import print
from rich.console import Console

console = Console()

XSS_PAYLOAD = "<script>alert('xss')</script>"

def inject_xss(url):
    parsed = urlparse(url)
    query = parse_qs(parsed.query)

    if not query:
        console.print("[red][!] No query parameters found in URL to test.[/red]")
        return

    # Inject payload into all parameters
    xss_query = {k: XSS_PAYLOAD for k in query}
    new_query = urlencode(xss_query, doseq=True)
    new_url = urlunparse(parsed._replace(query=new_query))

    console.print(f"[blue][*] Testing XSS on:[/blue] {new_url}")

    try:
        r = requests.get(new_url, timeout=10)
        if XSS_PAYLOAD in r.text:
            console.print(f"[bold green][+] Reflected XSS detected![/bold green] Payload found in response.")
        else:
            console.print(f"[yellow][-] No reflected XSS detected.[/yellow]")
    except requests.RequestException as e:
        console.print(f"[red][!] Request failed: {e}[/red]")