def número_contagiados_d_después(C:int,D:int):
    número_contagiados_posteriores= C*(2**D)
    return número_contagiados_posteriores

if __name__ == "__main__":
    C=int(input("introduzca el número de contagiados de Covid-19 que hay hoy en NuncaLandia:"))
    D=int(input("introduzca el número de días para los que quiere conocer la proyección a futuro:"))
    número_c_final=número_contagiados_d_después(C,D)

    print("el número de contagiados de Covid-19 que habrá en",D,"días es:",número_c_final)