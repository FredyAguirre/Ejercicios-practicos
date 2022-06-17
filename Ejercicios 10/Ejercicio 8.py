meses = {'marzo':3,'abril':4,'mayo':5,'junio':6,'julio':7,'agosto':8,'septiembre':9,'octubre':10,'noviembre':11,'diciembre':12,'enero':13,'febrero':14}
def dia(x):
    f = meses[x[1]]
    d = int(x[0])
    y = int(x[2])
    if meses[x[1]]==13 or meses[x[1]]==14:
        y=y-1
    formu=(d+13*(f+1)//5)+y
    formu=(((formu+y//4)-y//100)+y//400)
    formu=(formu%7)
    if formu<1:
        return ("sabado")
    elif formu<2:
        return ("domingo")
    elif formu<3:
        return ("lunes")
    elif formu<4:
        return ("martes")
    elif formu<5:
        return ("miercoles")
    elif formu<6:
        return ("jueves")
    elif formu<7:
        return ("viernes")  
n = int(input())
for i in range(n):
    f = input()
    se = f.split('-')
    se[0] = int(se[0])
    se[2] = int(se[2])
    print(dia(se))

