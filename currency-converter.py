import PySimpleGUI as sg

sg.theme('Reddit')
layout = [
    [sg.Text('Currency Converter')],
    [sg.Combo(['United States Dollar','Brazilian Real','Euro','Pound Sterling']), sg.Input(key = 'input')],
    [sg.Combo(['United States Dollar','Brazilian Real','Euro','Pound Sterling']), sg.Text('', size = (0,1), key='output')],
    [sg.Button('Show Result') ,sg.Button('Exit')]
]

window = sg.Window('Currency Converter', layout)
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    elif event == 'Show Result':
        input = values['input']
        window['output'].update(value = input)


window.close()