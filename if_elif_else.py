# Demander à l'utilisateur d'entrer une note
note = float(input("Veuillez entrer votre note : "))

# Vérifier la note et afficher la mention correspondante
if note >= 18:
    print("Excellent")
elif note >= 16 and note < 18:
    print("Très bien")
elif note >= 14 and note < 16:
    print("Bien")
elif note >= 12 and note < 14:
    print("Satisfaisant")
elif note >= 10 and note < 12:
    print("Passable")
else:
    print("Échec")