# Reto 6 clase PDC Unal 2024-1
# -David Montes

A continuación de presentarán las distintas soluciones a los ejercicios del reto 6:
 
# ejercicio 1
Dado la figura de la imagen, desarrolle:
![](https://camo.githubusercontent.com/100b4565370665cb6dc8eeb57a662a10739043ee88c469412805f701539f370b/68747470733a2f2f692e706f7374696d672e63632f465276436d7078782f696d6167652e706e67)
Una función matemática para calcular el volumen y el área superficial.
Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.
Revise como utilizar el valor de pi usando import math y math.pi

```python

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

```
# ejercicio 2
Dado la figura de la imagen, desarrolle:
![](https://camo.githubusercontent.com/1a56c739fc45f64bd5f731f69f70c88c2bdd59840ffe6ad12c41082d76393952/68747470733a2f2f692e706f7374696d672e63632f3174344d727a734c2f696d6167652e706e67)
Una función matemática para calcular el área y el perimetro.
Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b.
Revise como utilizar el valor de pi usando import math y math.pi

```python

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
```
# ejercicio 3

Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

```python
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

```
# ejercicio 4
Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.
```python

Pan=300
Leche=3300
Huevo=350

def vueltas(P:int,M:int,H:int,B:int):
    precio_pan= P*300
    precio_leche=M*3300
    precio_huevos= H*350
    return B - precio_pan - precio_leche - precio_huevos

if __name__ == "__main__":
    P=int(input("introduzca la cantidad de panes que toca comprar:"))
    M=int(input("introduzca la cantidad de bolsas de leche que toca comprar"))
    H=int(input("introduzca la cantidad de huevos que toca comprar"))
    B=int(input("introduzca la cantidad de dinero que le dio su querida mamá para ir a hacer la compra:"))
    vueltas_o_deuda= vueltas(P,M,H,B)
    if (vueltas_o_deuda >= 0):
        print("La cantidad de vueltas que le deben entregar es:", vueltas_o_deuda)
    else:
        print("Usted debe:",-1*(vueltas_o_deuda))
```
# ejercicio 5

Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.
```python
def interés_compuesto(Ci:int,i:float,n:int):
    interes=Ci*((1+i/100)**n)
    return interes

if __name__=="__main__":
    Ci=int(input("Introduzca el valor inicial del préstamo:"))
    i=float(input("Introduzca la tasa de interés del préstamo:"))
    n=int(input("introduzca la cantidad de meses en las que va a pagar el préstamo:"))
    pago_final=interés_compuesto(Ci,i,n)
    print("El pago final que usted hará será de:", pago_final, "tras haber pedido un préstamo de:",Ci)
```

# ejercicio 6
El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

```python
def número_contagiados_d_después(C:int,D:int):
    número_contagiados_posteriores= C*(2**D)
    return número_contagiados_posteriores

if __name__ == "__main__":
    C=int(input("introduzca el número de contagiados de Covid-19 que hay hoy en NuncaLandia:"))
    D=int(input("introduzca el número de días para los que quiere conocer la proyección a futuro:"))
    número_c_final=número_contagiados_d_después(C,D)

    print("el número de contagiados de Covid-19 que habrá en",D,"días es:",número_c_final)
```
# ejercicio 7

Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:

El promedio

La mediana
El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)

Ordenar los números de forma ascendente

Ordenar los números de forma descendente

La potencia del mayor número elevado al menor número

La raíz cúbica del menor número

** Este punto no lo alcancé a acabar antes de la fecha de entrega debido a que fui incapaz de organizar los números correctamente, en el programa que está aquí escrito se encuentra una alternativa poco viable.

```python
def promedio(a:float,b:float,c:float,d:float,e:float):
    prm=(a+b+c+d+e)/5
    return prm
def mediana(a:float,b:float,c:float,d:float,e:float):
    med =1+1
    return med
def promedio_multiplicativo(a:float,b:float,c:float,d:float,e:float): #aquí entiendo que debo sacar la multiplicación de todos los números 
    #y luego calcular la raíz quinta de ese producto, aunque no encontré nada al respecto en internet
    rq=1/5
    multiplic_val=a*b*c*d*e
    return multiplic_val**rq
    
def número_mayor_f(a:float,b:float,c:float,d:float,e:float):
    if ((a>=b and a>=c ) and (a>=d and a>=e )): #aquí no queda de otra que encontrar el número mayor
        número_mayor=a
    elif((b>=a and b>=c ) and (b>=d and b>=e )):
        número_mayor=b
    elif((c>=a and c>=b ) and (c>=d and c>=e )):
        número_mayor=c
    elif((d>=a and d>=b ) and (d>=c and d>=e )):
        número_mayor=d
    elif((e>=a and e>=b ) and (e>=c and e>=d )):
        número_mayor=e
        return número_mayor
def número_menor_f(a:float,b:float,c:float,d:float,e:float):
    if ((a<=b and a<=c ) and (a<=d and a<=e )): #aquí toca encontrar el número menor
        número_menor=a
    elif((b<=a and b<=c ) and (b<=d and b<=e )):
        número_menor=b
    elif((c<=a and c<=b ) and (c<=d and c<=e )):
        número_menor=c
    elif((d<=a and d<=b ) and (d<=c and d<=e )):
        número_menor=d
    elif((e<=a and e<=b ) and (e<=c and e<=d )):
        número_menor=e
        return número_menor
    
def número_mayor_elevado_menor(número_mayor,número_menor):
    if ((a>=b and a>=c ) and (a>=d and a>=e )): #aquí no queda de otra que encontrar el número mayor
        número_mayor=a
    elif((b>=a and b>=c ) and (b>=d and b>=e )):
        número_mayor=b
    elif((c>=a and c>=b ) and (c>=d and c>=e )):
        número_mayor=c
    elif((d>=a and d>=b ) and (d>=c and d>=e )):
        número_mayor=d
    elif((e>=a and e>=b ) and (e>=c and e>=d )):
        número_mayor=e
        return número_mayor
    if ((a<=b and a<=c ) and (a<=d and a<=e )): #aquí toca encontrar el número menor
        número_menor=a
    elif((b<=a and b<=c ) and (b<=d and b<=e )):
        número_menor=b
    elif((c<=a and c<=b ) and (c<=d and c<=e )):
        número_menor=c
    elif((d<=a and d<=b ) and (d<=c and d<=e )):
        número_menor=d
    elif((e<=a and e<=b ) and (e<=c and e<=d )):
        número_menor=e
        return número_mayor**número_menor
    
def raíz_cúbica_menor(a:float,b:float,c:float,d:float,e:float):
    rcu=1/3
    if ((a<=b and a<=c ) and (a<=d and a<=e )): #aquí toca encontrar el número menor
        número_menor=a
    elif((b<=a and b<=c ) and (b<=d and b<=e )):
        número_menor=b
    elif((c<=a and c<=b ) and (c<=d and c<=e )):
        número_menor=c
    elif((d<=a and d<=b ) and (d<=c and d<=e )):
        número_menor=d
    elif((e<=a and e<=b ) and (e<=c and e<=d )):
        número_menor=e
    rcu_me=número_menor**rcu
    return rcu_me

if __name__=="__main__":
    a=float(input("introduzca el primer número:"))
    b=float(input("introduzca el segundo número:"))
    c=float(input("introduzca el tercer número:"))
    d=float(input("introduzca el cuarto número:"))
    e=float(input("introduzca el quinto número:"))
    número_menor=número_menor_f(a,b,c,d,e)
    número_mayor=número_mayor_f(a,b,c,d,e)
    prom=promedio(a,b,c,d,e)
    medi=mediana(a,b,c,d,e)
    prom_mult=promedio_multiplicativo(a,b,c,d,e)
    nma_el_nm=número_mayor_elevado_menor(número_mayor,número_menor)
    r3_me=raíz_cúbica_menor(a,b,c,d,e)

print("el promedio de estos números es:",prom)
print("la mediana de estos números es:",medi)
print("el promedio multiplicativo de estos números es:")
print("estos números ordenados de forma ascendente son:",número_menor,medi,número_mayor)
print("estos números ordenados de forma descendente son:",número_mayor,medi,número_menor)
print("la potencia del número mayor elevado al menor es:",nma_el_nm)
print("la raíz cúbica del menor número es:",r3_me)
```

# ejercicio 8

Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.

```python
# punto 8, alternativa al punto 7
import funciones as f

if __name__=="__main__":
    a=float(input("introduzca el primer número:"))
    b=float(input("introduzca el segundo número:"))
    c=float(input("introduzca el tercer número:"))
    d=float(input("introduzca el cuarto número:"))
    e=float(input("introduzca el quinto número:"))
    número_menor=f.número_menor_f(a,b,c,d,e)
    número_mayor=f.número_mayor_f(a,b,c,d,e)
    prom=f.promedio(a,b,c,d,e)
    medi=f.mediana(a,b,c,d,e)
    prom_mult=f.promedio_multiplicativo(a,b,c,d,e)
    nma_el_nm=f.número_mayor_elevado_menor(número_mayor,número_menor,a,b,c,d,e)
    r3_me=f.raíz_cúbica_menor(a,b,c,d,e)

print("el promedio de estos números es:",prom)
print("la mediana de estos números es:",medi)
print("el promedio multiplicativo de estos números es:")
print("estos números ordenados de forma ascendente son:",número_menor,medi,número_mayor)
print("estos números ordenados de forma descendente son:",número_mayor,medi,número_menor)
print("la potencia del número mayor elevado al menor es:",nma_el_nm)
print("la raíz cúbica del menor número es:",r3_me)
```
# ejercicio 9
Consultar qué es y cómo funciona pip en python.

Solución:

"pip" es un sistema de gestión de paquetes, el cual se encuentra incluido en todas las versiones de python 3; pip permite instalar o desinstalar una gran cantidad de paquetes de python, entre otras acciones.

(según la página de wikipedia sobre pip)

# Ejercicio 10

Hacer un listado de módulos populares para python que se puedan instalar com pip y consultar cómo instalarlos.


Solución:

Gran parte de los módulos de python son instalables a través de pip mediante la escritura del comando ```pip install (nombre del paquete)``` en la consola de windows(si es que se usa windows).

Algunos de los módulos más populares de python son:

- NumPy (#esta no sé si vaya a usarla alguna vez pero la instale cuando volví a instalar python en mi pc)
- SciPy
- SciKit Image
- SimplelTK
- SciKit Learn
- IPython
- NetworKX
- PyGame (con esta una vez intenté hacer un jueguito de una nave espacial siguiendo unos tutoriales de youtube)
- Django
- Ilastik
- Py2Exe
- PyGTK