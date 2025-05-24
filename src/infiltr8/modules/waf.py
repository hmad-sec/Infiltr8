import requests
from rich.console import Console
from rich.table import Table
from urllib.parse import urlparse

console = Console()

COMMON_WAF_SIGNATURES = {
    "Cloudflare": ["cf-ray", "cloudflare"],
    "Akamai": ["akamai", "akamai-ghost"],
    "Sucuri": ["sucuri"],
    "Imperva Incapsula": ["incapsula"],
    "F5 BIG-IP": ["bigip"],
    "AWS WAF": ["aws"],
    "Barracuda": ["barracuda"],
    "StackPath": ["stackpath"],
    "DOSarrest": ["dosarrest"],
    "Citrix NetScaler": ["netscaler"],
    "Alibaba Cloud": ["alibaba"]
}

def detect_waf(target_url):
    try:
        response = requests.get(target_url, timeout=5)
        headers = response.headers
        waf_found = False

        table = Table(title="WAF Detection Results", style="bold red")
        table.add_column("WAF Vendor", style="cyan")
        table.add_column("Matched Header(s)", style="green")

        for vendor, patterns in COMMON_WAF_SIGNATURES.items():
            matched = []
            for key, value in headers.items():
                for pattern in patterns:
                    if pattern.lower() in key.lower() or pattern.lower() in value.lower():
                        matched.append(f"{key}: {value}")
            if matched:
                waf_found = True
                table.add_row(vendor, "\n".join(matched))

        if waf_found:
            console.print(table)
        else:
            console.print("[bold green]No known WAF detected.[/bold green]")

    except requests.RequestException as e:
        console.print(f"[bold red]Request failed: {e}[/bold red]")