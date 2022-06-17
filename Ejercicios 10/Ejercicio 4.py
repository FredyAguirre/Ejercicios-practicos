N = int(input())
L = []
L3 = {}
for i in range(N):
    X = input()
    sep = X.split(" ")
    L3[sep[0]] = sep[1]
F = int(input())
for i in range(F):
    X2 = input()
    L.append(X2)
for i in range(F):
    if L[i] in L3:
        print(L3[L[i]])
    else:
        print("palabra no encontrada")
