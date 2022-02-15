# 1) Crear una función que reciba un número como parámetro y devuelva si True si 
# es primo y False si no lo es

from glob import iglob


def PedirNumero():
    validar=False
    while(validar==False):
        num=int(input("Ingrese un numero: " ))
        if(num>0):
            validar=True

    return num


def Esprimo(numero):
    primo=True
    for i in range(2,numero-1):
        if(numero%i==0):
            primo=False
            break
    return primo    

def run():
    num= PedirNumero()
    print(str(Esprimo(num)))
    




if __name__ == '__main__':
    run()
