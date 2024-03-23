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