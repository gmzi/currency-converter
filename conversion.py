from flask.json import tojson_filter
from forex_python.converter import CurrencyRates
from decimal import *

c = CurrencyRates()


class Conversion:
    def __init__(self, fro, to, amount):
        self.amount = amount
        self.to = to
        self.fro = fro

    def rate(self):
        return c.get_rate(self.fro, self.to)

    # taken from Decimal docs: https://docs.python.org/3/library/decimal.html

    def convert_and_format(self, value=0, places=2, curr='', sep=',', dp='.', pos='', neg='-', trailneg=''):
        if not value:
            value = c.convert(self.fro, self.to, self.amount)
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


# print(c.get_rates('USD'))


currs = {'GBP': 0.7224417552, 'HKD': 7.7526138141, 'IDR': 13964.8472873961, 'ILS': 3.2543837985, 'DKK': 6.1233226311, 'INR': 72.7784638182, 'CHF': 0.8892730715, 'MXN': 19.925660657, 'CZK': 21.2167613402, 'SGD': 1.3237836503, 'THB': 29.8600477484, 'HRK': 6.23100354, 'EUR': 0.8232485387, 'MYR': 4.0424796246, 'NOK': 8.4461183831, 'CNY': 6.4582201367,
         'BGN': 1.6101094921, 'PHP': 48.0307894953, 'PLN': 3.702560303, 'ZAR': 14.6153782827, 'CAD': 1.266485552, 'ISK': 128.2621223347, 'BRL': 5.3458467111, 'RON': 4.0129250021, 'NZD': 1.3807524492, 'TRY': 7.0185230921, 'JPY': 104.6513542438, 'RUB': 73.5812957932, 'KRW': 1103.1283444472, 'USD': 1.0, 'AUD': 1.2873960649, 'HUF': 294.047913065, 'SEK': 8.3039433605}

# for key in currs:
#     print(f"<option name='to-curr' value='{key}'>{key}</option>")


def all_currs(curr):
    return c.get_rates(curr)


def format(value, places=2, curr='', sep=',', dp='.', pos='', neg='-', trailneg=''):
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


# print(format(Decimal(0.1344447432), places=4))
