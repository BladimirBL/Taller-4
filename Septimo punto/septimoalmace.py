def descuento (compras):
    escritorio = 800000
    if compras < 5:
        print("Su compra tiene un 10% de descuento, usted pagara un total de: ", escritorio * compras - (escritorio * compras*0.10))
    elif compras >= 5 and compras < 10:
        print("Su compra tiene un 20% de descuento, usted pagara un total de: ", escritorio * compras - (escritorio * compras*0.20))
    else:
        print("su compra tiene un 40% de descuento, usted pagara un total de: ", escritorio * compras - (escritorio * compras*0.40))
    return

llamada = int(input("Por favor indique cuantos escritorios compro"))
tota = descuento(llamada)






