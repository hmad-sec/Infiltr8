# Infiltr8
**Infiltr8** is a Python CLI toolkit designed for web application penetration testing. It brings together multiple offensive tools in one command-line interface for fast, focused testing.

## Features
- 🔍 **Subdomain Enumeration** – Uses `crt.sh` to find subdomains.
- 📂 **Directory Bruteforce** – Recursively brute-forces directories with a custom wordlist.
- 🛡️ **HTTP Headers** – Fetches and displays HTTP headers.
- 💉 **SQLi Testing** – Naive GET-parameter-based SQLi detection.
- 📡 **Port Scanning** – Scans ports across a target IP or host.
- 🔥 **WAF Detection** – Identifies possible Web Application Firewalls in front of targets.
- 🧪 **XSS Scanner** – Detects reflected Cross-Site Scripting (XSS) vulnerabilities using payload injection.

## Installation

Clone the repository:

```bash
git clone https://github.com/hmad-sec/Infiltr8.git
cd Infiltr8
```

Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # or venv/Scripts/activate on Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install the CLI tool:

```bash
pip install -e .
```

Now you can use `infiltr8` from anywhere:

```bash
infiltr8 --help
```

## Usage

#### Subdomain Enumeration
```bash
infiltr8 subdomain example.com
```

#### Directory Bruteforce
```bash
infiltr8 dirbuster https://example.com -w wordlist.txt
```

#### HTTP Headers
```bash
infiltr8 headers https://example.com
```

#### SQL Injection Test
```bash
infiltr8 sqli https://example.com/product?id=1
```

#### Port Scanner
```bash
infiltr8 portscan 127.0.0.1 -p 22-100
```

#### WAF Detection
```bash
infiltr8 waf https://example.com
```

#### XSS Scanner
```bash
infiltr8 xss https://example.com/search?q=test
```

## Examples

You can find example usage output and screenshots in the `examples/` directory.

## Built With
- [Python](https://www.python.org/)
- [argparse](https://docs.python.org/3/library/argparse.html)
- [requests](https://pypi.org/project/requests/)
- [rich](https://pypi.org/project/rich/)
- [pyfiglet](https://pypi.org/project/pyfiglet/)

## Roadmap
- [x] Subdomain enum – Uses crt.sh to find subdomains.
- [x] Dirbuster – Recursively brute-forces directories.
- [x] SQLi test – Simple SQL injection tester.
- [x] Headers fetch – Displays HTTP response headers.
- [x] Portscanner – Scans specified port ranges.
- [x] WAF detection – Identify common WAFs via behavior and headers.
- [x] XSS scanner – Test for reflected XSS payloads.
- Login brute-force – Attempt to brute-force web login forms.
- Session analysis – Evaluate cookie flags, session handling.
- Tech stack fingerprinting – Identify tech used by target web apps.
- CORS misconfig scanner – Detect overly permissive CORS settings.
- Vulnerability DB checker – Match target info against known CVEs.
- CSP & security header analyzer – Check for missing/misconfigured headers.
- Command injection tester – Attempt basic OS injection payloads.
- WHOIS lookup – Display WHOIS info for domains.
- DNS record enumerator – Lookup DNS A, MX, TXT, and NS records.
- Parameter discovery – Fuzz for common parameter names.
- Open redirect tester – Identify improperly validated redirect URLs.
- Admin panel finder – Discover common admin URLs.
- Swagger/OpenAPI crawler – Auto-enumerate API endpoints from spec.
- JWT analyzer – Decode and inspect JWTs for weaknesses.

## Contributing
Pull requests are welcome! For major changes, please open an issue first, to discuss what you would like to change.

## Disclaimer
This tool is intended for **educational** and **authorized testing** purposes only.

## Contact
- Built by [@HmadSec](https://github.com/hmad-sec) • 2025
- LinkedIn - (https://linkedin.com/in/hammaadm/)