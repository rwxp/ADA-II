def accionesFB(A, B, n, ofertas):
    mejor_asignacion = None
    mejor_valor = 0
    for i in range(A+1):
        for j in range(A-i+1):
            for k in range(A-i-j+1):
                asignacion = [i, j, k, A-i-j-k]
                if es_valida(asignacion, B, ofertas):
                    valor = calcular_valor(asignacion, ofertas)
                    if valor > mejor_valor:
                        mejor_valor = valor
                        mejor_asignacion = asignacion
    return mejor_asignacion

def es_valida(asignacion, B, ofertas):
    for i in range(len(ofertas)):
        if asignacion[i] < ofertas[i][2] or asignacion[i] > ofertas[i][1]:
            return False
    if asignacion[-1] < 0 or asignacion[-1] > B:
        return False
    return True

def calcular_valor(asignacion, ofertas):
    valor = 0
    for i in range(len(ofertas)):
        valor += asignacion[i] * ofertas[i][0]
    valor += asignacion[-1] 
    return valor

print( accionesFB(1000,100, 2, [(500, 600, 100),(450, 800, 400)] ))

