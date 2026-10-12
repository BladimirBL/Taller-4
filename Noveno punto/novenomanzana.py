def descuento (compras):
    manzana = 2000
    if compras <= 2:
        print("Su compra tiene un 0% de descuento, usted pagara un total de: ", manzana * compras)
    elif compras >= 3 and compras <= 5:
        print("Su compra tiene un 10% de descuento, usted pagara un total de: ", manzana * compras - (manzana * compras * 0.10))
    elif compras >= 6 and compras <= 10:
        print("su compra tiene un 15% de descuento, usted pagara un total de: ", manzana * compras - (manzana * compras *0.15))
    else:
        print("su compra tiene un 20% de descuento, usted pagara un total de: ", manzana * compras - (manzana * compras *0.20))
        return

llamada = int(input("Por favor indique cuantos manzanas compro"))
tota = descuento(llamada)