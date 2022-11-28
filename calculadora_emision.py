nombre  = input('Ingrese su Nombre: ')
ventas = float(input("Ingrese monto vendido: "))

comision = round(ventas * 0.13)
print(f'{nombre} tu monto correspondiente por comision es: ${comision}')
