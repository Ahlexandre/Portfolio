"""
Auteur : REQUILLART Marius et DU Alexandre
Date de création : 30/11/2023
Nom du fichier : minigame.py
Description : Ce programme génère un jeu de labyrinthe aléatoire où le joueur doit se déplacer à travers la carte,
collecter des objets et atteindre la sortie pour passer au niveau suivant. Le jeu propose différents niveaux de difficulté.
"""


import random

dico = {0: ' ', 1: '█', 'o': '○', '.': '⚡', 2: ' ', 3: 'X'}

def generate_random_map(size_map, proportion_wall):
    """
        Génère une carte aléatoire en fonction de la taille spécifiée et de la proportion de murs.

        paramètre: size_map: Tuple (largeur, hauteur) de la carte.
        paramètre: proportion_wall: Proportion de murs dans la carte.
        return: Carte générée aléatoirement.
    """
    width, height = size_map
    total_cells = width * height
    num_walls = int(proportion_wall * total_cells)

    new_map = [[0] * width for _ in range(height)]

    for i in range(num_walls):
        x = random.randint(1, width - 1)
        y = random.randint(1, height - 1)
        new_map[y][x] = 1

    entry_x = random.randint(1, width - 2)
    entry_y = random.randint(1, height - 2)
    new_map[entry_y][entry_x] = 2

    exit_x = random.randint(1, width - 2)
    exit_y = random.randint(1, height - 2)
    new_map[exit_y][exit_x] = 3

    return new_map

def choose_difficulty():
    """
        Permet au joueur de choisir le niveau de difficulté.

        return: Tuple contenant les paramètres du jeu en fonction du choix du joueur.
    """
    print("Choisissez le niveau de difficulté :")
    print("1. Facile")
    print("2. Moyen")
    print("3. Difficile")
    choice = input("Entrez le numéro du niveau de difficulté : ")

    if choice == '1':
        size_map = (7, 6)
        proportion_wall = 0.2
        num_objects = random.randint(3, 5)
    elif choice == '2':
        size_map = (9, 7)
        proportion_wall = 0.3
        num_objects = random.randint(6, 9)
    elif choice == '3':
        size_map = (11, 9)
        proportion_wall = 0.4
        num_objects = random.randint(10, 12)
    else:
        print("Niveau de difficulté non valide. Utilisation des paramètres par défaut.")
        size_map = (7, 6)
        proportion_wall = 0.2
        num_objects = random.randint(3, 5)

    return size_map, proportion_wall, num_objects


def create_perso(depart):
    """
        Crée un personnage avec une position initiale donnée.

        paramètre: depart: Tuple (x, y) de la position initiale du personnage.
        return: Dictionnaire représentant le personnage.
    """
    perso = {
        'char': 'o',
        'x': depart[0],
        'y': depart[1],
        'score': 0
    }
    return perso

def display_map(m, d):
    """
    Affiche la carte en utilisant un dictionnaire pour mapper les éléments.

    paramètre: m: Carte à afficher.
    paramètre: d: Dictionnaire de correspondance entre les éléments de la carte et leur représentation.
    return: Chaîne de caractères représentant la carte.
    """
    result = ''
    for ligne in m:
        for element in ligne:
            result += d[element]
        result += '\n'
    return result

def display_map_and_char(m, d, p):
    """
    Affiche la carte avec la position du personnage.

    paramètre: m: Carte à afficher.
    paramètre: d: Dictionnaire de correspondance entre les éléments de la carte et leur représentation.
    paramètre: p: Dictionnaire représentant le personnage.
    return: Chaîne de caractères représentant la carte avec le personnage.
    """
    m2 = []
    for ligne in m:
        m2.append(ligne[:])
    result = ""
    for i in range(len(m2)):
        for j in range(len(m2[i])):
            if i == p['y'] and j == p['x']:
                result += p['char']
            else:
                result += d[m[i][j]]
        result += '\n'
    return result

def delete_all_walls(m, pos):
    """
    Supprime tous les murs autour d'une position donnée.

    paramètre: m: Carte à modifier.
    paramètre: pos: Tuple (x, y) de la position autour de laquelle supprimer les murs.
    """
    x, y = pos
    for i in range(y - 1, y + 2):
        for j in range(x - 1, x + 2):
            if 0 <= i < len(m) and 0 <= j < len(m[0]) and m[i][j] != 3:
                m[i][j] = 0

def update_p(letter, p, m):
    """
    Met à jour la position du personnage en fonction de la lettre de déplacement.

    paramètre: letter: Lettre de déplacement ('z', 's', 'q', 'd', 'e' ou 'p').
    paramètre: p: Dictionnaire représentant le personnage.
    paramètre: m: Carte du jeu.
    return: Dictionnaire mis à jour représentant le personnage.
    """
    x = p['x']
    y = p['y']

    valid_moves = ['z', 's', 'q', 'd', 'e', 'p']

    if letter in valid_moves:
        if letter == 'z':
            y -= 1
        elif letter == 's':
            y += 1
        elif letter == 'q':
            x -= 1
        elif letter == 'd':
            x += 1
        elif letter == 'e':
            delete_all_walls(m, (x, y))
            print("Vous avez détruit les murs autour de vous.")
        elif letter == 'p':
            print("Vous avez quitté le jeu. Votre score est de " + str(p['score']))
            exit()

        if 0 <= y < len(m) and 0 <= x < len(m[0]) and m[y][x] != 1:
            p['x'] = x
            p['y'] = y
        else:
            print("Vous ne pouvez pas effectuer ce déplacement !")
    else:
        print("Entrée invalide. Utilisez les touches 'z', 's', 'q', 'd', 'e' ou 'p'.")

    return p

def create_objects(nb_objects, m):
    """
    Crée des objets à des positions aléatoires sur la carte.

    paramètre: nb_objects: Nombre d'objets à créer.
    paramètre: m: Carte du jeu.
    return: Ensemble d'objets représentés par des tuples (x, y).
    """
    objects = set()

    while len(objects) < nb_objects:
        x = random.randint(1, len(m[0]) - 1)
        y = random.randint(1, len(m) - 1)

        if m[y][x] == 0:
            objects.add((x, y))

    return objects

def display_map_char_and_objects(m, d, p, objects):
    """
    Affiche la carte avec la position du personnage et les objets.

    paramètre: m: Carte à afficher.
    paramètre: d: Dictionnaire de correspondance entre les éléments de la carte et leur représentation.
    paramètre: p: Dictionnaire représentant le personnage.
    paramètre: objects: Ensemble d'objets représentés par des tuples (x, y).
    return: Chaîne de caractères représentant la carte avec le personnage et les objets.
    """
    map_copy = [ligne[:] for ligne in m]

    for obj in objects:
        x, y = obj
        map_copy[y][x] = '.'

    map_copy[p['y']][p['x']] = p['char']

    map_str = ''
    for row in map_copy:
        for element in row:
            map_str += d[element]
        map_str += '\n'

    map_str += "Score du joueur: " + str(p['score'])

    return map_str

def update_objects(perso, objects):
    """
    Met à jour la position des objets en fonction de la position du personnage.

    paramètre: perso: Dictionnaire représentant le personnage.
    paramètre: objects: Ensemble d'objets représentés par des tuples (x, y).
    return: Ensemble d'objets mis à jour après la collecte éventuelle par le personnage.
    """

    perso_position = (perso['x'], perso['y'])

    if perso_position in objects:
        objects.remove(perso_position)
        print("Vous avez ramassé un objet ! Votre score est maintenant de " + str(perso['score'] + 1))
        perso['score'] += 1

    return objects

def find_entry(m):
    """
    Recherche et retourne les coordonnées de l'entrée sur la carte.

    paramètre: m: Carte du jeu.
    return: Tuple (x, y) des coordonnées de l'entrée.
    """
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 2:
                return j, i

def create_new_level(p, m, obj, size_map, proportion_wall):
    """
    Crée un nouveau niveau en générant une nouvelle carte, replaçant le personnage à l'entrée
    et générant de nouveaux objets.

    paramètre: p: Dictionnaire représentant le personnage.
    paramètre: m: Carte actuelle du jeu.
    paramètre: obj: Ensemble d'objets représentés par des tuples (x, y).
    paramètre: size_map: Tuple (largeur, hauteur) de la nouvelle carte.
    paramètre: proportion_wall: Proportion de murs dans la nouvelle carte.
    return: Nouvelle carte et ensemble d'objets pour le niveau suivant.
    """
    m = generate_random_map(size_map, proportion_wall)
    p['x'], p['y'] = find_entry(m)
    obj = create_objects(len(obj), m)
    print("Niveau suivant !")

    return m, obj

def generate_new_objects(m, num_objects):
    """
    Génère de nouveaux objets à des positions aléatoires sur la carte.

    paramètre: m: Carte du jeu.
    paramètre: num_objects: Nombre d'objets à créer.
    return: Ensemble d'objets représentés par des tuples (x, y).
    """
    new_objects = set()

    while len(new_objects) < num_objects:
        x = random.randint(1, len(m[0]) - 1)
        y = random.randint(1, len(m) - 1)

        if m[y][x] == 0:
            new_objects.add((x, y))

    return new_objects

def are_all_objects_collected(objects):
    """
    Vérifie si tous les objets ont été collectés.

    paramètre: objects: Ensemble d'objets représentés par des tuples (x, y).
    return: True si tous les objets ont été collectés, False sinon.
    """
    return not objects


size_map, proportion_wall, nb_objects = choose_difficulty()
random_map = generate_random_map(size_map, proportion_wall)
objects = create_objects(nb_objects, random_map)
perso = create_perso((0, 0))

while True:
    print(display_map_char_and_objects(random_map, dico, perso, objects))

    letter = input("Quel est votre déplacement ? (Appuyez sur 'p' pour quitter) ")

    if letter.lower() == 'p':
        print("Bravo ! Votre score est de " + str(perso['score']))
        break

    perso = update_p(letter, perso, random_map)
    objects = update_objects(perso, objects)

    if random_map[perso['y']][perso['x']] == 3:
        if are_all_objects_collected(objects):
            random_map, objects = create_new_level(perso, random_map, objects, size_map, proportion_wall)
            new_objects = generate_new_objects(random_map, nb_objects)
            objects.update(new_objects)
        else:
            print("Il reste des objets à ramasser avant de passer au niveau suivant.")