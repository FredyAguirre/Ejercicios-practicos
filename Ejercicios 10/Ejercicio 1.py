encuesta=[]
encuestaM=[]
N= int(input())
for i in range(N):
    ciuda=input()
    a= ciuda.split()
    a[3]=int (a[3])
    a[1]=int (a[1])
    encuesta.append(a)
for fil in encuesta:
    if fil[2]=="positiva":
        fil[2]=fil[2].upper()
        encuestaM.append(fil)

encuestaM.sort(key=lambda x: (x[3],x[1]), reverse=True)
for e in encuestaM:
    print(e[1],e[2],e[3])
