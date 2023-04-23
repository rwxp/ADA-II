import os

def accionesPD1(A, B, n, offers):
    dp = [[-float('inf') for _ in range(A + 1)] for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        p, c, r = offers[i - 1]
        for j in range(A + 1):
            dp[i][j] = dp[i - 1][j]
            for k in range(r, min(c, j) + 1):
                dp[i][j] = max(dp[i][j], dp[i - 1][j - k] + k * p)
    result = [0] * n
    i = n
    j = A
    while i > 0 and j > 0:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            p, c, r = offers[i - 1]
            k = min(c, j)
            while k >= r and dp[i][j] != dp[i - 1][j - k] + k * p:
                k -= 1
            result[i - 1] = k
            j -= k
            i -= 1
    costo = 0 
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
    return "La función accionesPD1 ha sido ejecuta, diríjase a la carpeta accionesPD1-output para ver la salida."

