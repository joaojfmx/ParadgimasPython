
a = float(input("Primeiro numero:"))
b = float(input("Segundo numero:"))
c = float(input("Terceiro numero:"))

if a<b and a<c:
    if b<c:
        print(a,b,c)
    else:
        print(a,c,b)
elif b<c:
    if a<c:
        print(b,a,c)
    else:
        print(b,c,a)
else:
    if a<b:
        print(c,a,b)
    else:
        print(c,b,a)
    

