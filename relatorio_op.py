e =0 
b =0
r =0
for h in range(0,50):
    input('qual é seu nome? ')
    int (input('qual é a sua idade? '))
    a= input(' qual é o nivel do atendimento pretado: (coloque: excelente(e), bom(b), ruim(r)) ')
    if a== "e":
        e = e+1
    elif a== "b":
        b=b+1
    elif a== "r":
        r=r+1
    else:
        print('não teve respostas validas!')
print("as avaliações foram:\n {} excelentes\n {} bom\n {} ruim".format(e,b,r))            
