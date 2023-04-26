import os

def accionesPD1(A, B, n, offers):
    #inicialización de la matriz que aloja los resultados para cada subproblema
    dp = [[-float('inf') for _ in range(A + 1)] for _ in range(n + 1)]
    dp[0][0] = 0
    #recorre cada oferta del arreglo
    for i in range(1, n + 1):
        p, c, r = offers[i - 1]
        #para cada oferta recorre cada posible asignación de A
        for j in range(A + 1): 
            dp[i][j] = dp[i - 1][j]
            # k va desde el minimo de acciones a comprar por cada i y va hasta el min entre el 
            # max de acciones a comprar "c" y "j"
            for k in range(r, min(c, j) + 1):
                #calcular el max entre la solución óptima anterior 
                # y la solución actual si se venden k acciones
                dp[i][j] = max(dp[i][j], dp[i - 1][j - k] + k * p)
    #array que guarda el resultado final de asignaciones
    result = [0] * n
    i = n
    j = A
    #while que va desde 0 < i < n y 0 < j < A O(A*n)
    while i > 0 and j > 0:
        #si la solución actual no cambia respecto a la anterior
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            p, c, r = offers[i - 1]
            k = min(c, j)
            #escogemos un k que representa el num de acciones que cumple 
            # con la restricción de min y hace parte de la solución óptima
            while k >= r and dp[i][j] != dp[i - 1][j - k] + k * p:
                k -= 1
            result[i - 1] = k
            j -= k
            i -= 1
    costo = 0 
    #calculamos el vr de la solución óptima
    for x in range(0, len(result)):
        costo += result[x]*offers[x][0]
    
    output_dir = 'accionesPD1-output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    i = 1
    while os.path.exists(os.path.join(output_dir, f'salida{i}.txt')):
        i += 1
    with open(os.path.join(output_dir, f'salida{i}.txt'), 'w') as f:
        f.write(f'{costo}\n')
        for item in result:
            f.write(f'{item}\n')
    return f'{costo}\n' + '\n'.join(str(item) for item in result)

