def esfera (a, b, c, d):
    if a > b and a > c and a > d:
        print("El mayor es a con valor de: ", a)
    elif b > a and b > c and b > d:
        print("El mayor es b con valor de: ", b)
    elif c > a and c > b and c > d:
        print("El mayor es c con valor de :", c)
    else:
        print("El mayor es d con valor de: ", d)
     
    

        

    
llamada = input("Ingrese los cuatro datos separados por comas: ")
a, b, c, d = map(int, llamada.split(","))
esfera(a, b, c, d)