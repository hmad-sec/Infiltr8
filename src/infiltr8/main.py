import argparse
from rich import print
from rich.console import Console

from infiltr8.modules import subdomain, dirbuster, sqli

console = Console()

def show_banner():
    print(r"""
[bold red]
  _____        _  __ _       
 |  ___|__  __| |/ _(_)_ __  
 | |_ / _ \/ _` | |_| | '_ \ 
 |  _|  __/ (_| |  _| | | | |
 |_|  \___|\__,_|_| |_|_| |_|

[/bold red]
[bold]Infiltr8[/bold] - Web App Pentesting Toolkit
""")

def main():
    parser = argparse.ArgumentParser(
        description="Infiltr8 - A Python CLI toolkit for basic web app pentesting tasks"
    )
    subparsers = parser.add_subparsers(dest="command")

    # Subdomain
    sub_parser = subparsers.add_parser("subdomain", help="Enumerate subdomains using crt.sh")
    sub_parser.add_argument("domain", help="Target domain")

    # Dirbuster
    dir_parser = subparsers.add_parser("dirbuster", help="Simple directory brute-forcer")
    dir_parser.add_argument("url", help="Target URL")
    dir_parser.add_argument("-w", "--wordlist", required=True, help="Path to wordlist file")

    # SQLi
    sqli_parser = subparsers.add_parser("sqli", help="Basic SQL injection payload tester")
    sqli_parser.add_argument("url", help="Target URL with injectable parameter (e.g. ?id=1)")

    args = parser.parse_args()
    show_banner()

    if args.command == "subdomain":
        subdomain.run(args.domain, console)
    elif args.command == "dirbuster":
        dirbuster.run(args.url, args.wordlist, console)
    elif args.command == "sqli":
        sqli.run(args.url, console)
    else:
        parser.print_help()