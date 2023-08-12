from bs4 import BeautifulSoup
import requests

url = "https://programmer100.pythonanywhere.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/39.0.2171.95 Safari/537.36'}

response = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.find(id="temperatureId").text)