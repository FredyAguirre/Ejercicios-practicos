archivo = open('frase.txt','r')
frecs ={} #igual a frecs = dict{}
for renglon in archivo:
    listaPalabras = renglon.split()
    for palabra in listaPalabras:
        palabra = palabra.lower()
        for letra in palabra:
            if letra not in frecs:
                frecs[letra] = 1
            else:
                frecs[letra] = frecs[letra] + 1
for i in frecs:
    print(i, ':', frecs[i], end='\t')
archivo.close()
