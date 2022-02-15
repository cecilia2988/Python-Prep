# 6) Iterando una lista con los tres valores posibles de temperatura
#  que recibe la función del punto 5, hacer un print para cada combinación de los mismos:


from cProfile import run


def calcularconversion(tipo,ngrados,convertir):
    conversion=0
    if (tipo=="Celcius"):
        conversion=convertirCelcius(ngrados,convertir)
    if (tipo=="Fareheint"):
        conversion=convertirFareheint(ngrados,convertir)
    if (tipo=="Kelvin"):
        conversion=convertirKelvin(ngrados,convertir)    
    return conversion


def convertirCelcius(ng,destino):
    d=0
    if(destino=="Celcius"):
        d=ng
    else:
        if(destino=="Fareheint"):
            d=(ng* 9/5) + 32
            
        else:
            destino=ng + 273.15
    return d           



def convertirFareheint(ng,destino):
    d=0
    if(destino=="Fareheint"):
       d=ng
    else:
        if(destino=="Celcius"):
            d=(ng-32 )/(9/5)
        else:
            d=(ng-32) *5/9+273.15  
    return d       



def convertirKelvin(ng,destino):
    d=0
    if(destino=="Kelvin"):
        d =ng
    else:
        if(destino=="Celcius"):
            d= ng-273.15        
        else:
            d= (ng-273.15)* 9/5 +32
    return d  


def Iterarlista(lista):
    for i in range(0,3):
        for j in range(0,3):
            print(" 1 grado de ", lista[i], " es ", calcularconversion(lista[i],1,lista[j]), "de ", lista[j])
           





def run():
    listatiposgrados=["Celcius","Fareheint","Kelvin"]
    Iterarlista(listatiposgrados)
     




if __name__=='__main__': 
    run()