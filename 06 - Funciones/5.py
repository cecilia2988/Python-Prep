#5) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F<br>
# Fórmula 2	: °C + 273.15 = °K<br>
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino


def calcularconversion(tipo,ngrados,convertir):
    conversion=0
    if (tipo==1):
        conversion=convertirCelcius(ngrados,convertir)
    if (tipo==2):
        conversion=convertirFarenheit(ngrados,convertir)
    if (tipo==3):
        conversion=convertirKelvin(ngrados,convertir)    
    return conversion


def convertirCelcius(ng,destino):
    destino=0
    if(destino==1):
        destino=ng
    else:
        if(destino==2):
            destino=(ng* 9/5) + 32
            
        else:
            destino=ng + 273.15
    return destino           



def convertirFarenheit(ng,destino):
    destino=0
    if(destino==2):
       destino=ng
    else:
        if(destino==1):
            destino=(ng-32 )/(9/5)
        else:
            destino=(ng-32) *5/9+273.15  
    return destino        

def convertirKelvin(ng,destino):
    destino=0
    if(destino==3):
        destino =ng
    else:
        if(destino==1):
            destino= ng-273.15        
        else:
            destino= (ng-273.15)* 9/5 +32
    return destino        


        

# def IngresoTGrados():
#     validar=False
#     while(validar==False):
#         t=int(input("Ingrese tipo de grado 1-Celsius,2-Farenhet, 3 Kelvin : "))
#         if(t==1 or t==2 or t==3):
#             validar=True
#     return t

def IngresoGrados():
        misgrados= int(input("Ingrese los grados a convertir "))
        return misgrados

              

def run():
   
    # Tgrados=IngresoTGrados()
    
    g=IngresoGrados()
    
    # print("A que quiere convertir: ? ")
    # destino=IngresoTGrados()
    # calcularconversion(Tgrados,g,destino)
    print("Grados Celcius: ", g, " son ", calcularconversion(1,g,2), " Grados Fareheint")
    print("Grados Celcius: ", g, " son ", calcularconversion(1,g,3), " Grados Kelvin")
    print("Grados Fareheint: ", g, " son ", calcularconversion(2,g,1), " Grados Celcius")
    print("Grados Fareheint: ", g, " son ", calcularconversion(2,g,3), " Grados Kelvin")
    print("Grados Kelvin: ", g, " son ", calcularconversion(3,g,1), " Grados Celcius")
    print("Grados Kelvin: ", g, " son ", calcularconversion(3,g,2), " Grados Fareheint")





if __name__=='__main__':
    run()