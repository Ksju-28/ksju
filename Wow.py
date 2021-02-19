a=int(input("write first number"))
b=int(input("write second number"))
c=int(input("write third number"))

if a>b:
    if a>c:
        print(a)
    else:
        print(c)
else:
    if b>c:
        print(b)
    else:
        print(c)