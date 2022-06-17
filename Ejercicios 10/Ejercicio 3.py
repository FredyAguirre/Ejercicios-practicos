def IMC(a):
    L=[]
    for i in range(1,4):
        X=float(a[i])
        L.append(X)
    calculo= round(L[0]/L[1]**2, 1)
    return calculo
E=int(input())
lista=[]
Riesgo=[]
L2 = []
L3 = []
for i in range(E):  
    ciu=input()
    lista = ciu.split(", ")
    L=[]
    for t in range(1,5):
        X=float(lista[t])
        L.append(X)
    B=IMC(lista)
    if B>25 and L[2]>100 and L[3]>150:
        L2.append(B)
        Riesgo.append(lista[0])
        
for i in range(len(Riesgo)):
    F = [Riesgo[i], L2[i]]
    L3.append(F)
L3.sort(key=lambda x: x[1], reverse= True)
r = 1
for e in L3:
    print(r,e[0], e[1])
    r= r+1
