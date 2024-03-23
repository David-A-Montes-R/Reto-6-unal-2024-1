def interés_compuesto(Ci:int,i:float,n:int):
    interes=Ci*((1+i/100)**n)
    return interes

if __name__=="__main__":
    Ci=int(input("Introduzca el valor inicial del préstamo:"))
    i=float(input("Introduzca la tasa de interés del préstamo:"))
    n=int(input("introduzca la cantidad de meses en las que va a pagar el préstamo:"))
    pago_final=interés_compuesto(Ci,i,n)
    print("El pago final que usted hará será de:", pago_final, "tras haber pedido un préstamo de:",Ci)