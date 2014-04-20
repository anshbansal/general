__author__ = 'Aseem'

from datetime import date


def today(date_format="%d-%m-%Y"):
    return date.today().strftime(date_format)