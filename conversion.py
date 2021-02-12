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

    # adapted from Decimal docs: https://docs.python.org/3/library/decimal.html:

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
