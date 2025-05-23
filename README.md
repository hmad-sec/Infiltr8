# Infiltr8
**Infiltr8** is a Python CLI toolkit for basic web application penetration testing. It provides modules for subdomain enumeration, directory brute-forcing, and basic SQL injection testing — all with stylish terminal output using Rich.

## Features
- 🌐 Subdomain Enumeration (`crt.sh`)
- 📂 Directory Brute-forcing
- 💉 Basic SQL Injection Testing
- 🎨 Beautiful output with `rich`

## Installation (Dev Mode)
```bash
git clone https://github.com/yourusername/Infiltr8.git
cd Infiltr8
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -e .
```

## Usage

#### Subdomain Enumeration
```bash
infiltr8 subdomain example.com
```

#### Directory Bruteforce
```bash
infiltr8 dirbuster http://example.com -w wordlist.txt
```

#### SQLi Test
```bash
infiltr8 sqli http://example.com/page.php?id=1
```

## Modules
- subdomain: searches for subdomains using crt.sh
- dirbuster: bruteforces directories with a wordlist
- sqli:      tests URLs for basic SQL injection