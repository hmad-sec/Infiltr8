import sys
import argparse
from rich.console import Console
from rich.text import Text
from pyfiglet import Figlet

from infiltr8.modules import subdomain, dirbuster, sqli, headers, portscan, waf, xss


console = Console()

def main():
    console = Console()

    figlet = Figlet(font="digital")
    console.print(figlet.renderText("Infiltr8"), style="bold red")
    console.print("[bold]Infiltr8[/bold] - Web App Pentesting Toolkit\n", style="bold white")

    parser = argparse.ArgumentParser(description="Infiltr8 - Web App Pentesting Toolkit")
    subparsers = parser.add_subparsers(dest="module", help="Available modules")

    # Subdomain module
    subdomain_parser = subparsers.add_parser("subdomain", help="Enumerate subdomains")
    subdomain_parser.add_argument("domain", help="Target domain")

    # Dirbuster module
    dirbuster_parser = subparsers.add_parser("dirbuster", help="Directory brute-forcing")
    dirbuster_parser.add_argument("url", help="Target URL")
    dirbuster_parser.add_argument("-w", "--wordlist", help="Path to wordlist", required=True)

    # SQLi module
    sqli_parser = subparsers.add_parser("sqli", help="SQL injection testing")
    sqli_parser.add_argument("url", help="Target URL")

    # Headers module
    headers_parser = subparsers.add_parser("headers", help="Fetch HTTP headers")
    headers_parser.add_argument("url", help="Target URL")

    # Portscan module
    portscan_parser = subparsers.add_parser("portscan", help="Scan open ports on target host")
    portscan_parser.add_argument("host", help="Target IP or hostname")
    portscan_parser.add_argument("-p", "--ports", help="Ports to scan, e.g., 80 or 1-1000", default="1-1024")

    # Waf module
    waf_parser = subparsers.add_parser("waf", help="Detect presence of WAF on target")
    waf_parser.add_argument("target", help="Target URL or IP address")

    # XSS module
    xss_parser = subparsers.add_parser("xss", help="Test for reflected XSS")
    xss_parser.add_argument("url", help="Target URL with a query parameter")

    # login brute-force
    login_parser = subparsers.add_parser("login", help="Brute-force login form")
    login_parser.add_argument("url", help="Login URL (POST endpoint)")
    login_parser.add_argument("-u", "--username", required=True, help="Username to brute-force for")
    login_parser.add_argument("-w", "--wordlist", required=True, help="Password wordlist file")
    login_parser.add_argument("--user-field", default="username", help="Form field name for username")
    login_parser.add_argument("--pass-field", default="password", help="Form field name for password")

    # Session analysis module
    session_parser = subparsers.add_parser("session", help="Analyze session handling and cookies")
    session_parser.add_argument("url", help="Target URL")

    # Tech stack fingerprinting module
    tech_parser = subparsers.add_parser("techstack", help="Identify technologies used by the target web app")
    tech_parser.add_argument("url", help="Target URL")


    args = parser.parse_args()

    if args.module == "subdomain":
        subdomain.run(args.domain, console)
    elif args.module == "dirbuster":
        dirbuster.run(args.url, args.wordlist, console)
    elif args.module == "sqli":
        sqli.run(args.url, console)
    elif args.module == "headers":
        headers.run(args.url, console)
    elif args.module == "portscan":
        portscan.run(args.host, args.ports, console)
    elif args.module == "waf":
        waf.detect_waf(args.target)
    elif args.module == "xss":
        from infiltr8.modules.xss import inject_xss
        inject_xss(args.url)
    elif args.module == "login":
        from infiltr8.modules.login_brute import login_bruteforce
        login_bruteforce(args.url, args.user_field, args.pass_field, args.username, args.wordlist)
    elif args.module == "session":
        from infiltr8.modules.session_analysis import check_session_security
        check_session_security(args.url)
    elif args.module == "techstack":
        from infiltr8.modules.techstack import fingerprint_tech
        fingerprint_tech(args.url)
    else:
        parser.print_help()

if __name__ == "__main__":
    sys.exit(main())