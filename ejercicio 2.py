# se tiene que el área de un círculo es pi* radio^2 y que el area de un rectangulo es base*altura
import math
pi= math.pi
def area_rectangulo(a:float,b:float):
    Ar=a*b
    return Ar
def area_circulo_1(r1:float,pi):
    Ac1=(r1**2)*pi
    return Ac1
def area_circulo_2(r2:float,pi):
    Ac2= (r2**2)*pi
    return Ac2
def area_total(Ar:float,Ac1:float,Ac2:float):
    At= Ar+Ac1+Ac2
    return At
if __name__ =="__main__":
    a=(float(input("por favor introduzca la base del rectángulo:")))
    b=(float(input("por favor introduzca la altura del rectángulo:")))
    r1=(float(input("introduzca el radio del círculo 1:")))
    r2=(float(input("introduzca el radio del círculo 2:")))
    Ar=area_rectangulo(a,b)
    Ac1=area_circulo_1(r1,pi)
    Ac2=area_circulo_2(r2,pi)
    At=area_total(Ar,Ac1,Ac2)
    print("el area total de la figua es:",At,"(el area del rectángulo es",Ar,"el área del círculo 1 es:",Ac1,"el área del círculo 2 es:",Ac2,")")