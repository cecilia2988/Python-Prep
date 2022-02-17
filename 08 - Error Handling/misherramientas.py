class Herramientas:
    def __init__(self, lista_numeros):
        if(type(lista_numeros)!=list):
            self.lista=[0]
            raise ValueError("Se debe ingresar una lista de numeros")
        else:   
            self.lista = lista_numeros


    def verifica_primo(self):
        listaprimos=[]
        for i in self.lista:
            if (self.__verifica_primo(i)):
                listaprimos.append(True)
            else:
                listaprimos.append(False)
        return listaprimos      

    def conversion_grados(self, origen, destino):
        parametros=["Celsius", "Fareheint", "Kelvin"]
        if destino not in parametros or origen not in parametros:
            print("Por favor ingresar origen, destino correctamente")
        else:
            for i in self.lista:
                print(i, 'grados', origen, 'son', self.__conversion_grados(i, origen, destino),'grados',destino)
    
    def factorial(self):
        listafactorial=[]
        for i in self.lista:
            listafactorial.append(self.__factorial(i))
        return listafactorial

    def __verifica_primo(self, nro):
        assert type(nro)==int
        es_primo = True
        for i in range(2, nro):
            if nro % i == 0:
                es_primo = False
                break
        return es_primo

    def valor_modal(self, menor):
        lista_unicos = []
        lista_repeticiones = []
        if len(self.lista) == 0:
            return None
        if (menor):
            self.lista.sort()
        else:
            self.lista.sort(reverse=True)
        for elemento in self.lista:
            if elemento in lista_unicos:
                i = lista_unicos.index(elemento)
                lista_repeticiones[i] += 1
            else:
                lista_unicos.append(elemento)
                lista_repeticiones.append(1)
        moda = lista_unicos[0]
        maximo = lista_repeticiones[0]
        for i, elemento in enumerate(lista_unicos):
            if lista_repeticiones[i] > maximo:
                moda = lista_unicos[i]
                maximo = lista_repeticiones[i]
        return moda, maximo

    def __conversion_grados(self, valor, origen, destino):
        valor_destino = None
        if (origen == 'Celsius'):
            if (destino == 'Celsius'):
                valor_destino = valor
            elif (destino == 'Farenheit'):
                valor_destino = (valor * 9 / 5) + 32
            elif (destino == 'Kelvin'):
                valor_destino = valor + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'Farenheit'):
            if (destino == 'Celsius'):
                valor_destino = (valor - 32) * 5 / 9
            elif (destino == 'Farenheit'):
                valor_destino = valor
            elif (destino == 'Kelvin'):
                valor_destino = ((valor - 32) * 5 / 9) + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'Kelvin'):
            if (destino == 'Celsius'):
                valor_destino = valor - 273.15
            elif (destino == 'Farenheit'):
                valor_destino = ((valor - 273.15) * 9 / 5) + 32
            elif (destino == 'Kelvin'):
                valor_destino = valor
            else:
                print('Parámetro de Destino incorrecto')
        else:
            print('Parámetro de Origen incorrecto')
        return valor_destino

    def __factorial(self, numero):
        assert type(numero) == int, 'El numero debe ser un entero'
        assert numero >= 0, 'El numero debe ser pisitivo'
        if (numero > 1):
            numero = numero * self.__factorial(numero - 1)
        return numero