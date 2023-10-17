class Node:
    def __init__(self, name, is_hero):
        self.name = name
        self.is_hero = is_hero
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, name, is_hero):
        self.root = self._insert(self.root, name, is_hero)

    def _insert(self, node, name, is_hero):
        if node is None:
            return Node(name, is_hero)
        if name < node.name:
            node.left = self._insert(node.left, name, is_hero)
        elif name > node.name:
            node.right = self._insert(node.right, name, is_hero)
        return node

    def list_villains_alphabetically(self):
        villains = self._list_characters_alphabetically(self.root, False)
        return villains

    def list_heroes_starting_with_c(self):
        heroes = self._list_characters_starting_with_c(self.root)
        return heroes

    def count_superheroes(self):
        return self._count_superheroes(self.root)

    def find_and_rename_doctor_strange(self):
        self.root = self._find_and_rename(self.root, "Doctor Strange", "Dr. Strange")

    def list_characters_descending(self):
        characters = self._list_characters_descending(self.root)
        return characters

    def generate_forest(self):
        heroes_tree = BinarySearchTree()
        villains_tree = BinarySearchTree()
        self._generate_forest(self.root, heroes_tree, villains_tree)
        return heroes_tree, villains_tree

    def _list_characters_alphabetically(self, node, is_hero):
        if node is None:
            return []
        characters = []
        if is_hero and not node.is_hero:
            characters.append(node.name)
        characters += self._list_characters_alphabetically(node.left, is_hero)
        characters += self._list_characters_alphabetically(node.right, is_hero)
        return characters

    def _list_characters_starting_with_c(self, node):
        if node is None:
            return []
        heroes = []
        if node.is_hero and node.name.startswith('C'):
            heroes.append(node.name)
        heroes += self._list_characters_starting_with_c(node.left)
        heroes += self._list_characters_starting_with_c(node.right)
        return heroes

    def _count_superheroes(self, node):
        if node is None:
            return 0
        count = 0
        if node.is_hero:
            count += 1
        count += self._count_superheroes(node.left)
        count += self._count_superheroes(node.right)
        return count

    def _find_and_rename(self, node, target_name, new_name):
        if node is None:
            return None
        if node.name == target_name:
            node.name = new_name
        node.left = self._find_and_rename(node.left, target_name, new_name)
        node.right = self._find_and_rename(node.right, target_name, new_name)
        return node

    def _list_characters_descending(self, node):
        if node is None:
            return []
        characters = []
        characters += self._list_characters_descending(node.right)
        characters.append(node.name)
        characters += self._list_characters_descending(node.left)
        return characters

    def _generate_forest(self, node, heroes_tree, villains_tree):
        if node is None:
            return
        if node.is_hero:
            heroes_tree.insert(node.name, True)
        else:
            villains_tree.insert(node.name, False)
        self._generate_forest(node.left, heroes_tree, villains_tree)
        self._generate_forest(node.right, heroes_tree, villains_tree)

# Ejemplo de uso:
tree = BinarySearchTree()
tree.insert("Spider-Man", True)
tree.insert("Iron Man", True)
tree.insert("Loki", False)
tree.insert("Captain America", True)
tree.insert("Doctor Strange", True)
tree.insert("Black Widow", True)
tree.insert("Thanos", False)

# Tareas:
# a. Árbol ya contiene los datos como se describe.
# b. Listar los villanos ordenados alfabéticamente.
villains = tree.list_villains_alphabetically()
print("Villanos ordenados alfabéticamente:", villains)

# c. Mostrar todos los superhéroes que empiezan con C.
heroes_starting_with_c = tree.list_heroes_starting_with_c()
print("Superhéroes que empiezan con C:", heroes_starting_with_c)

# d. Determinar cuántos superhéroes hay en el árbol.
hero_count = tree.count_superheroes()
print("Número de superhéroes:", hero_count)

# e. Encontrar y renombrar a Doctor Strange.
tree.find_and_rename_doctor_strange()

# f. Listar los superhéroes ordenados de manera descendente.
characters_descending = tree.list_characters_descending()
print("Superhéroes ordenados de manera descendente:", characters_descending)

# g. Generar un bosque a partir del árbol.
heroes_tree, villains_tree = tree.generate_forest()

# I. Determinar cuántos nodos tiene cada árbol.
hero_node_count = tree.count_superheroes()
villain_node_count = villains_tree.count_superheroes()
print("Número de nodos en el árbol de superhéroes:", hero_node_count)
print("Número de nodos en el árbol de villanos:", villain_node_count)

# II. Realizar un barrido ordenado alfabéticamente de cada árbol.
heroes_alphabetical = heroes_tree.list_villains_alphabetically()
villains_alphabetical = villains_tree.list_villains_alphabetically()
print("Barrido alfabético de superhéroes:", heroes_alphabetical)
print("Barrido alfabético de villanos:", villains_alphabetical)
