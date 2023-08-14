import requests
import selectorlib
import smtplib, ssl
import os
import sqlite3

URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/39.0.2171.95 Safari/537.36'}

# "INSERT INTO events VALUES ('Tigers', 'Tiger City', '4.3.2093')"
# "SELECT * FROM events WHERE date='31.10.2091'"
# "DELETE FROM events WHERE band='Tigers'"


def scrape(url):
    response = requests.get(url, headers=HEADERS)
    content = response.text
    return content


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)['tours']
    if value == "No upcoming tours":
        return None
    else:
        return value


def check_if_exists(extr):
    with open("data.txt", "r") as file:
        existings = file.readlines()
    existings = [each.strip("\n") for each in existings]
    print(extr in existings)
    return extr in existings


def check_db(extr):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    band, city, date = extr.split(",")


def store_text(extr):
    with open("data.txt", "a") as file:
        file.write(extr + "\n")
        print("new data written")


def store_db(extr):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    band, city, date = extr.split(",")
    cursor.execute("INSERT INTO events VALUES (?,?,?)", (band.strip(), city.strip(), date.strip()))
    cursor.execute("SELECT * FROM events")  # Query all data
    conn.commit()
    rows = cursor.fetchall()
    print(rows)
    print("stored in db")


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = os.getenv("GMAIL")
    password = os.getenv("GMAIL_PASS")

    receiver = os.getenv("GMAIL")
    context = ssl.create_default_context()

    # with smtplib.SMTP_SSL(host, port, context=context) as server:
    #     server.login(username, password)
    #     server.sendmail(username, receiver, message)
    print("mail sent")


if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)
    if extracted:
        if check_if_exists(extracted):
            print("already in the list")
        else:
            send_email(extracted)
            store_text(extracted)
            store_db(extracted)
