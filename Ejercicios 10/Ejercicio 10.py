N = int(input())
for i in range(1, N+1):
    tabla = []
    caso = input()
    x1 = input()
    x2 = input()
    x3 = input()
    x4 = input()
    x1 = x1.split()
    x2 = x2.split()
    x3 = x3.split()
    x4 = x4.split()
    tabla.append(x1)
    tabla.append(x2)
    tabla.append(x3)
    tabla.append(x4)
    for o in range(4):
        x1[o] = int(x1[o])
        x2[o] = int(x2[o])
        x3[o] = int(x3[o])
        x4[o] = int(x4[o])
    suma = 0
    suma2 = 0
    suma3 = 0
    suma4 = 0
    a = sum(x1)
    a2 = sum(x2)
    a3 = sum(x3)
    a4 = sum(x4)
    for e in tabla:
        suma = suma + e[0]
        suma2 = suma2 + e[1]
        suma3 = suma3 + e[2]
        suma4 = suma4 + e[3]
    diag1 = tabla[0][3] + tabla[1][2] + tabla[2][1] + tabla[3][0]
    diag2 = tabla[0][0] + tabla[1][1] + tabla[2][2] + tabla[3][3]
    if a == a2 and a == a3 and a==a4 and suma == suma2 and suma == suma3 and suma == suma4 and diag1 == diag2 and diag1 == a and diag1 == suma:
        print("Cuadrado magico")
    else:
        print("Cuadrado muggle")

