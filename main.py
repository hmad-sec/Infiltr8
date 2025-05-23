import argparse
from modules import subdomain, dirbuster, sqli

def main():
    parser = argparse.ArgumentParser(description="Infiltr8 - Web App Pentesting Toolkit")
    subparsers = parser.add_subparsers(dest="command", help="Modules")

    # Subdomain enumeration
    sub_enum = subparsers.add_parser("subdomain", help="Enumerate subdomains using crt.sh")
    sub_enum.add_argument("domain", help="Target domain (e.g., example.com)")

    # Directory brute-force
    dirb = subparsers.add_parser("dirbuster", help="Directory brute-force using a wordlist")
    dirb.add_argument("url", help="Base URL (e.g., https://example.com/)")
    dirb.add_argument("wordlist", help="Path to wordlist file")

    # SQLi tester
    sqli_parser = subparsers.add_parser("sqli", help="Test URL for basic SQL injection")
    sqli_parser.add_argument("url", help="Target URL with injectable parameter (e.g., https://site.com/page.php?id=1)")

    args = parser.parse_args()

    if args.command == "subdomain":
        subdomain.run(args.domain)
    elif args.command == "dirbuster":
        dirbuster.run(args.url, args.wordlist)
    elif args.command == "sqli":
        sqli.run(args.url)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()