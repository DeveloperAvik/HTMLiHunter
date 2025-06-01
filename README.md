"""
HTMLiHunter - Advanced HTML Injection Scanner
=============================================

HTMLiHunter is an automated tool to detect HTML Injection vulnerabilities 
in web applications. It supports scanning GET and POST parameters, DOM 
reflection detection with Selenium, and custom payload injection.

Features:
- Injects multiple payloads into URL parameters and form inputs
- Detects reflected HTML in server responses and DOM using Selenium
- Supports custom payload lists
- Saves vulnerabilities to a JSON report file
- Color-coded terminal output for readability

Installation:
-------------
1. Ensure Python 3.7+ is installed.
2. Install dependencies with:

   pip install requests beautifulsoup4 selenium colorama lxml

3. Download ChromeDriver from:
   https://chromedriver.chromium.org/
   and add it to your system PATH.

Usage:
------
Run the scanner on a target URL:

    python htmlihunter.py "https://example.com/search?query=test"

With custom payloads (one per line in payloads.txt):

    python htmlihunter.py "https://example.com/search?query=test" --payloads payloads.txt

Output:
-------
- Prints scan progress and vulnerabilities found
- Saves report to `htmli_report.json`

License:
--------
MIT License (see LICENSE file or https://opensource.org/licenses/MIT)

Disclaimer:
-----------
Use only on targets you have permission to test.

Contact:
--------
Developed by Your Name
Email: your.email@example.com

Happy hunting! 🐛🔍
"""