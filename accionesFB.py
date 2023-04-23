import os
def accionesFB(A,B, n, ofertas):
    num_ofertas = len(ofertas)
    ranges = [ofertas[i][1] for i in range(num_ofertas)]
    last_elem = ranges[len(ranges)-1]
    vr= []
    combinations = []
    for i in range(2**num_ofertas):
        combination = []
        for j in range(len(ranges)):
            if ranges[j] == last_elem and sum(combination) < A :
              combination.append(A - sum(combination)) 
            elif i & (1 << j):
                combination.append(ranges[j])
            else:
              combination.append(0)
        if sum(combination)==A:
          combinations.append(combination)


    ##Me estaba repitiendo asignaciones a la hora de imprimir
    unique_arr = []
    for item in combinations:
        if item not in unique_arr:
            unique_arr.append(item)
            vr.append(calcular_valor(A,B,item,ofertas))
    vr_index= vr.index(max(vr))
    vr_combination = combinations[vr_index]
    output_dir = 'accionesFB-output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    i = 1
    while os.path.exists(os.path.join(output_dir, f'salida{i}.txt')):
        i += 1
    with open(os.path.join(output_dir, f'salida{i}.txt'), 'w') as f:
        f.write(f'{max(vr)}\n')
        for item in vr_combination:
            f.write(f'{item}\n')
    return "La función accionesFB ha sido ejecuta, diríjase a la carpeta accionesFB-output para ver la salida."


def calcular_valor(A, B, asignacion, ofertas):
    valor = 0
    acciones_vendidas = 0

    for i in range(len(ofertas)):
        acciones_vendidas += asignacion[i] 
        valor += asignacion[i] * ofertas[i][0] 

    valor += (A - acciones_vendidas) * B
    
    return valor
