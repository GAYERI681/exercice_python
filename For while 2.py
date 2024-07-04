# Fonction pour vérifier si l'entrée est un nombre
def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# Demander à l'utilisateur d'entrer un nombre
user_input = input("Veuillez entrer un nombre : ")

# Vérifier que l'entrée est bien un nombre
while not is_number(user_input):
    print("Erreur : Veuillez entrer un nombre valide.")
    user_input = input("Veuillez entrer un nombre : ")

# Convertir l'entrée en entier
number = int(user_input)

# Afficher les nombres entiers de 1 à nombre en utilisant une boucle for
print("Affichage avec une boucle for :")
for i in range(1, number + 1):
    print(i)

# Afficher les nombres entiers de 1 à nombre en utilisant une boucle while
print("Affichage avec une boucle while :")
i = 1
while i <= number:
    print(i)
    i += 1