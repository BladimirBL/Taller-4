def octal(lista_digitos):
    cantidad_numeros = 0
    for digito in lista_digitos:
        cantidad_numeros = cantidad_numeros + 1
    
    if cantidad_numeros < 5 or cantidad_numeros > 5:
        print("Error: El número debe tener exactamente 5 dígitos.")
        return

    for digito in lista_digitos:
        if digito < 0 or digito > 7:
            print("Error: Los dígitos deben estar entre 0 y 7 (el 8 y el 9 no existen).")
            return 

    decimal = (lista_digitos[0] * 4096) + (lista_digitos[1] * 512) + (lista_digitos[2] * 64) + (lista_digitos[3] * 8) + (lista_digitos[4] * 1)
    
    print(f"El valor equivalente en el sistema decimal es: {decimal}")
    return decimal


llamada = input("Introduce un número octal de 5 dígitos (separados por comas, ej: 1,2,3,4,5): ")
ingreso = list(map(int, llamada.split(",")))
resultado = octal(ingreso)


