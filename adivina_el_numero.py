from random import *
print("Bueno, Juan, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número")

valor =randint(1, 100)
#print(valor)
user = int(input("Ingresa un numero: "))
contador  = 8

while contador > 0:
    if contador > 1 :
        if user <= 100 and user >= 1:
            if user < valor: 
                print("El numero es incorrecto el valor es mayor")
            elif user > valor:
                print("El numero es incorrecto el valor es menor")
            elif user == valor:
                print("El numero es corecto..FELICITACIONES GANASTE") 
                break
        else:
            print("El valor no esta permitido el rango es entre 1 y 100")
        contador -= 1
        print(f'Queda {contador} intentos')
        user = int(input("Ingresa un numero: "))
    else:
        print("Se acabaron los intentos, perdiste")
        contador-= 1;
    