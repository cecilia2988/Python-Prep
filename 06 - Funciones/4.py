#4) A la función del punto 3, agregar un parámetro más, que permita elegir
# si se requiere el menor o el mayor de los mas repetidos.

def ListaUnicos(milista):
    sinrepetir=[]
    for elem in milista:
        if(elem not in sinrepetir):
            sinrepetir.append(elem)
    return sinrepetir        


def Maximo(Listaprincipal, Listaunicos):
    elemento=Listaunicos[0]
    mimaximo=Listaprincipal.count(elemento)
    for n in Listaunicos:
        if Listaprincipal.count(n)>=mimaximo:
            mimaximo=Listaprincipal.count(n)
    print("El elemento mayor elemento con mayor cantidad de repeticiones es ", elemento)
    print("Aparece ", mimaximo ,  "veces")


     

# def Minimo(Listaprincipal, Listaunicos):
#     elementominimo=Listaunicos[0]
#     miminimo=Listaprincipal.count(elementominimo)
#     for n in Listaunicos:
#         if Listaprincipal.count(n)<miminimo:
#             miminimo=Listaprincipal.count(n)
#             elementominimo=n
#     print("El elemento con menor cantidad de repeticiones es ", elementominimo)
#     print("Aparece ", miminimo ,  "veces")
     


def run():
    lista=[1,3,4,6,2,4,7,8,8,6,3,4,5,9,1,1,1,4,5,5,6,7,7,8,1,1]
    listasinrepetir=ListaUnicos(lista.copy())
    Maximo(lista,listasinrepetir)
    # Minimo(lista,listasinrepetir)



if __name__=='__main__':
    run()