import os

def programacion_voraz(A, B, n, ofertas):
    # Inicializar asignación
    asignacion = [0] * (n+1)

    # Asignar recursos a las ofertas en orden descendente de tasa de valoración
    for oferta in ofertas:
        if oferta[2] <= A:
            cantidad_asignada = min(oferta[1], A)
            asignacion[ofertas.index(oferta)] = cantidad_asignada
            A -= cantidad_asignada

    # Calcular la suma de las ventas
    ventas = sum([asignacion[i] * ofertas[i][0] for i in range(n)])
    ventas += (A * B)

    # Guardar archivo de salida
    output_dir = 'accionesVR-output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    i = 1
    while os.path.exists(os.path.join(output_dir, f'salida{i}.txt')):
        i += 1
    with open(os.path.join(output_dir, f'salida{i}.txt'), 'w') as f:
        f.write(f'{ventas}\n')
        for item in asignacion:
            f.write(f'{item}\n')
    print("La funcion programacion_voraz ha sido ejecutada, dirijase a la carpeta accionesVR-output para ver la salida.")
    return f'{ventas}\n' + '\n'.join(str(item) for item in asignacion)
