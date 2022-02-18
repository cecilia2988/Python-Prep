import os

def run():

    montañas={
        "nombre":["k1","k2","k3","k4","k5","k6"],
        "orden":[1,2,3,4,5,6],
        "cordillera":["c1","c2","c3","c4","c5","c6"],
        "pais":["p1","p2","p3","p4","p5","p6"],
        "altura":[100,200,300,400,500,600]

    }
    with open("Montañas.csv","w") as f:
        for llave in montañas.keys():
            if(llave=="altura"):
                f.write("\n")
            else:
                f.write(llave + ",")

        cantidad_elementos =len(montañas["altura"])
        i=0

        while(i<cantidad_elementos):
            f.write(montañas["nombre"][i] + ",")
            f.write(str(montañas["orden"][i]) + ",")
            f.write(montañas["cordillera"][i] + ",")
            f.write(montañas["pais"][i] + ",")
            f.write(str(montañas["altura"][i]))
            f.write("\n")
            i+=1






if __name__=='__main__':
    run()