def estimular (nivel, promedio):
    costo_pregrado = 50000
    costo_posgrado = 300000
    
    if nivel == "Pregrado" or nivel == "pregrado":
        costo_credito = costo_pregrado
        if promedio >= 4.5:
            print("Por su buen rendimiento academico usted cursara 28 creditos por su pregrado y se le dara un 25% de descuento, el costo total sera de: ", costo_pregrado * 28 - (costo_pregrado * 28 * 0.25))
        elif promedio >= 4.0:
            print("Por su buen rendimiento academico usted cursara 25 creditos por su pregrado y se le dara un 10% de descuento, el costo total sera de: ", costo_pregrado * 25 - (costo_pregrado * 25 * 0.10))
        elif promedio > 3.5:
            print("Usted cursara 20 creditos por su pregrado el costo total sera de: ", costo_pregrado * 20 )
        elif promedio >= 2.5:
            print("Usted cursara 15 creditos por su pregrado el costo total sera de: ", costo_pregrado * 15 )
        elif promedio < 2.5:
            print("Lamentamos mucho este acontesimiento pero usted no podra matricularse por su bajo rendimiento academico")
    elif nivel == "Posgrado" or nivel == "posgrado":
        if promedio >= 4.5:
            print("Por su buen rendimiento academico usted cursara 20 creditos por su posgrado y se le dara un 20% de descuento, el costo total sera de: ", costo_posgrado * 20 - (costo_posgrado * 20 * 0.20))
        else:
            print("Usted cursara 10 creditos por su posgrado el costo total sera de: ", costo_posgrado * 10)


 
llamada = input("Por favor indique su nivel y su promedio(Ejemplo: Posgrado 4.5): ")
nivel, promedio = llamada.split()
promedio = float(promedio)
estimular(nivel, promedio)

