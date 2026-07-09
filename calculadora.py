start=int(input('Olá, qual conta vc gostaria de fazer?\n 1.soma\n2.subtração\n3.multiplicação\n4.divisão'))
def soma():
    n1=int(input('digite um número:'))
    n2=int(input('digite outro número'))
    res=n1+n2
    print(res)

def subtração():
    n1=int(input('digite um número:'))
    n2=int(input('digite outro número'))
    res=n1-n2
    print(res)

def divisão():
    n1=int(input('digite um número:'))
    n2=int(input('digite outro número'))
    res=n1/n2
    print(res)

def mult():
    n1=int(input('digite um número:'))
    n2=int(input('digite outro número'))
    res=n1*n2
    print(res)
if start==1:
    soma()
elif start==2:
    subtração()
elif start==3:
    mult()
else:
    divisão()