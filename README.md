HTMLiHunter - Advanced HTML Injection Scanner
=============================================

HTMLiHunter is an automated tool to detect HTML Injection vulnerabilities 
in web applications. It supports scanning GET and POST parameters, DOM 
reflection detection with Selenium, and custom payload injection.

---

## 🚀 Features

- 🔍 Scans for **HTML Injection** and **Reflected XSS** vulnerabilities
- 🌐 Supports **GET** and **POST** parameter testing
- 🧠 Uses **Selenium + headless Chrome** for DOM-based reflection detection
- 🧾 Automatically parses and injects into **HTML forms**
- 🧨 Supports **custom payload lists**
- 💾 Outputs results to `htmli_report.json`
- 🌈 **Color-coded** output for readability
- 🔁 Built-in retry logic for unstable networks

---

Installation:
-------------
1. Ensure Python 3.7+ is installed.
2. Install dependencies with:

   pip3 install -r requirements.txt --break-system-packages (If you using Debian)

3. Download ChromeDriver from:
   https://chromedriver.chromium.org/
   and add it to your system PATH.

Usage:
------
Scan a Single URL:

    python exploit.py "https://example.com/search?query=test"

Scan Multiple URLs from File:

    python exploit.py -l urls.txt

Use Custom Payloads:

    python exploit.py -l urls.txt --payloads payloads.txt

Display Help:

    python exploit.py -h



Output:
-------
- Prints scan progress and vulnerabilities found
- Saves report to `htmli_report.json`

Terminal output will indicate:

✅ Successes and findings in green

🔵 Debug messages in blue

⚠️ Warnings or network issues in yellow

❌ DOM injection findings in red


Demo Video
🎬 [Watch the HTMLiHunter Demo on YouTube](https://youtu.be/vZzh86E6XA0)


License:
--------
MIT License (see LICENSE file or https://opensource.org/licenses/MIT)

Legal Disclaimer:
-----------
Use responsibly.

HTMLiHunter is intended for educational and authorized penetration testing only.
Scanning systems without explicit written permission is illegal and unethical.
You are solely responsible for how you use this tool.

--------
Developed by Avik Das
Email: developeravikdas@gmail.com

Happy hunting! 🐛🔍
