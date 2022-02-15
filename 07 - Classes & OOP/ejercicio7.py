# 7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual
#  se aplquen las funciones incorporadas


class MisFunciones:
    lista= list

    def __init__(self, list) -> None:
        self.lista=list

    def VEsprimo(self,numero):
        primo=True
        for i in range(2,numero-1):
            if(numero%i==0):
                primo=False
                break
        return primo  


    def Esprimo(self):
        for z in self.lista:
            if(self.VEsprimo(z)==True):
                print("Es primo ",z)
            else:
                print("No es primo ",z)    


    def fac(self):
        f=0
        for j in self.lista:
            f=self.Vfac(j)
            print("El factorial de ", j, " es ", f)



    def Vcalcularconversion(self,tipo,ngrados,convertir):
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



    def Vfac(self, minum):
        if(minum>1):
            minum=minum*self.Vfac(minum-1)

        return minum
