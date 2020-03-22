import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
import json
from parser_2.config import site


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('result.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow([data['url_gif'],
                        data['title']])


def main():
    for i in range(0, 150, 15):
        url = site.format(i)
        response = get_html(url)
        for j in range(len(json.loads(response.strip())['data'])):
            url_gif = json.loads(response.strip())['data'][j]['images']['downsized_large']['url']
            title = json.loads(response.strip())['data'][j]['title']

            data = {'url_gif': url_gif,
                    'title': title}

            write_csv(data)


if __name__ == '__main__':
    main()
