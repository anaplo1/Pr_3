import logging
from logging import FileHandler

handler = FileHandler("/Users/anaplo1/Documents/Python projects/Pr 3/Task 6/log.txt", "w")
logger = logging.getLogger(__name__)
logger.addHandler(handler)


def run_with_log(func):
    try:
        func(1, 0)
    except Exception as err:
            logger.exception("Ошибка деления", exc_info=True)


def f(a, b):
    return a / b


run_with_log(f)
