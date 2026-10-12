entrada = input("Ingrese los cuatro datos separados por coma: ")
a, b, c, d = map(int, entrada.split(","))
 
mayor = a
menor = a
 
if b > mayor:
    mayor = b
if b < menor:
    menor = b
 
if c > mayor:
    mayor = c
if c < menor:
    menor = c
 
if d > mayor:
    mayor = d
if d < menor:
    menor = d
 
suma = mayor + menor
print("El mayor es:", mayor)
print("El menor es:", menor)
print("La suma del mayor y el menor es:", suma)