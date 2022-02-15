# 5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 6<br>
# Verificar Primo<br>
# Valor modal<br>
# Conversión grados<br>
# Factorial<br>

class MisFunciones:
    def __init__(self) -> None:
        pass
    

    def Esprimo(self,numero):
        primo=True
        for i in range(2,numero-1):
            if(numero%i==0):
                primo=False
                break
        return primo  



    def calcularconversion(self,tipo,ngrados,convertir):
        conversion=0
        if (tipo=="Celcius"):
            conversion=self.convertirCelcius(ngrados,convertir)
        if (tipo=="Fareheint"):
            conversion=self.convertirFareheint(ngrados,convertir)
        if (tipo=="Kelvin"):
            conversion=self.convertirKelvin(ngrados,convertir)    
        return conversion
    


    def convertirCelcius(self,ng,destino):
        d=0
        if(destino=="Celcius"):
            d=ng
        else:
            if(destino=="Fareheint"):
                d=(ng* 9/5) + 32
            
            else:
                d=ng + 273.15
        return d           



    def convertirFareheint(self,ng,destino):
        d=0
        if(destino=="Fareheint"):
            d=ng
        else:
            if(destino=="Celcius"):
                d=(ng-32 )/(9/5)
            else:
                d=(ng-32) *5/9+273.15  
        return d       



    def convertirKelvin(self,ng,destino):
        d=0
        if(destino=="Kelvin"):
            d =ng
        else:
            if(destino=="Celcius"):
                d= ng-273.15        
            else:
                d= (ng-273.15)* 9/5 +32
        return d        





    def fac(self,minum):
        if(minum>1):
            minum=minum*self.fac(minum-1)
        return minum
