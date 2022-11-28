def devolver_distintos(val1:int,val2:int,val3:int):
    arr = [val1,val2,val3]
    arr.sort()
    if sum(arr) > 15:
        return (f'{max(arr)}')
    elif sum(arr) < 10:
        return (f'{min(arr)}')
    return (f'{arr.pop(1)}')
    
distinto = devolver_distintos(7,4,6) 
print(distinto)


def nombre(texto):
    arr = list(set((texto.lower())))
    arr.sort()
    return print(arr)

nomb = nombre("entretenido")
print(nomb)


def repetidos(*args):
    acc = 0;
    for i in args:
        if i == 0:
            acc +=1
    if acc == 2:
        return True
    return False

rep = repetidos(1,2,3)
print(rep)

def ceros_vecinos(*args):
    contador = 0
    for i in args:
        if contador + 1 == len(args):
            return False
        if args[contador] == 0 and args[contador + 1] == 0:
            return True
        else:
            contador +=1
    return False

veci =ceros_vecinos(0,1,2,4,0,0)
print(veci)


def contar_primos(num):
    count = 0
    for i in list(range(2, num)):
        if i % 2 != 0:
            print(i)
            count += 1
    return f'El total de numero primos es {count}'

primo = contar_primos(50)
print(primo)
