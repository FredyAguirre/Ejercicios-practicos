def morse(x):
    t=len(x)
    taco=""
    for q in range(t):
        if x[q]=="a":
            taco+=".-"
        elif x[q]=="b":
            taco+="-..."
        elif x[q]=="c":
            taco+="-.-."
        elif x[q]=="d":
            taco+="-.."
        elif x[q]=="e":
            taco+="."
        elif x[q]=="f":
            taco+="..-."
        elif x[q]=="g":
            taco+="--."
        elif x[q]=="h":
            taco+="...."
        elif x[q]=="i":
            taco+=".."
        elif x[q]=="j":
            taco+=".---"
        elif x[q]=="k":
            taco+="-.-"
        elif x[q]=="l":
            taco+=".-.."
        elif x[q]=="m":
            taco+="--"
        elif x[q]=="n":
            taco+="-."
        elif x[q]=="o":
            taco+="---"
        elif x[q]=="p":
            taco+=".--."
        elif x[q]=="q":
            taco+="--.-"
        elif x[q]=="r":
            taco+=".-."
        elif x[q]=="s":
            taco+="..."
        elif x[q]=="t":
            taco+="-"
        elif x[q]=="u":
            taco+="..-"
        elif x[q]=="v":
            taco+="...-"
        elif x[q]=="w":
            taco+=".--"
        elif x[q]=="x":
            taco+="-..-"
        elif x[q]=="y":
            taco+="-.--"
        elif x[q]=="z":
            taco+="--.."
        elif x[q]==".":
            taco+=".-.-.-"
        elif x[q]==",":
            taco+="-.-.--"
        elif x[q]==" ":
            taco+="/"
        taco+=" "
    return taco 


ca=int(input())
lo=[]
for i in range(ca):
    ff=input()
    ff=ff.lower()
    li=[]
    for car in ff:
        li.append(car)
    lo.append(li)
for e in range(ca):
    print(morse(lo[e]))
    print()
