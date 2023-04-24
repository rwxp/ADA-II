from accionesPD1 import accionesPD1
from accionesPD2 import accionesPD2
from accionesFB import accionesFB
from accionesVR import programacion_voraz
import PySimpleGUI as sg

layout = [[sg.Text('Seleccione un archivo de entrada:')],
          [sg.Input(key='-FILE-'), sg.FileBrowse()],
          [sg.Text('Seleccione una función:')],
          [sg.Combo(['Programación dinámica 1','Programación dinámica 2','Fuerza Bruta', 'Voraz'], key='function')],
          [sg.Button('Calcular')],
          [sg.Text('Entrada:')],
          [sg.Output(key='-INPUT-', size=(80, 5))],
          [sg.Text('Salida:')],
          [sg.Output(key='-OUTPUT-', size=(80, 20))]
         ]

window = sg.Window('Ejemplo', layout)

while True:
    event, values = window.read()
    if event == 'Calcular':
        file_path = values['-FILE-']
        with open(file_path, 'r') as f:
            lines = f.readlines()
            A = int(lines[0])
            B = int(lines[1])
            n  = int(lines[2]) 
            offers = lines[3:]
            offers = [tuple(int(num) for num in line[:-1].split(',') if num) for line in offers]
            
            # Actualiza el área de texto de entrada
            window['-INPUT-'].update(value=f'A={A}, B={B}, n={n}, offers={offers}')
            
            if values['function'] == 'Programación dinámica 1':
                result = accionesPD1(A,B, n, offers)
            elif values['function'] == 'Programación dinámica 2':
                result = accionesPD2(A,B, n, offers)
            elif values['function'] == 'Fuerza Bruta':
                result = accionesFB(A,B,n, offers)
            elif values['function'] == 'Voraz':
                result = programacion_voraz(A,B,n, offers)
            
            # Actualiza el área de texto de salida
            window['-OUTPUT-'].update(value=result)
            
    if event == sg.WIN_CLOSED:
        break

window.close()
