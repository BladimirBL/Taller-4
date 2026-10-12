ventas1 = float(input("Ventas del departamento 1: "))
ventas2 = float(input("Ventas del departamento 2: "))
ventas3 = float(input("Ventas del departamento 3: "))
salario = float(input("Salario mensual de un vendedor: "))

total = ventas1 + ventas2 + ventas3
limite = total * 0.33

if ventas1 > limite:
    pago1 = salario + (salario * 0.20)
else:
    pago1 = salario

if ventas2 > limite:
    pago2 = salario + (salario * 0.20)
else:
    pago2 = salario

if ventas3 > limite:
    pago3 = salario + (salario * 0.20)
else:
    pago3 = salario

print("Ventas totales:", total)
print("Límite (33%):", limite)
print("Pago por vendedor, departamento 1:", pago1)
print("Pago por vendedor, departamento 2:", pago2)
print("Pago por vendedor, departamento 3:", pago3)