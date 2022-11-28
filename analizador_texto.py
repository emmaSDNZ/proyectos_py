
arr = []
texto = input('Ingrese un texto : ')
a = input('Ingrese un palabra : ')
b = input('Ingrese un palabra : ')
c = input('Ingrese un palabra : ')
textLowe = texto.lower()

arr.append(a)
arr.append(b)
arr.append(c)

#ejercicio 1
dicc = {
    texto.find(arr[0]) : texto.count(a),
    texto.find(arr[1]) : texto.count(b),
    texto.find(arr[2]) : texto.count(c)
}

print(dicc)

#ejercicio 2
value = len(texto.split())
print(f'El texto tiene {value} cantidad de palabras')

#ejercicio 3
print(f'La primer letra del texto es {texto[0:1].upper()}')
print(f'La ultima letra del texto es {texto[-1].upper()}')

#ejercicio 4
lista = texto.split()
lista.reverse()
text_invertido = ' '.join(lista)
print(text_invertido)

#ejercicio 5
buscar = 'python' in texto

dicc2 = {
    True: "SI",
    False: "No"
}

print(f'La palabra Python: {dicc2[buscar]} se encuentra')