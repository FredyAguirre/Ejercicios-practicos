def promedio(a):
    L = []
    for i in range(0,13):
        X = int(a[i])
        L.append(X)
    pr = round((L[1]/9)*5, 1) + round((L[2]/11)*5, 1) + round((L[3]/12)*5, 1) + round((L[4]/8)*5, 1) + round((L[5]/12)*5, 1) + round((L[6]/9)*5, 1) + round((L[7]/11)*5, 1) + round((L[8]/8)*5, 1) + round((L[9]/11)*5, 1) + round((L[10]/10)*5, 1) + round((L[11]/9)*5, 1) + round((L[12]/10)*5, 1)
    return pr
N= int(input())
notafinal = 0
listainicial=[]
L2 = []
for i in range(N):
    est= input()
    listainicial= est.split(", ")
    notafinal = round(promedio(listainicial)/12, 1)
    F = [listainicial[0],notafinal]
    L2.append(F)
L2.sort(key=lambda x: x[0])
for e in L2:
    print(e[0], e[1])
