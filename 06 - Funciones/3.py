#3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuánt
# as veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera

from cmath import sin


# def Maximo(listacantidad):
#     max=0
#     for i in listacantidad:
#         if(i>=max):
#             max=i
#     return max


def ListaUnicos(milista):
    sinrepetir=[]
    for elem in milista:
        if(elem not in sinrepetir):
            sinrepetir.append(elem)
    return sinrepetir        


def Cantidad(Listaprincipal, Listaunicos):
    elementomaximo=Listaunicos[0]
    maximo=Listaprincipal.count(elementomaximo)
    for n in Listaunicos:
        if Listaprincipal.count(n)>maximo:
            maximo=Listaprincipal.count(n)
            elementomaximo=n
    print("El elemento con mayor cantidad de repeticiones es ", elementomaximo)
    print("Aparece ", maximo ,  "veces")
     



def run():
    lista=[1,3,4,6,2,4,7,8,8,6,3,4,5,9,1,1,1,4,5,5,6,7,7,8,1,1]
    listasinrepetir=ListaUnicos(lista.copy())
    Cantidad(lista,listasinrepetir)



if __name__=='__main__':
    run()