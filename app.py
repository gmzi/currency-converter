from flask import Flask, request, render_template, redirect, flash, jsonify
import conversion
import btc_conversion
from decimal import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "converter"


@app.route('/')
def show_form():
    return render_template('base1.html')


@app.route('/convert')
def convert():
    amount = Decimal(request.args['amount'])
    fro = request.args.get('from-curr')
    to = request.args.get('to-curr')
    vals = [fro, to]
    if 'BTC' in vals:
        if vals[0] == 'BTC':
            calc = btc_conversion.convert_to_curr(amount, to)
            result = btc_conversion.format(value=calc)
            rate = btc_conversion.rate(to)
            calc_rates = btc_conversion.prev_prices(to)
            prev_rates = btc_conversion.format_nums(calc_rates)
        if vals[1] == 'BTC':
            operation = btc_conversion.BtcConversion(Decimal(amount), fro)
            result = operation.convert_to_btc()
            rate = btc_conversion.rate(fro)
            calc_rates = btc_conversion.prev_prices(fro)
            prev_rates = btc_conversion.format_nums(calc_rates)
        return render_template('btc_result.html', result=result, amount=amount, fro=fro, to=to, rate=rate, dict_item=prev_rates)
    if "BTC" not in vals:
        operation = conversion.Conversion(fro, to, Decimal(amount))
        result = operation.convert_and_format()
        calc_rate = operation.rate()
        rate = conversion.format(Decimal(calc_rate), places=4)
        calc_all_currs = conversion.all_currs(fro)
        all_currs = btc_conversion.format_nums(calc_all_currs)
        return render_template('result.html', result=result, amount=amount, fro=fro, to=to, rate=rate,
                               dict_item=all_currs
                               )
