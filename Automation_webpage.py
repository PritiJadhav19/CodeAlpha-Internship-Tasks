import requests
import re

url = "https://www.python.org"
response = requests.get(url)

if response.status_code == 200:
    html = response.text
    title = re.search(r"<title>(.*?)</title>", html)
    if title:
        with open("web_title.txt", "w") as f:
            f.write(title.group(1))
        print("Webpage title saved to 'web_title.txt'")
    else:
        print("Title tag not found!")
else:
    print("Failed to fetch webpage!")
