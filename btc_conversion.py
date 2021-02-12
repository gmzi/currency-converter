import conversion
from forex_python.bitcoin import BtcConverter
from decimal import *
from datetime import datetime, timedelta
from datetime import date

b = BtcConverter()
symbol = b.get_symbol()


class BtcConversion:
    def __init__(self, amount, curr):
        self.amount = amount
        self.curr = curr

    def price(self):
        return b.get_latest_price(self.curr)

    def convert_to_btc(self):
        return b.convert_to_btc(self.amount, self.curr)

    def convert_btc_to(self):
        return b.convert_btc_to_cur(self.amount, self.curr)


def convert_btc_to_cur(amt, curr):
    return b.convert_btc_to_cur(amt, curr)


def format(value=0, places=2, curr='', sep=',', dp='.', pos='', neg='-', trailneg=''):
    q = Decimal(10) ** -places
    sign, digits, exp = value.quantize(q).as_tuple()
    result = []
    digits = list(map(str, digits))
    build, next = result.append, digits.pop
    if sign:
        build(trailneg)
    for i in range(places):
        build(next() if digits else '0')
    if places:
        build(dp)
    if not digits:
        build('0')
    i = 0
    while digits:
        build(next())
        i += 1
        if i == 3 and digits:
            i = 0
            build(sep)
    build(curr)
    build(neg if sign else pos)
    return ''.join(reversed(result))


def rate(curr):
    return b.get_latest_price(curr)


def convert_to_curr(amt, curr):
    return b.convert_btc_to_cur(amt, curr)


def prev_prices(curr, days_back=90):
    today = datetime.now()
    start_date = today - timedelta(days=days_back)
    return b.get_previous_price_list(curr, start_date, today)


def format_nums(dictionary):
    for item in dictionary:
        dictionary[item] = format(
            value=Decimal(dictionary[item]))
    return dictionary
