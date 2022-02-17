from operator import truediv
from pickle import FALSE


def prepararlista(lista):
    listafinal=[]
    cantidad=[]
    listadevolver=[]
    for elemento in lista:
        if(elemento not in listafinal):
            listafinal.append(elemento)
            cantidad.append(lista.count(elemento))
    listadevolver=zip(listafinal,cantidad)
    return list(listadevolver)

def factorizar(num):
    i=2
    lista_divisores=[]
    mismodivisor=True
    while(i<=num):
        while(mismodivisor):
            if num%i==0:
                lista_divisores.append(i)
                num=num/i
                mismodivisor = False
            else:
                i += 1
        i = 2
        mismodivisor = True
    return prepararlista(lista_divisores)
            




def run():
    bandera=False
    while(bandera==False):
        num= (input("Ingrese numero: "))
        try:
            assert num.isnumeric()
            assert type(num)!= int
            print(factorizar(int(num)))
            bandera=True
        except AssertionError:
            print("Debes ingresar un numero entero: ")    
    
    


if __name__=='__main__':
    run()