'''функції для скрапінгу'''

import requests
from bs4 import BeautifulSoup
from colors import gray_

quotes_data = []
authors_data = []


def find_next_url(soup, domain):
    try:
        next_url = soup.find("li", class_="next").a["href"]
        return domain + next_url if next_url else None
    except AttributeError:
        return None


def scrape_author_details(url) -> None:
    author_response = requests.get(url)
    author_soup = BeautifulSoup(author_response.text, features="html.parser")

    author_details = author_soup.find("div", class_="author-details")

    new_author = {
        "fullname": author_details.find("h3", class_="author-title").text,
        "born_date": author_details.find("span", class_="author-born-date").text,
        "born_location": author_details.find(
            "span", class_="author-born-location"
        ).text,
        "description": author_details.find(
            "div", class_="author-description"
        ).text.strip(),
    }

    if not new_author in authors_data:
        authors_data.append(new_author)


def scrape_quotes(url):
    domain = url  # виглядає як милиця

    while url:
        print(" -", gray_(url))
        response = requests.get(url)
        soup = BeautifulSoup(response.text, features="html.parser")

        quotes = soup.find_all("div", class_="quote")

        for quote in quotes:
            author = quote.find("small", class_="author").text.strip()
            author_url = domain + quote.a["href"]
            scrape_author_details(author_url)

            tags_list = [tag.text for tag in quote.find_all("a", class_="tag")]

            new_quote = {
                "tags": tags_list,
                "author": author,
                "quote": quote.find("span", class_="text").text.strip(),
            }
            quotes_data.append(new_quote)

        url = find_next_url(soup, domain)

    return "done"
