def dif(x,li):
    y=len(x)
    for i in range(y):
        if x[i]not in li:
            li.append(x[i])
    return(li)
ca=int(input())
li=[]
for e in range(ca):
    ff=input()
    na=ff.split(" ")
    li.append(dif(na,li))
de=int(input())
lo=[]
for e in range(de):
    fo=input()
    ne=fo.split(" ")
    lo.append(dif(ne,lo))
print("Reggaeton:",len(li)-ca,"Rock:",(len(lo)-de))
