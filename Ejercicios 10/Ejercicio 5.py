def bandera(n):
    L = []
    g = n
    l = n
    if n%2!=0:
        for i in range(n//2):
            X = ('0' * i + '#' + '0' * ((l-3)//2) +"+"+'0' * ((l-3)//2)+ '#' + '0' *i)
            L.append(X)
            l = l - 2
        X = ('+'*(n//2)+'#'+'+'*(n//2))
        L.append(X)
        co = (n//2) -1
        g = 0
        for a in range(n//2):
            if n%2!=0:
                X = ('0'*co+'#'+'0'*(g)+"+"+ '0' * g + '#'+'0'*co)
                co = co - 1
                g = g + 1
                L.append(X)
        return L

N = int(input())
for i in range(N):
    L2 = []
    X = int(input())
    for o in range(X):
        F = input()
        L2.append(F)
    defi = bandera(X)
    if L2 == defi:
        print("Bandera britanica")
    else:
        print("Ni idea")
