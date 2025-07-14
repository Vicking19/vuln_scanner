import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Common payloads
XSS_PAYLOAD = "<script>alert('XSS')</script>"
SQLI_PAYLOADS = ["' OR '1'='1", '" OR "1"="1', "';--", '" AND 1=0 --']

def get_all_forms(url):
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
    details = {"action": form.get("action"), "method": form.get("method", "get").lower(), "inputs": []}
    for input_tag in form.find_all("input"):
        input_type = input_tag.get("type", "text")
        name = input_tag.get("name")
        value = input_tag.get("value", "")
        details["inputs"].append({"type": input_type, "name": name, "value": value})
    return details

def is_vulnerable(response, payload):
    return payload in response.text

def test_xss(url):
    forms = get_all_forms(url)
    print(f"\n🔍 Testing {len(forms)} forms for XSS on {url}")
    for form in forms:
        details = get_form_details(form)
        data = {}
        for input in details["inputs"]:
            if input["type"] == "text" or input["type"] == "search":
                data[input["name"]] = XSS_PAYLOAD
            else:
                data[input["name"]] = input["value"]

        target_url = urljoin(url, details["action"])
        if details["method"] == "post":
            res = requests.post(target_url, data=data)
        else:
            res = requests.get(target_url, params=data)

        if is_vulnerable(res, XSS_PAYLOAD):
            print(f"⚠️ XSS Vulnerability detected in form: {target_url}")
        else:
            print(f"✅ No XSS detected in form: {target_url}")

def test_sqli(url):
    print(f"\n🔍 Testing URL for SQLi: {url}")
    for payload in SQLI_PAYLOADS:
        params = {"id": payload}  # assume 'id' is a query parameter
        res = requests.get(url, params=params)
        errors = ["you have an error in your sql syntax", "warning: mysql", "unclosed quotation mark"]
        for error in errors:
            if error.lower() in res.text.lower():
                print(f"⚠️ SQL Injection possible with payload: {payload}")
                break
        else:
            print(f"✅ No SQLi detected with payload: {payload}")

if __name__ == "__main__":
    target = input("🔗 Enter the target URL (with http/https): ").strip()
    test_xss(target)
    test_sqli(target)