import csv
import os
import random
from time import sleep

import requests
from bs4 import BeautifulSoup


def random_sleep():
    sleep(random.randint(2, 5))


def get_page_content(page: int, size: int = 100) -> str:
    query_parameters = {
        'indexName': 'auto,order_auto,newauto_search',
        'country.import.usa.not': '-1',
        'price.currency': '1',
        'abroad.not': '0',
        'custom.not': '1',
        'page': page,
        'size': size,
    }
    base_url = 'https://auto.ria.com/uk/search/'
    response = requests.get(base_url, params=query_parameters)
    response.raise_for_status()
    return response.text


def remove_file(file_path):
    try:
        os.remove(file_path)
    except OSError:
        pass


class CSVWritter:
    def __init__(self, filename, headers):
        self.filename = filename
        self.headers = headers
        remove_file(self.filename)

        with open(self.filename, 'a', encoding='UTF8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(headers)

    def write(self, row: list):
        with open(self.filename, 'a', encoding='UTF8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(row)


class StdOutWriter:
    def write(self, row: list):
        print(row)


def main():
    page = 0
    writers = [
        CSVWritter('cars1.csv', ['id', 'link']),
        CSVWritter('cars2.csv', ['id', 'link']),
        CSVWritter('cars3.csv', ['id', 'link']),
        # StdOutWriter(),
    ]

    while True:
        print(f'Page: {page}.')
        page_content = get_page_content(page)
        random_sleep()

        page += 1
        soup = BeautifulSoup(page_content)

        search_results = soup.find("div", {"id": "searchResults"})
        ticket_items = search_results.findAll('section', {'class': 'ticket-item'})[1:]

        if not ticket_items:
            breakpoint()
            break

        for ticket_item in ticket_items:
            car_details = ticket_item.find('div', {'class': 'hide'})
            car_id = car_details['data-id']
            data_link_to_view = car_details['data-link-to-view']
            csv_item = [car_id, data_link_to_view]

            for writer in writers:
                writer.write(csv_item)


if __name__ == '__main__':
    main()
