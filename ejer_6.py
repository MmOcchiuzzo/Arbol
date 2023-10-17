class Jedi:
    def __init__(self, nombre, especie, anio_nacimiento, color_sable, ranking, maestros):
        self.nombre = nombre
        self.especie = especie
        self.anio_nacimiento = anio_nacimiento
        self.color_sable = color_sable
        self.ranking = ranking
        self.maestros = maestros

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class JediRegistry:
    def __init__(self):
        self.root_name = None
        self.root_ranking = None
        self.root_especie = None

    def insert_by_name(self, jedi):
        self.root_name = self._insert_by_name(self.root_name, jedi)

    def insert_by_ranking(self, jedi):
        self.root_ranking = self._insert_by_ranking(self.root_ranking, jedi)

    def insert_by_especie(self, jedi):
        self.root_especie = self._insert_by_especie(self.root_especie, jedi)

    def _insert_by_name(self, root, jedi):
        if root is None:
            return TreeNode(jedi)
        if jedi.nombre < root.data.nombre:
            root.left = self._insert_by_name(root.left, jedi)
        else:
            root.right = self._insert_by_name(root.right, jedi)
        return root

    def _insert_by_ranking(self, root, jedi):
        if root is None:
            return TreeNode(jedi)
        if jedi.ranking < root.data.ranking:
            root.left = self._insert_by_ranking(root.left, jedi)
        else:
            root.right = self._insert_by_ranking(root.right, jedi)
        return root

    def _insert_by_especie(self, root, jedi):
        if root is None:
            return TreeNode(jedi)
        if jedi.especie < root.data.especie:
            root.left = self._insert_by_especie(root.left, jedi)
        else:
            root.right = self._insert_by_especie(root.right, jedi)
        return root

    def in_order_traversal(self, root, attribute):
        if root is not None:
            self.in_order_traversal(root.left, attribute)
            if attribute == "nombre":
                print(f"Nombre: {root.data.nombre}, Especie: {root.data.especie}, Ranking: {root.data.ranking}")
            elif attribute == "ranking":
                print(f"Ranking: {root.data.ranking}, Nombre: {root.data.nombre}, Especie: {root.data.especie}")
            self.in_order_traversal(root.right, attribute)

    def level_order_traversal(self, root, attribute):
        if root is None:
            return
        queue = []
        queue.append(root)
        while queue:
            current = queue.pop(0)
            if attribute == "ranking":
                print(f"Ranking: {current.data.ranking}, Nombre: {current.data.nombre}, Especie: {current.data.especie}")
            elif attribute == "especie":
                print(f"Especie: {current.data.especie}, Nombre: {current.data.nombre}, Ranking: {current.data.ranking}")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    def find_jedi(self, name):
        return self._find_jedi(self.root_name, name)

    def _find_jedi(self, root, name):
        if root is None:
            return None
        if name == root.data.nombre:
            return root.data
        if name < root.data.nombre:
            return self._find_jedi(root.left, name)
        else:
            return self._find_jedi(root.right, name)

    def get_jedi_by_ranking(self, ranking):
        results = []
        self._get_jedi_by_ranking(self.root_ranking, ranking, results)
        return results

    def _get_jedi_by_ranking(self, root, ranking, results):
        if root is None:
            return
        if ranking == root.data.ranking:
            results.append(root.data)
        if ranking < root.data.ranking:
            self._get_jedi_by_ranking(root.left, ranking, results)
        else:
            self._get_jedi_by_ranking(root.right, ranking, results)

    def get_jedi_by_sable_color(self, color):
        results = []
        self._get_jedi_by_sable_color(self.root_name, color, results)
        return results

    def _get_jedi_by_sable_color(self, root, color, results):
        if root is not None:
            self._get_jedi_by_sable_color(root.left, color, results)
            if color in root.data.color_sable:
                results.append(root.data)
            self._get_jedi_by_sable_color(root.right, color, results)

    def get_jedi_with_masters(self, masters):
        results = []
        self._get_jedi_with_masters(self.root_name, masters, results)
        return results

    def _get_jedi_with_masters(self, root, masters, results):
        if root is not None:
            self._get_jedi_with_masters(root.left, masters, results)
            if any(master in root.data.maestros for master in masters):
                results.append(root.data)
            self._get_jedi_with_masters(root.right, masters, results)

    def get_jedi_by_species(self, species):
        results = []
        self._get_jedi_by_species(self.root_especie, species, results)
        return results

    def _get_jedi_by_species(self, root, species, results):
        if root is not None:
            self._get_jedi_by_species(root.left, species, results)
            if root.data.especie in species:
                results.append(root.data)
            self._get_jedi_by_species(root.right, species, results)

    def get_jedi_by_name_starting_with_a_or_containing_hyphen(self):
        results = []
        self._get_jedi_by_name_starting_with_a_or_containing_hyphen(self.root_name, results)
        return results

    def _get_jedi_by_name_starting_with_a_or_containing_hyphen(self, root, results):
        if root is not None:
            self._get_jedi_by_name_starting_with_a_or_containing_hyphen(root.left, results)
            if root.data.nombre.startswith('A') or '-' in root.data.nombre:
                results.append(root.data)
            self._get_jedi_by_name_starting_with_a_or_containing_hyphen(root.right, results)


# Ejemplo de uso:
# Crear un registro de Jedi y agregar Jedi a los árboles
registro_jedi = JediRegistry()

# Agregar Jedi al registro
registro_jedi.insert_by_name(Jedi("Yoda", "Unknown", 896, "verde", "Jedi Master", []))
registro_jedi.insert_by_name(Jedi("Luke Skywalker", "Human", 19, "verde", "Jedi Knight", ["Yoda"]))
# Agregar más Jedi...

# a. Los Jedi se agregarán automáticamente a los árboles por nombre, ranking y especie.
# b. Realizar un barrido inorden por nombre y ranking
print("Barrido inorden por nombre:")
registro_jedi.in_order_traversal(registro_jedi.root_name, "nombre")

print("Barrido inorden por ranking:")
registro_jedi.in_order_traversal(registro_jedi.root_ranking, "ranking")

# c. Realizar un barrido por nivel de los árboles por ranking y especie
print("Barrido por nivel por ranking:")
registro_jedi.level_order_traversal(registro_jedi.root_ranking, "ranking")

print("Barrido por nivel por especie:")
registro_jedi.level_order_traversal(registro_jedi.root_especie, "especie")

# d. Mostrar toda la información de Yoda y Luke Skywalker
yoda_info = registro_jedi.find_jedi("Yoda")
luke_skywalker_info = registro_jedi.find_jedi("Luke Skywalker")
if yoda_info:
    print("Información de Yoda:", yoda_info.__dict__)
if luke_skywalker_info:
    print("Información de Luke Skywalker:", luke_skywalker_info.__dict__)

# e. Mostrar todos los Jedi con ranking "Jedi Master"
jedi_masters = registro_jedi.get_jedi_by_ranking("Jedi Master")
print("Jedi Masters:")
for jedi in jedi_masters:
    print(jedi.__dict__)

# f. Listar todos los Jedi que utilizaron sable de luz color verde
green_saber_users = registro_jedi.get_jedi_by_sable_color("verde")
print("Usuarios de sables verdes:")
for jedi in green_saber_users:
    print(jedi.__dict__)

# g. Listar todos los Jedi cuyos maestros están en el archivo
jedi_with_masters = registro_jedi.get_jedi_with_masters(["Yoda"])
print("Jedi con Yoda como maestro:")
for jedi in jedi_with_masters:
    print(jedi.__dict__)

# h. Mostrar todos los Jedi de especie "Togruta" o "Cerean"
specific_species = registro_jedi.get_jedi_by_species(["Togruta", "Cerean"])
print("Jedi de especie Togruta o Cerean:")
for jedi in specific_species:
    print(jedi.__dict__)

# i. Listar los Jedi que comienzan con la letra A o contienen un "-"
special_jedi = registro_jedi.get_jedi_by_name_starting_with_a_or_containing_hyphen()
print("Jedi cuyos nombres comienzan con A o contienen un -:")
for jedi in special_jedi:
    print(jedi.__dict__)
