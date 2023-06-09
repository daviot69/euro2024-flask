from helpers.config import get_config
from datetime import datetime
from time import gmtime, strftime


if __name__ == "__main__":
    config = get_config()

    print(config["entry_closing_date"])

    dt_utcnow = datetime.utcnow()

    print(dt_utcnow)

    print(dt_utcnow > config["entry_closing_date"])
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    print("Your Time Zone is GMT", strftime("%z", gmtime()))
    print(gmtime())
