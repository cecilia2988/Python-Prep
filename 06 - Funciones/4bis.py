def ListaUnicos(milista):
    sinrepetir=[]
    for elem in milista:
        if(elem not in sinrepetir):
            sinrepetir.append(elem)
    return sinrepetir        


def cantidad(milista):
    maximo=0
    listasinrepetir=ListaUnicos(milista.copy())
    for elemento in listasinrepetir:
        if(milista.count(elemento)>maximo):
            maximo=milista.count(elemento)
    return maximo

def funcionmayormenor(milista,cantidad,menor):
    valor=milista[0]
    if(menor==True):
        for n in milista:
            if(milista.count(n)==cantidad):
                if(n<valor):
                    valor=n
    else:
         for n in milista:
            if(milista.count(n)==cantidad):
                if(n>valor):
                    valor=n
    return valor

def run():
    lista=[1,5,6,7,3,6,2,2,1,5,8,8,4,6,7,3,5,7,7,9,1,1,1,7]
    mayorrepeticiones=cantidad(lista.copy())
    mayoromenor=funcionmayormenor(lista.copy(),mayorrepeticiones,False)
    print("El numero con mayor repeticiones es: ", mayoromenor, "con ", mayorrepeticiones, "repeticiones")



if __name__=='__main__':
    run()