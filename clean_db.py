from connection import connect
from models import Author, Quote
from colors import lightred_, cyan_, lightblue_


def delete_all_documents():
    Author.objects().delete()
    Quote.objects().delete()

    print(lightblue_("Database cleaned successfully"))


if __name__ == "__main__":
    if (
        input(lightred_(">>> It is a database cleanup! Are you sure? (yes/no) "))
        == "yes"
    ):
        delete_all_documents()
    else:
        print(cyan_("Database cleanup canceled"))
