"""підключення до хмарної бази даних Atlas MongoDB"""

import configparser
from mongoengine import connect

if __name__ == "__main__":
    print("run 'seed.py' or 'main.py'")

else:
    config = configparser.ConfigParser()
    config.read("config.ini")

    mongo_user = config.get("DB", "user")
    mongodb_pass = config.get("DB", "pass")
    db_name = config.get("DB", "db_name")
    domain = config.get("DB", "domain")

    connect(
        host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority""",
        ssl=True,
    )
