"""скрипт для завантаження json файлів у хмарну базу даних"""

from connection import connect
import json
from models import Author, Quote


def save_to_json(data, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
    return f"{filename.split(".")[0].capitalize()} are successfully saved to file {filename}"


def load_json_to_db() -> str:
    def load_data(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    authors_data = load_data("authors.json")
    quotes_data = load_data("quotes.json")

    for author_data in authors_data:
        author = Author(
            fullname=author_data["fullname"],
            born_date=author_data["born_date"],
            born_location=author_data["born_location"],
            description=author_data["description"],
        )
        author.save()

    for quote_data in quotes_data:
        author = Author.objects(fullname=quote_data["author"]).first()
        quote = Quote(tags=quote_data["tags"], author=author, quote=quote_data["quote"])
        quote.save()

    return "Data uploaded successfully"
