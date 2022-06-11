import random
import string
import datetime
import logging
from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver
from constants.base import BaseConstants


def random_int():
    return str(random.randint(333333, 778888))


def random_letters(length=4):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


class User:

    def __init__(self, first_name="", last_name="", email="", phone="", password=""):
        self.first_name = first_name if first_name else f"Name{random_letters()}"
        self.last_name = last_name if last_name else f"Lastname{random_letters()}"
        self.email = email if email else f"email{random_int()}@email.com"
        self.phone = phone if phone else "0999999999"
        self.password = password if password else f"Password{random_int()}"


def create_driver():
    driver = WebDriver(executable_path=BaseConstants.DRIVER_PATH)
    driver.implicitly_wait(1)
    driver.get(BaseConstants.BASE_URL)
    return driver


def wait_until_ok(timeout=5, period=0.25):
    logger = logging.getLogger("[WaitUntilOk]")

    def decorator(original_function):

        def wrapper(*args, **kwargs):
            end_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout)
            while True:
                try:
                    return original_function(*args, **kwargs)
                except Exception as err:
                    if datetime.datetime.now() > end_time:
                        logger.warning(f"Catch: {err}")
                        raise err
                    sleep(period)

        return wrapper

    return decorator
