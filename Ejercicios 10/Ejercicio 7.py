N=int(input())
puntos={}
l = []
mayor = 0
for i in range(N):
    M=input()
    mensaje = M.split(": ")
    if mensaje[0] not in puntos:
        puntos[mensaje[0]] = mensaje[1]
    else:
        puntos[mensaje[0]] = int(puntos[mensaje[0]]) + int(mensaje[1])
        if puntos[mensaje[0]] > mayor:
            mayor = (puntos[mensaje[0]])
            X = (mensaje[0],mayor)
print("El vendedor del mes es", X[0])





