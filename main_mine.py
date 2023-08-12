from bs4 import BeautifulSoup
import requests

url = "https://programmer100.pythonanywhere.com/tours/"

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')

# print(soup.prettify())
print("*" * 50)

print(soup.find(class_="animated fadeIn mb-4"))
print(soup.find(class_="animated fadeIn mb-4").text)
print("*" * 50)
print(soup.find(id="displaytimer"))
print(soup.find(id="displaytimer").text)