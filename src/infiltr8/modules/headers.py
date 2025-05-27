import requests
from rich.console import Console
from rich.table import Table

def run(url, console):
    console = Console()
    try:
        response = requests.get(url, timeout=5)
        table = Table(title=f"HTTP Headers for {url}")

        table.add_column("Header", style="cyan", no_wrap=True)
        table.add_column("Value", style="magenta")

        for key, value in response.headers.items():
            table.add_row(key, value)

        console.print(table)
    except Exception as e:
        console.print(f"[red]Failed to fetch headers:[/red] {e}")