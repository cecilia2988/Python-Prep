#2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una
#  lista de números y devuelva sólo aquellos que son primos en otra lista


from glob import iglob

def ListaPrimos(milista):
    lprimos=[]
    for elemento in milista:
        if(Esprimo(elemento)):
            lprimos.append(elemento)
    return lprimos

def MostrarLista(lista):
    for e in lista:
        print(e)


def Esprimo(numero):
    primo=True
    for i in range(2,numero-1):
        if(numero%i==0):
            primo=False
            break
    return primo    

def run():
    lista1=[3,7,34,9,29,87,101,13,11,23,27]
    lista2=ListaPrimos(lista1.copy())
    print("Lista normal")
    MostrarLista(lista1)
    print("Lista primos")
    MostrarLista(lista2)
    
    

    




if __name__ == '__main__':
    run()
