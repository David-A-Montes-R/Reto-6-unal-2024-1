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
    
def número_mayor_elevado_menor(número_mayor,número_menor,a,b,c,d,e):
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