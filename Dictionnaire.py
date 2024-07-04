def afficher_menu():
    print("\nChoisissez parmi les 5 options suivantes:")
    print("1- Ajouter un article dans le panier")
    print("2- Supprimer un article du panier")
    print("3- Afficher tous les articles")
    print("4- Vider le panier")
    print("5- Quitter")

# Créer une variable panier qui est une liste vide
panier = []

while True:
    afficher_menu()
    choix = input("Quel est votre choix? ")

    if choix == '1':
        # Ajouter un article dans le panier
        nom_article = input("Entrez le nom de l'article: ")
        prix_article = float(input("Entrez le prix de l'article: "))
        article = {'name': nom_article, 'price': prix_article}
        panier.append(article)
        print(f"Article {nom_article} ajouté avec succès!")

    elif choix == '2':
        # Supprimer un article du panier
        nom_article = input("Entrez le nom de l'article à supprimer: ")
        article_trouve = False
        for article in panier:
            if article['name'] == nom_article:
                panier.remove(article)
                article_trouve = True
                print(f"Article {nom_article} supprimé avec succès!")
                break
        if not article_trouve:
            print("Aucun article avec ce nom.")

    elif choix == '3':
        # Afficher tous les articles
        if panier:
            print("Voici les articles dans votre panier:")
            for article in panier:
                print(f"Article: {article['name']}, Prix: {article['price']}")
        else:
            print("Votre panier est vide.")

    elif choix == '4':
        # Vider le panier
        panier.clear()
        print("Le panier a été vidé avec succès!")

    elif choix == '5':
        # Quitter
        print("Fin du programme")
        exit()

    else:
        print("Choix invalide, veuillez réessayer.")