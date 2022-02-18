def run():
    cadena="Hola esta es una cadena"
    palabra=""
    lista_de_palabras=[]
    largocadena=len(cadena)
    for i in range (0,largocadena):
        if(cadena[i].isspace()) :
            lista_de_palabras.append(palabra)
            palabra=""
        elif (i==len(cadena)-1):
                palabra=palabra+cadena[i] 
                lista_de_palabras.append(palabra) 
        else:
            palabra=palabra+cadena[i]  
    
    print(lista_de_palabras)
    lista_de_palabras.sort(key=len,reverse=True)
    print(lista_de_palabras)


if __name__=='__main__':
    run()