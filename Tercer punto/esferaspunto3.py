def esfera (esfera_A, esfera_B, esfera_C):
    if esfera_A > esfera_B and esfera_A > esfera_C:
        print("Esfera A es la mayor de todas las esferas y su valor es:", esfera_A)
    elif esfera_B > esfera_A and esfera_B > esfera_C:
        print("Esfera B es la mayor de todas las esferas y su valor es:", esfera_B)
    else:
        print("Esfera C es la mayor de todas las esferas y su valor es:", esfera_C)

        

        
    
llamada = input("Ingrese el peso de las esferas( por favor divida el peso de las esferas por comas): ")
a, b, c = map(int, llamada.split(","))
esfera(a, b, c)

