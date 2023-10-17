class NodoArbol:
    def __init__(self, nombre, derrotador=None, descripcion=""):
        self.nombre = nombre
        self.derrotador = derrotador
        self.descripcion = descripcion
        self.izquierda = None
        self.derecha = None

def insertar(raiz, criatura, derrotador=None, descripcion=""):
    if raiz is None:
        return NodoArbol(criatura, derrotador, descripcion)
    if criatura < raiz.nombre:
        raiz.izquierda = insertar(raiz.izquierda, criatura, derrotador, descripcion)
    elif criatura > raiz.nombre:
        raiz.derecha = insertar(raiz.derecha, criatura, derrotador, descripcion)
    return raiz

def cargar_descripcion(raiz, criatura, descripcion):
    nodo = buscar(raiz, criatura)
    if nodo:
        nodo.descripcion = descripcion

def buscar(raiz, criatura):
    if raiz is None or raiz.nombre == criatura:
        return raiz
    if criatura < raiz.nombre:
        return buscar(raiz.izquierda, criatura)
    return buscar(raiz.derecha, criatura)

def mostrar_criatura(raiz, criatura):
    nodo = buscar(raiz, criatura)
    if nodo:
        print(f"Nombre: {nodo.nombre}")
        print(f"Descripción: {nodo.descripcion}")
        print(f"Derrotador: {nodo.derrotador}")
    else:
        print(f"Criatura '{criatura}' no encontrada")

def listado_inorden(raiz):
    if raiz:
        listado_inorden(raiz.izquierda)
        print(f"Nombre: {raiz.nombre}, Derrotador: {raiz.derrotador}")
        listado_inorden(raiz.derecha)

def derrotadores_mas_comunes(raiz):
    derrotadores = {}
    contar_derrotadores(raiz, derrotadores)
    return sorted(derrotadores.items(), key=lambda x: x[1], reverse=True)[:3]

def contar_derrotadores(raiz, derrotadores):
    if raiz:
        contar_derrotadores(raiz.izquierda, derrotadores)
        derrotador = raiz.derrotador
        if derrotador:
            if derrotador in derrotadores:
                derrotadores[derrotador] += 1
            else:
                derrotadores[derrotador] = 1
        contar_derrotadores(raiz.derecha, derrotadores)

def criaturas_derrotadas_por(raiz, derrotador):
    criaturas = []
    buscar_criaturas_derrotadas(raiz, derrotador, criaturas)
    return criaturas

def buscar_criaturas_derrotadas(raiz, derrotador, criaturas):
    if raiz:
        buscar_criaturas_derrotadas(raiz.izquierda, derrotador, criaturas)
        if raiz.derrotador == derrotador:
            criaturas.append(raiz.nombre)
        buscar_criaturas_derrotadas(raiz.derecha, derrotador, criaturas)

def criaturas_no_derrotadas(raiz):
    no_derrotadas = []
    buscar_criaturas_no_derrotadas(raiz, no_derrotadas)
    return no_derrotadas

def buscar_criaturas_no_derrotadas(raiz, no_derrotadas):
    if raiz:
        buscar_criaturas_no_derrotadas(raiz.izquierda, no_derrotadas)
        if raiz.derrotador is None:
            no_derrotadas.append(raiz.nombre)
        buscar_criaturas_no_derrotadas(raiz.derecha, no_derrotadas)

def capturar_criatura(raiz, criatura, capturador):
    nodo = buscar(raiz, criatura)
    if nodo:
        nodo.derrotador = capturador

def eliminar_criatura(raiz, criatura):
    if raiz is None:
        return raiz
    if criatura < raiz.nombre:
        raiz.izquierda = eliminar_criatura(raiz.izquierda, criatura)
    elif criatura > raiz.nombre:
        raiz.derecha = eliminar_criatura(raiz.derecha, criatura)
    else:
        if raiz.izquierda is None:
            return raiz.derecha
        elif raiz.derecha is None:
            return raiz.izquierda
        sucesor = encontrar_sucesor(raiz.derecha)
        raiz.nombre = sucesor.nombre
        raiz.derecha = eliminar_criatura(raiz.derecha, sucesor.nombre)
    return raiz

def encontrar_sucesor(nodo):
    while nodo.izquierda:
        nodo = nodo.izquierda
    return nodo

def modificar_nombre(raiz, criatura, nuevo_nombre):
    nodo = buscar(raiz, criatura)
    if nodo:
        nodo.nombre = nuevo_nombre

def listar_por_nivel(raiz):
    if not raiz:
        return
    nivel_actual = [raiz]
    while nivel_actual:
        nivel_siguiente = []
        for nodo in nivel_actual:
            print(f"Nombre: {nodo.nombre}, Derrotador: {nodo.derrotador}")
            if nodo.izquierda:
                nivel_siguiente.append(nodo.izquierda)
            if nodo.derecha:
                nivel_siguiente.append(nodo.derecha)
        nivel_actual = nivel_siguiente

def criaturas_capturadas_por(raiz, capturador):
    capturadas = []
    buscar_criaturas_capturadas(raiz, capturador, capturadas)
    return capturadas

def buscar_criaturas_capturadas(raiz, capturador, capturadas):
    if raiz:
        buscar_criaturas_capturadas(raiz.izquierda, capturador, capturadas)
        if raiz.derrotador == capturador:
            capturadas.append(raiz.nombre)
        buscar_criaturas_capturadas(raiz.derecha, capturador, capturadas)

# Crear el árbol con los datos iniciales
raiz = None
datos_iniciales = [
    ("Cerbero", "Heracles"),
    ("Toro de Creta", "Heracles"),
    ("Cierva Cerinea", "Heracles"),
    ("Jabalí de Erimanto", "Heracles"),
    ("Basilisco", "Zeus"),
    ("Sirenas", "Ulises"),
    ("Aves del Estínfalo", "Heracles"),
    ("Ladón", "Hera"),
    # Agrega más criaturas y sus derrotadores aquí
]

for criatura, derrotador in datos_iniciales:
    raiz = insertar(raiz, criatura, derrotador)

# Modificar el nodo de las Aves del Estínfalo para indicar que Heracles las derrotó
capturar_criatura(raiz, "Aves del Estínfalo", "Heracles")

# Modificar el nombre de la criatura Ladón por Dragón Ladón
modificar_nombre(raiz, "Ladón", "Dragón Ladón")

# Eliminar al Basilisco y a las Sirenas
raiz = eliminar_criatura(raiz, "Basilisco")
raiz = eliminar_criatura(raiz, "Sirenas")

# Listar criaturas derrotadas por Heracles
criaturas_derrotadas_por_heracles = criaturas_derrotadas_por(raiz, "Heracles")
print("Criaturas derrotadas por Heracles:", criaturas_derrotadas_por_heracles)

# Listado inorden de las criaturas y quienes las derrotaron
print("Listado Inorden:")
listado_inorden(raiz)

# Mostrar toda la información de la criatura Talos
mostrar_criatura(raiz, "Talos")

# Determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas
derrotadores_top3 = derrotadores_mas_comunes(raiz)
print("3 héroes o dioses que derrotaron más criaturas:")
for derrotador, cantidad in derrotadores_top3:
    print(f"{derrotador}: {cantidad}")

# Listar las criaturas que no han sido derrotadas
criaturas_no_vencidas = criaturas_no_derrotadas(raiz)
print("Criaturas no derrotadas:", criaturas_no_vencidas)

# Listado por nivel del árbol
print("Listado por nivel del árbol:")
listar_por_nivel(raiz)

# Muestre las criaturas capturadas por Heracles
criaturas_capturadas_por_heracles = criaturas_capturadas_por(raiz, "Heracles")
print("Criaturas capturadas por Heracles:", criaturas_capturadas_por_heracles)
