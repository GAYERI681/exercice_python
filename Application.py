class Client:
    def __init__(self, code, nom, telephone, adresse, email):
        self.code = code
        self.nom = nom
        self.telephone = telephone
        self.adresse = adresse
        self.email = email
        self.solde = 0

class Transaction:
    def __init__(self, ref_paiement, code_emetteur, code_recepteur, date_transaction, montant, canal):
        self.ref_paiement = ref_paiement
        self.code_emetteur = code_emetteur
        self.code_recepteur = code_recepteur
        self.date_transaction = date_transaction
        self.montant = montant
        self.canal = canal

def afficher_menu_principal():
    print("\nChoisissez parmi les options suivantes:")
    print("1 - Gestion des clients")
    print("2 - Gestion des transactions")
    print("3 - Sortir")

def afficher_menu_clients():
    print("\nGestion des clients:")
    print("1 - Afficher la liste des clients")
    print("2 - Ajouter un client")
    print("3 - Supprimer un client")
    print("4 - Modifier les informations d'un client")
    print("5 - Afficher le solde d'un client")
    print("6 - Retour au menu principal")

def afficher_menu_transactions():
    print("\nGestion des transactions:")
    print("1 - Afficher toutes les transactions")
    print("2 - Afficher les transactions d'un client")
    print("3 - Ajouter une transaction")
    print("4 - Retour au menu principal")

# Listes pour stocker les clients et les transactions
clients = []
transactions = []

def trouver_client(code):
    for client in clients:
        if client.code == code:
            return client
    return None

def afficher_clients():
    if clients:
        print("Liste des clients :")
        for client in clients:
            print(f"Code: {client.code}, Nom: {client.nom}, Téléphone: {client.telephone}, Adresse: {client.adresse}, Email: {client.email}, Solde: {client.solde}")
    else:
        print("Aucun client n'est enregistré.")

def ajouter_client():
    code = input("Entrez le code du client: ")
    if trouver_client(code):
        print("Un client avec ce code existe déjà.")
        return
    nom = input("Entrez le nom du client: ")
    telephone = input("Entrez le téléphone du client: ")
    adresse = input("Entrez l'adresse du client: ")
    email = input("Entrez l'email du client: ")
    client = Client(code, nom, telephone, adresse, email)
    clients.append(client)
    print("Client ajouté avec succès.")

def supprimer_client():
    code = input("Entrez le code du client à supprimer: ")
    client = trouver_client(code)
    if client:
        clients.remove(client)
        print("Client supprimé avec succès.")
    else:
        print("Aucun client avec ce code n'a été trouvé.")

def modifier_client():
    code = input("Entrez le code du client à modifier: ")
    client = trouver_client(code)
    if client:
        client.nom = input(f"Entrez le nouveau nom (actuel: {client.nom}): ") or client.nom
        client.telephone = input(f"Entrez le nouveau téléphone (actuel: {client.telephone}): ") or client.telephone
        client.adresse = input(f"Entrez la nouvelle adresse (actuel: {client.adresse}): ") or client.adresse
        client.email = input(f"Entrez le nouvel email (actuel: {client.email}): ") or client.email
        print("Informations du client mises à jour.")
    else:
        print("Aucun client avec ce code n'a été trouvé.")

def afficher_solde_client():
    code = input("Entrez le code du client: ")
    client = trouver_client(code)
    if client:
        print(f"Le solde du client {client.nom} est de {client.solde}.")
    else:
        print("Aucun client avec ce code n'a été trouvé.")

def afficher_transactions():
    if transactions:
        print("Liste des transactions :")
        for transaction in transactions:
            print(f"Référence: {transaction.ref_paiement}, Emetteur: {transaction.code_emetteur}, Récepteur: {transaction.code_recepteur}, Date: {transaction.date_transaction}, Montant: {transaction.montant}, Canal: {transaction.canal}")
    else:
        print("Aucune transaction n'est enregistrée.")

def afficher_transactions_client():
    code = input("Entrez le code du client: ")
    client = trouver_client(code)
    if client:
        print(f"Transactions pour le client {client.nom} :")
        for transaction in transactions:
            if transaction.code_emetteur == code or transaction.code_recepteur == code:
                print(f"Référence: {transaction.ref_paiement}, Emetteur: {transaction.code_emetteur}, Récepteur: {transaction.code_recepteur}, Date: {transaction.date_transaction}, Montant: {transaction.montant}, Canal: {transaction.canal}")
    else:
        print("Aucun client avec ce code n'a été trouvé.")

def ajouter_transaction():
    ref_paiement = input("Entrez la référence de la transaction: ")
    code_emetteur = input("Entrez le code de l'émetteur: ")
    code_recepteur = input("Entrez le code du récepteur: ")
    date_transaction = input("Entrez la date de la transaction: ")
    montant = float(input("Entrez le montant de la transaction: "))
    canal = input("Entrez le canal de la transaction (ORANGE MONEY, WAVE, FREE MONEY, VIREMENT BANCAIRE): ")

    emetteur = trouver_client(code_emetteur)
    recepteur = trouver_client(code_recepteur)

    if not emetteur or not recepteur:
        print("L'émetteur ou le récepteur n'existe pas.")
        return

    if emetteur.solde < montant:
        print("Solde insuffisant pour effectuer la transaction.")
        return

    transaction = Transaction(ref_paiement, code_emetteur, code_recepteur, date_transaction, montant, canal)
    transactions.append(transaction)
    
    emetteur.solde -= montant
    recepteur.solde += montant
    print("Transaction ajoutée avec succès.")

while True:
    afficher_menu_principal()
    choix = input("Quel est votre choix? ")

    if choix == '1':
        while True:
            afficher_menu_clients()
            choix_client = input("Quel est votre choix? ")
            if choix_client == '1':
                afficher_clients()
            elif choix_client == '2':
                ajouter_client()
            elif choix_client == '3':
                supprimer_client()
            elif choix_client == '4':
                modifier_client()
            elif choix_client == '5':
                afficher_solde_client()
            elif choix_client == '6':
                break
            else:
                print("Choix invalide, veuillez réessayer.")

    elif choix == '2':
        while True:
            afficher_menu_transactions()
            choix_transaction = input("Quel est votre choix? ")
            if choix_transaction == '1':
                afficher_transactions()
            elif choix_transaction == '2':
                afficher_transactions_client()
            elif choix_transaction == '3':
                ajouter_transaction()
            elif choix_transaction == '4':
                break
            else:
                print("Choix invalide, veuillez réessayer.")

    elif choix == '3':
        print("Fin du programme")
        break

    else:
        print("Choix invalide, veuillez réessayer.")
        