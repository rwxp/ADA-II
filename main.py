from accionesPD1 import accionesPD1
from accionesPD2 import accionesPD2
from accionesFB import accionesFB
from accionesVR import accionesVR
import PySimpleGUI as sg

import time

layout = [[sg.Text('Seleccione un archivo de entrada:')],
          [sg.Input(key='-FILE-'), sg.FileBrowse()],
          [sg.Text('Seleccione una función:')],
          [sg.Combo(['Fuerza Bruta', 'Programación Voraz', 'Programación dinámica 1','Programación dinámica 2',], key='function', default_value='Fuerza Bruta')],
          [sg.Button('Calcular')],
          [sg.Button('Ver Entrada')],
          [sg.Text('Entrada:')],
          [sg.Output(key='-INPUT-', size=(80, 5))],
          [sg.Text('Salida:')],
          [sg.Output(key='-OUTPUT-', size=(80, 18))],
          [sg.Output(key='-TIME-', size=(80, 2))]
         ]

window = sg.Window('Ejemplo', layout)

while True:
    event, values = window.read()
    if event == 'Ver Entrada':
        file_path = values['-FILE-']
        if file_path:
            with open(file_path, 'r') as f:
                lines = f.readlines()
                A = int(lines[0])
                B = int(lines[1])
                n  = int(lines[2]) 
                offers = lines[3:]
                offers = [tuple(int(num) for num in line[:-1].split(',') if num) for line in offers]
            window['-INPUT-'].update(value=f'A={A}\nB={B}\nn={n}\nOfertas:\n{offers}')
        else:
            window['-INPUT-'].update(value='No se seleccionó archivo de entrada')

    if event == 'Calcular':
        file_path = values['-FILE-']
        with open(file_path, 'r') as f:
            lines = f.readlines()
            A = int(lines[0])
            B = int(lines[1])
            n  = int(lines[2]) 
            offers = lines[3:]
            offers = [tuple(int(num) for num in line[:-1].split(',') if num) for line in offers]
            
            # Actualiza el area de texto de entrada
            window['-INPUT-'].update(value=f'A={A}\nB={B}\nn={n}\nOfertas:\n{offers}')
            
            start = time.time()
            if values['function'] == 'Programación dinámica 1':
                result = accionesPD1(A,B, n, offers)
            elif values['function'] == 'Programación dinámica 2':
                if(len(offers) > n+1):
                    M = int(lines[-1])
                    offers.pop()
                else:
                    M = 1
                result = accionesPD2(A,B, n, M, offers)
            elif values['function'] == 'Fuerza Bruta':
                result = accionesFB(A,B,n, offers)
            elif values['function'] == 'Programación Voraz':
                result = accionesVR(A,B,n, offers)
            
            end = time.time()
            window['-TIME-'].update(value=f'Tiempo de ejecución: {end - start} segundos')
            # Actualiza el area de texto de salida
            window['-OUTPUT-'].update(value=result)
            
    if event == sg.WIN_CLOSED:
        break

window.close()
