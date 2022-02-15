# 7) Armar una función que devuelva el factorial de un número. 
# Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo

from pickle import TRUE


def IngresoNumero():
    validar=False
    while(validar==False):
        n=int(input("Ingrese un numero mayor a 0: "))
        if(n>0):
            validar=TRUE
    return n


def fac(minum):
    if(minum>1):
        minum=minum*fac(minum-1)
    return minum



def run():
    num= IngresoNumero()
    n=fac(num)
    print("Factorial de ",num, " es " ,n)



if __name__=='__main__':
    run()