from locale import currency
import PySimpleGUI as sg
from forex_python.converter import CurrencyRates

c = CurrencyRates()

sg.theme('Reddit')
layout = [
    [sg.Text('Currency Converter')],
    [sg.Combo(['USD','EUR','BRL','CNY','GBP'], key = 'currencyInput'), sg.Input(key = 'input')],
    [sg.Combo(['USD','EUR','BRL','CNY','GBP'], key = 'currencyOutput'), sg.Text('', size = (0,1), key='output')],
    [sg.Button('Show Result') ,sg.Button('Exit')]
]

window = sg.Window('Currency Converter', layout)
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    elif event == 'Show Result':
        def converter(value, input, output):
            rate = c.get_rate(input, output)
            return int(value) * rate
        result = converter(values['input'],values['currencyInput'],values['currencyOutput'])
        window['output'].update(value = "%.2f" % result)


window.close()