Gallina=6
Gallo=7
pollito=1

def suma_de_animales(a:int,b:int,c:int):
    suma_gallinas=a*Gallina
    suma_gallos=b*Gallo
    suma_pollitos=c*pollito
    suma_todo=suma_gallinas + suma_gallos + suma_pollitos
    return suma_todo
if __name__ == "__main__":
    a=(int(input("Introduzca el número de gallinas:")))
    b=(int(input("Introduzca el número de gallos:")))
    c=(int(input("Introduzca el número de pollitos:")))
    total_carne=suma_de_animales(a,b,c)
    print("la cantidad total de carne de aves en kilos es:",total_carne)