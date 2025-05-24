import socket
from concurrent.futures import ThreadPoolExecutor
from rich.progress import track

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((host, port))
            if result == 0:
                return port
    except:
        pass
    return None

def parse_ports(port_range):
    if "-" in port_range:
        start, end = map(int, port_range.split("-"))
        return range(start, end + 1)
    else:
        return [int(port_range)]

def run(host, port_range, console):
    console.print(f"[cyan][+] Scanning {host} for open ports in range {port_range}...[/cyan]")

    ports = parse_ports(port_range)
    open_ports = []

    with ThreadPoolExecutor(max_workers=100) as executor:
        results = track(executor.map(lambda p: scan_port(host, p), ports), total=len(ports), description="Scanning")

    for port in results:
        if port:
            open_ports.append(port)

    if open_ports:
        console.print(f"[green][+] Open ports on {host}:[/green] {', '.join(map(str, open_ports))}")
    else:
        console.print(f"[yellow][-] No open ports found on {host}[/yellow]")