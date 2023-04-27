import os
# implementación similiar solo que A se divide en 5000
def accionesPD2(A, B, n, M, offers):
    dp = [[-float('inf') for _ in range(A + 1)] for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        p, c, r = offers[i - 1]
        for j in range(0, A + 1,  M):
            dp[i][j] = dp[i - 1][j]
            for k in range(r, min(c, j) + 1, M):
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
    output_dir = 'accionesPD2-output'
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


