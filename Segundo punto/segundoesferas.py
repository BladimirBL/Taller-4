def esfera (esfera_A, esfera_B, esfera_C, esfera_D):
    lado_izquierdo = esfera_A + esfera_B
    print("El lado izquierdo pesa un total de: ", lado_izquierdo)
    lado_derecho = esfera_C + esfera_D
    print("El lado derecho pesa un total de: ", lado_derecho)

    if esfera_A == esfera_B:
        print("El lado izquierdo es equilibrado y cada esfera pesa lo mismo, lo que significa que el lado derecho tiene el peso diferente buscado")
        if esfera_C != esfera_A:
            print("La esfera C es el peso diferente buscado")
            if esfera_C > esfera_A:
                print("La esfera C es más pesada que las demás")
            else:
                print("La esfera C es más ligera que las demás")
        else:
            print("La esfera D es el peso diferente buscado")
            if esfera_D > esfera_A:
                print("La esfera D es más pesada que las demás")
            else:
                print("La esfera D es más ligera que las demás")
    else:
        print("El lado izquierdo no es equilibrado y cada esfera pesa diferente")
        if esfera_A != esfera_C:
            print("La esfera A es el peso diferente buscado")
            if esfera_A > esfera_C:
                print("La esfera A es más pesada que las demás")
            else:
                print("La esfera A es más ligera que las demás")
        else:
            print("La esfera B es el peso diferente buscado")
            if esfera_B > esfera_C:
                print("La esfera B es más pesada que las demás")
            else:
                print("La esfera B es más ligera que las demás")




    
llamada = input("Ingrese el peso de las esferas, tenga en cuenta que 3 de ellas deben ser del mismo peso (por favor escriba el peso de las esferas y dividalas por comas): ")
a, b, c, d = map(int, llamada.split(","))
esfera(a, b, c, d)

