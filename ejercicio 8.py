# punto 8
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