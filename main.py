"""скрапінг сайту http://quotes.toscrape.com. 
Мета - отримати два файли: 
1. qoutes.json, куди помістіть всю інформацію про цитати з усіх сторінок сайту та 
2. authors.json, де буде знаходитись інформація про авторів зазначених цитат. 
Структура файлів json має повністю збігатися зі структурою файлів попереднього домашнього завдання. 
Використайте раніше написані скрипти для завантаження json файлів у хмарну базу даних для отриманих файлів. 
Попередня домашня робота має коректно працювати з новою отриманою базою даних."""

from scraping import authors_data, quotes_data, scrape_quotes
from json_to_db import save_to_json, load_json_to_db
from colors import lightblue_, gray_


def main():
    url = "https://quotes.toscrape.com"

    print(lightblue_("Processing:"))

    print(lightblue_("Step 1: Scraping quotes..."))
    print(gray_(scrape_quotes(url), 3))

    print(lightblue_("Step 2: Saving authors to JSON..."))
    print(gray_(save_to_json(authors_data, "authors.json"), 3))

    print(lightblue_("Step 3: Saving quotes to JSON..."))
    print(gray_(save_to_json(quotes_data, "quotes.json"), 3))

    print(lightblue_("Step 4: Uploading data to a cloud database..."))
    print(gray_(load_json_to_db(), 3))

    print(lightblue_("Processing completed"))


if __name__ == "__main__":
    main()
