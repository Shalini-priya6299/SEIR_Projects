import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = sys.argv[1]

if not url.startswith("http"):
    url = "https://" + url

options = Options()
options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.get(url)

soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

title = soup.title.get_text() 
if soup.title:
    print("Title:\n",title)
else:
    print("No Title Found")

body = soup.body.get_text() 
if soup.body:
    print("Body:\n", body)
else:
    print("No Body Found")

print("Links")
for link in soup.find_all("a", href=True):
    print(urljoin(url, link["href"]))
