import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    title = soup.find_all('h3')
    data = []

    for i in title:
        item = i.getText()
        data.append(item)
    return data


def export_data(data):
    df = pd.DataFrame(data)
    df.to_excel("news.xlsx")
    df.to_csv('news.csv')


if __name__ == '__main__':
    data = get_data("https://indianexpress.com/")
    export_data(data)
    print("Finished  exporting.")
