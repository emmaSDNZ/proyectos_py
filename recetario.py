import os 
from os import remove ,system
from pathlib import Path

#RECETAS
def crearReceta(categoria,nombreReceta, contenidoReceta):
    ruta = Path(Path.home(),"Desktop","python", "proyectos_py", "Recetas", f'{categoria}',) / f'{nombreReceta}.txt'
    newReceta = open(ruta, "w")
    newReceta.write(f'{contenidoReceta}')
    newReceta.close()
    return True
#crearReceta("Carnes","holi",412)

def leerCategoriasRecetas():    
    ruta = Path(Path.home(),"Desktop","python", "proyectos_py", "Recetas")
    rutas = os.listdir(ruta)
    totalReceta = len(list(rutas))
    return [rutas, totalReceta, ruta]
#print(leerCategoriasRecetas())

def leerRecetaEspecifica(categoria,receta):
    ruta = Path(Path.home(),"Desktop","python", "proyectos_py", "Recetas", f"{categoria}") / f'{receta}'
    return  ruta.read_text()
#print(leerRecetaEspecifica('Carnes', 'Entrecot al Malbec.txt' ))


def leerListaRecetas(categoria):
    ruta = Path(Path.home(),"Desktop","python", "proyectos_py", "Recetas", f'{categoria}')
    listReceta = os.listdir(ruta)
    return listReceta
#print(leerListaRecetas("Postres"))

def eliminarReceta(categoria,nombreReceta):
    ruta = Path(Path.home(),"Desktop","python", "proyectos_py", "Recetas", f'{categoria}',) / f'{nombreReceta}'
    return remove(ruta)
#eliminarReceta("Pastas", "fideos")

#CATEGORIAS 
def crearCarpetaCategoria(nombreCategoria):
    ruta = Path(Path.home(),"Desktop","python", "proyectos_py", "Recetas", f'{nombreCategoria}')
    if ruta.exists():
        return f"La categoria ya existe ${nombreCategoria}"
    else:
        return os.makedirs(ruta)
#crearCarpetaCategoria("nueva categoria")

def leerCategorias():    
    ruta = Path(Path.home(),"Desktop","python", "proyectos_py", "Recetas")
    rutas = os.listdir(ruta)
    return list(rutas)
#leerCategorias()

def eliminarCategoria(nombreCategoria):
    ruta = Path(Path.home(),"Desktop","python", "proyectos_py", "Recetas", f'{nombreCategoria}')
    if ruta.exists():
        return os.rmdir(ruta)
    #print(f'El directorio {nombreCategoria} no existe')
    return False   
#eliminarCategoria("nueva categoria")


def bienvenida():
    categorias, total, ruta = leerCategoriasRecetas()
    saludo = print(f"""
    Bienvenido al recetario Python
    Tu ruta de acceso al recetario Python es {ruta}
    Hay {total} recetas en total """)
    return str(saludo)
#bienvenida()

def leerValorOpciones():
    bienvenida()
    value =int(input(""" 
    Por favor elegi un numero de Opcion
    1- Leer receta
    2- Crear receta
    3- Crear categoria de receta 
    4- Eliminar receta
    5- Eliminar categoria
    6- Finalizar recetario python
    """ ))
    if value not in range(1,7):
        print("LA OPCION ELEGIDA NO ES VALIDA")
        return leerValorOpciones()
    system("cls")
    return value

#punto1
#leerValorOpciones()
def mostrarTodasLasCategorias():
    allCategorias = leerCategorias()
    for index, categoria in enumerate(allCategorias):
        print(f"""{index} - {categoria}""")
    value = int(input('Por favor elegi un numero de Categoria: '))
    if value not in range(0,len(allCategorias)):
        print("LA CATEGORIA NO EXISTE")
        return mostrarTodasLasCategorias()
    categoria = allCategorias.pop(value)
    return [value, categoria]

#print(mostrarTodasLasCategorias())

def mostrarListaRecetas():
    index, result = mostrarTodasLasCategorias()
    system("cls")
    recetas = leerListaRecetas(result)
    return [recetas,result]
#print(mostrarListaRecetas())

def mostrarRecetaPrint():
    recetas, categoria = mostrarListaRecetas()
    print("""
    Estas son tus recetas:
    """)
    for index, r in enumerate(recetas):
        print(f'{index} - {r}')
    value = int(input("Selecciona un numero? "))
    for index, r in enumerate(recetas):
        if index == value:
            value = r
    system("cls")
    return  [value, categoria, leerRecetaEspecifica(categoria, value)]
#a = mostrarRecetaPrint()
#print(a)

#Punto2
def crearRecetaDirectorio():
    recetas, categoria = mostrarListaRecetas()
    system("cls")
    nombreReceta = str(input("Ingresa el Nombre de la Receta: "))
    contenidoReceta = str(input("Ingresa el contenido de la receta: "))
    newReceta = crearReceta(categoria, nombreReceta, contenidoReceta)
    print(f'Se creo la receta {nombreReceta}')
    return newReceta 
#crearRecetaDirectorio()

#Punto3
def crearCategoriaPrint():
    value = str(input('Ingresa el nombre de la Categoria: '))
    crearCarpetaCategoria(value)
    system("cls")
    return print(f'Se creo la categoria {value}')
#crearCategoriaPrint()

#Punto4
def elimnarRecetaDirectorio():
    nombreReceta, categoria, i = mostrarRecetaPrint()
    eliminarReceta(categoria,nombreReceta)
    system("cls")
    return print(f'Se elimino la receta {nombreReceta}')
#elimnarRecetaDirectorio()

#punto5
def elimnarCategoriaDirectorio():
    value, categoria= mostrarTodasLasCategorias()
    eliminarCategoria(categoria)
    system("cls")
    return print(f'La categoria {categoria} se elimino')
#elimnarCategoriaDirectorio()

def inicio():
    value = leerValorOpciones()

    if value == 1:
        allRecetas = mostrarRecetaPrint()
        print(allRecetas[2])
        return inicio()
    if value == 2:
        crearRecetaDirectorio()
        return inicio()
    if value == 3:
        crearCategoriaPrint()
        return inicio()
    if value == 4:
        elimnarRecetaDirectorio()
        return inicio()
    if value == 5:
        elimnarCategoriaDirectorio()
        return inicio()
    if value == 6: 
        return print('Hasta la proxima')         
inicio()
