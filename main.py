from accionesPD1 import accionesPD1
from accionesPD2 import accionesPD2
from accionesFB import accionesFB
import PySimpleGUI as sg

layout = [[sg.Text('Seleccione un archivo de entrada:')],
          [sg.Input(key='-FILE-'), sg.FileBrowse()],
          [sg.Text('Seleccione una función:')],
          [sg.Combo(['Programación dinámica 1','Programación dinámica 2','Fuerza Bruta'], key='function')],
          [sg.Button('Calcular')]]

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
            if values['function'] == 'Programación dinámica 1':
                print(accionesPD1(A,B, n, offers))
            if values['function'] == 'Programación dinámica 2':
                print(accionesPD2(A,B, n, offers))
            elif values['function'] == 'Fuerza Bruta':
                print(accionesFB(A,B,n, offers))
            pass
    if event == sg.WIN_CLOSED:
        break

window.close()