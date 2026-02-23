import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin 

url = input("Enter URL: ")

response = requests.get(url)
data = BeautifulSoup(response.text, "html.parser")

print("PAGE TITLE:")
if data.title:
    print(data.title.get_text())
else:
    print("No Title Found!")

print("\nPAGE BODY:")
if data.body:
  print(data.body.get_text())
else:
   print("No Body Found!")

print("\nLINKS:")
for link in data.find_all('a'):
    if link.get("href"):
      print(urljoin(url, link.get('href')))
    else:
      print("No link Found!")
