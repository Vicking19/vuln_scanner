# 🛡️ Web Vulnerability Scanner (Python)

A simple Python-based scanner to identify common web vulnerabilities such as **SQL Injection (SQLi)** and **Cross-Site Scripting (XSS)** in web applications.

---

## 🚀 Features

- ✅ Scans web forms for reflected **XSS vulnerabilities**
- ✅ Tests URLs for basic **SQL Injection** flaws
- ✅ Uses `requests` and `BeautifulSoup` for fast, lightweight analysis
- ✅ Command-line interface – simple to use

---

## 🧰 Requirements

Install dependencies using pip:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Use

1. **Clone or download** this repository:
   ```bash
   git clone https://github.com/Vicking19/vuln_scanner.git
   cd vuln_scanner
   ```

2. **Run the scanner**:
   ```bash
   python vuln_scanner.py
   ```

3. **Enter the target URL** when prompted:
   ```
   🔗 Enter the target URL (with http/https): http://example.com/page.php?id=1
   ```

---

## 📂 Example Output

```
🔍 Testing 2 forms for XSS on http://example.com
⚠️ XSS Vulnerability detected in form: /search

🔍 Testing URL for SQLi: http://example.com/page.php?id=1
⚠️ SQL Injection possible with payload: ' OR '1'='1
```

---

## ⚠️ Legal Disclaimer

> This tool is intended for **educational purposes** and **authorized penetration testing only**.  
> **Do not scan websites you do not own or have explicit permission to test.**

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Vikas Lalchand Mallah**  
📧 Email: vikas.malllah@example.com  
🔗 GitHub: [Vicking19](https://github.com/Vicking19)