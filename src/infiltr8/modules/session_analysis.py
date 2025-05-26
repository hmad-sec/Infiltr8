import requests
from urllib.parse import urlparse
from rich import print
from rich.console import Console

console = Console()

def check_session_security(url):
    try:
        response = requests.get(url)
        cookies = response.cookies

        if not cookies:
            console.print("[yellow]No cookies set on this response.[/yellow]")
            return

        for cookie in cookies:
            console.print(f"\n[bold cyan]Cookie Name:[/bold cyan] {cookie.name}")
            console.print(f"[bold]Value:[/bold] {cookie.value}")
            console.print(f"[bold]Domain:[/bold] {cookie.domain}")
            console.print(f"[bold]Path:[/bold] {cookie.path}")
            console.print(f"[bold]Secure:[/bold] {cookie.secure}")
            console.print(f"[bold]HttpOnly:[/bold] {cookie.has_nonstandard_attr('HttpOnly')}")

            if not cookie.secure:
                console.print("[red]⚠ Cookie is not marked Secure[/red]")
            if not cookie.has_nonstandard_attr("HttpOnly"):
                console.print("[red]⚠ Cookie is not marked HttpOnly[/red]")
            else:
                console.print("[green]✓ Cookie is HttpOnly[/green]")

        server_headers = response.headers
        if 'Set-Cookie' in server_headers:
            console.print(f"\n[bold magenta]Raw Set-Cookie Header:[/bold magenta] {server_headers['Set-Cookie']}")

    except requests.RequestException as e:
        console.print(f"[red]Error connecting to target: {e}[/red]")