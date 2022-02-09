from xmlrpc.client import Boolean


seguir=True
while(seguir==True):
    num= int(input("Ingrese un numero : " ))
    primo=True
    for n in range(2,num):
        if(num%n==0):
            primo=False
            break

    if(primo==True):
        print(str(num), " es primo ")
    else:
        print(str(num), " no es primo") 
    pregunta= int(input(" Desea continuar: 1-SI, 2-NO : "))
    while(pregunta!= 1 and pregunta!=2):
        pregunta= int(input(" Desea continuar: 1-SI, 2-NO : "))
    if(pregunta==2):
        seguir=False    