#el volumen de una esfera es (4/3pi)*r^3

#el volumen de un cono es ((pi*r^2)*h)/3
import math
pi= math.pi
#función para calcular el volumen de la esfera
def vol_esfera(a,pi):
    vol1:float=(a*a*a)*pi*(4/3)
    return vol1
#función para calcular el volumen del cono
def vol_cono(b,c,pi):
    vol2:float= (b**2)*pi*(c/3)
    return vol2
#función para calcular el volumen total
def vol_total(vol1,vol2):
    vol1=vol_esfera(a,pi)
    vol2= vol_cono(b,c,pi)
    return vol1 + vol2

def area_superficial_esfera(a,pi):
    area_e= a*a*4*pi
    return area_e

def area_superficial_cono(b,c,pi):
    #en este momento es necesario hallar la generatriz del cono(distancia desde un punto de la circunferencia de la base hasta el vertice), usando el teorema de pitagoras
    generatriz_cono:float=(b**2+c**2)**(1/2)
    area_c= generatriz_cono*pi*b
    return area_c

def area_superficial_total(area_e,area_c):
    area_e=area_superficial_esfera(a,pi)
    area_c=area_superficial_cono(b,c,pi)
    return area_e + area_c

if __name__ == "__main__":
    a=(float(input("introduzca el radio(r1) de la esfera: ")))
    b=(float(input("introduzca el radio(r2) de la base del cono")))
    c=(float(input("introduzca la altura(h) del cono: ")))
    vol1=vol_esfera(a,pi)
    vol2=vol_cono(b,c,pi)
    vol_t=vol_total(vol1,vol2)
    area_e=area_superficial_esfera(a,pi)
    area_c=area_superficial_cono(b,c,pi)
    area_t=area_superficial_total(area_e,area_c)
    print("el volumen total de la figura es:",vol_t, "y el area total de la superficie de la figura es:",area_t)