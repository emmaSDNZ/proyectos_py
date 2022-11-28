from random import *
def palabra_azar():
    arr = ['lentes']
    #'media', 'dado', 'goma','elefante',
    return arr

def guiones():
    palabra = list (choice(palabra_azar()))
    arr = []
   
    for i in palabra:
        arr.append('_')
    return arr, palabra


def letra():

    result = guiones()
    vida = 6
    arr = []
    while vida >= 0:

        val = input("ingresa una letra: ").lower()
        if val in result[1]:
            indice = result[1].index(val)
            letra  = result[1].pop(indice)
            arr.insert(indice,letra)
            print(arr)
            print(result[0])
        else:
            vida -= 1
            print(f'{val} no esta en la palabra, {result[0]}')
            
    
letra()