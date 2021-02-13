""""
Créer une connexion SQLITE3

Dans ce programme on apprend à :
-> créer une base de données : '''CREATE TABLE NomTable (NomChamp TypeDonnee)'''
-> insérer des données : "INSERT INTO NomTable VALUES 'condition'"
-> modifier les données : '''UPDATE NomTable SET NomChamp = 'Modification' WHERE NomChamp = 'condition''''
-> supprimer les données : "DELETE from NomTable WHERE 'condition'"
-> trier les données : "SELECT 'condition' * FROM NomTable ORDER BY NomChamp DESC (ou ASC)"
-> réaliser des conditions (AND/OR)
-> afficher les données : "SELECT * FROM NomTable WHERE 'condition'"
-> supprimer toutes les données de la table : DROP TABLE NomTable
-> recourir à des fonctions utilisées dans un autre fichier pour afficher/ajouter/supprimer/sélectionner des données

Dans un SGBD il y a 5 types de données :
-> null (équivalent au booléen)
-> integer (entiers)
-> real (float)
-> text
-> blob (images, musiques...)

Éditeur : Laurent REYNAUD
Date : 30-12-2020
"""

import sqlite3

"""Assignation à la connection au SGBD dont le fichier est créé dans le répertoire 'pieces'"""
conn = sqlite3.connect('pieces/clients.db')

"""Assignation d'un curseur au SGBD"""
c = conn.cursor()


def show_all():
    """Fonction permettant d'afficher toutes données de la table et qui va être utilisée dans un autre fichier"""

    """Assignation à la connection au SGBD dont le fichier est créé dans le répertoire 'pieces'"""
    conn = sqlite3.connect('pieces/clients.db')

    """Assignation d'un curseur au SGBD"""
    c = conn.cursor()

    """Requêtes pour afficher toutes les données de la table précédées d'un n° de clé"""
    c.execute("SELECT rowid, * FROM clients")  # rowid = clé par ligne
    items = c.fetchall()  # assignation de la récupération de toutes les données du SGBD
    for i in items:
        print(i)  # affichage des données précédées d'un n° de clé par ligne

    """Commit et fermeture des données"""
    conn.commit()
    conn.close()


def add_one(nom, prenom, email):
    """Fonction permettant d'ajouter une donnée à la table"""

    """Assignation à la connection au SGBD dont le fichier est créé dans le répertoire 'pieces'"""
    conn = sqlite3.connect('pieces/clients.db')

    """Assignation d'un curseur au SGBD"""
    c = conn.cursor()

    """Insertion de la donnée"""
    c.execute("INSERT INTO clients VALUES (?,?,?)", (nom, prenom, email))

    """Commit et fermeture des données"""
    conn.commit()
    conn.close()


def delete_one(data):
    """Fonction permettant de supprimer une donnée de la table à partir du n° de clé"""

    """Assignation à la connection au SGBD dont le fichier est créé dans le répertoire 'pieces'"""
    conn = sqlite3.connect('pieces/clients.db')

    """Assignation d'un curseur au SGBD"""
    c = conn.cursor()

    """Suppression de la donnée"""
    c.execute("DELETE from clients WHERE rowid = (?)", data)

    """Commit et fermeture des données"""
    conn.commit()
    conn.close()


def add_many(my_list):
    """Fonction permettant d'ajouter plusieurs données à la table"""

    """Assignation à la connection au SGBD dont le fichier est créé dans le répertoire 'pieces'"""
    conn = sqlite3.connect('pieces/clients.db')

    """Assignation d'un curseur au SGBD"""
    c = conn.cursor()

    """Ajout de plusieurs données"""
    c.executemany("INSERT INTO clients VALUES (?,?,?)", my_list)

    """Commit et fermeture des données"""
    conn.commit()
    conn.close()


def email_lookup(email):
    """Fonction permettant de sélectionner certaines données à partir de l'adresse email"""

    """Assignation à la connection au SGBD dont le fichier est créé dans le répertoire 'pieces'"""
    conn = sqlite3.connect('pieces/clients.db')

    """Assignation d'un curseur au SGBD"""
    c = conn.cursor()

    """Sélection de la donnée"""
    c.execute("SELECT rowid, * FROM clients WHERE email = (?)", (email,))

    """Affichage de la donnée concernée"""
    items = c.fetchall()  # assignation de la récupération de toutes les données du SGBD
    for i in items:
        print(i)  # affichage de la donnée sélectionnée précédée du n° de clé affectée

    """Commit et fermeture des données"""
    conn.commit()
    conn.close()


"----------------------------------------------------------------------------------------------------------------------"
"""                                            Création d'une table                                                  """
"----------------------------------------------------------------------------------------------------------------------"

"""Création d'une table au SGBD : recours aux exceptions pour éviter de recréer à nouveau une table lorsqu'on relance le 
script. Si on était dans la POO, il faudrait recourir à un décorateur singleton..."""
try:  # si la table n'existe pas ...
    c.execute("""CREATE TABLE clients ( 
            nom text,  
            prénom text,  
            email text)""")
except sqlite3.OperationalError:  # sinon RAF
    pass

"----------------------------------------------------------------------------------------------------------------------"
"""                                            Insertion de données                                                  """
"----------------------------------------------------------------------------------------------------------------------"

"""Insertion d'un enregistrement dans la table 'clients'"""
# c.execute("INSERT INTO clients VALUES ('MARIUS', 'Albert', 'amarius@gmail.com')")

"""Insertion de plusieurs enregistrements dans la table 'clients'"""
# many_customer = [('SMITH', 'John', 'matrix@gmail.com'),
#                  ('MOZART', 'Amadeus', 'mozart@gmail.com'),
#                  ('NAPOLEON', 'Louis', 'napoleon@gmail.com'),
#                  ('SHELBY', 'Arthur', 'ashelby@gmail.com')]  # Assignation d'une liste de tuple de données à insérer
# c.executemany("INSERT INTO clients VALUES (?,?,?)", many_customer)


"----------------------------------------------------------------------------------------------------------------------"
"""                                          Modification des données                                                """
"----------------------------------------------------------------------------------------------------------------------"

"""Mise à jour des données : pour le nom GERALD, le prénom est maintenant Amadeus"""
c.execute("""UPDATE clients SET prénom = 'Amadeus' 
            WHERE nom = 'GERALD'""")

"""Autre mise à jour des données à partir de la clé du SGBD"""
c.execute("""UPDATE clients SET prénom = 'John' 
            WHERE rowid = 1""")

"----------------------------------------------------------------------------------------------------------------------"
"""                                            Suppression de données                                                """
"----------------------------------------------------------------------------------------------------------------------"

"""Suppression de données"""
# c.execute("DELETE from clients WHERE rowid = 4")  # la clé supprimée n'est pas remplacée, on passe de la clé n° 3 à 5


"----------------------------------------------------------------------------------------------------------------------"
"""                                                 Trie de données                                                  """
"----------------------------------------------------------------------------------------------------------------------"

"""Trie des données des noms par ordre croissant : ASC"""
# c.execute("SELECT rowid, * FROM clients ORDER BY nom ASC")

"""Trie des données des noms par ordre décroissant : DESC"""
# c.execute("SELECT rowid, * FROM clients ORDER BY nom DESC")


"----------------------------------------------------------------------------------------------------------------------"
"""                                              Conditions AND / OR                                                 """
"----------------------------------------------------------------------------------------------------------------------"

"""Condition avec AND : nom commençant par la lettre M et la clé est le n° 6"""
# c.execute("SELECT rowid, * FROM clients WHERE nom LIKE 'M%' AND rowid = 6")

"""Condition avec OR : nom commençant par la lettre M ou la clé est le n° 1"""
# c.execute("SELECT rowid, * FROM clients WHERE nom LIKE 'M%' OR rowid = 1")


"----------------------------------------------------------------------------------------------------------------------"
"""                                            Afficher les données                                                  """
"----------------------------------------------------------------------------------------------------------------------"

"""Requête pour récupérer les données de la table 'clients'"""
# c.execute("SELECT * FROM clients")
# print(c.fetchone())  # récupération de la première donnée
# print(c.fetchone()[0])  # récupération du nom de la première donnée
# print(c.fetchmany(3))  # récupération des 3 premières données
# print(c.fetchall())  # récupération de toutes les données
# items = c.fetchall()  # assignation de la récupération de toutes les données du SGBD
# for i in items:
#     print(i[1] + ' ' + i[0] + ' : ' + i[2])  # affichage des prénoms et des noms et des adresses e-mails du SGBD

"""Requête pour récupérer les données de la table 'clients' avec l'obtention d'un n° clé par donnée"""
# c.execute("SELECT rowid, * FROM clients")  # rowid = clé par ligne
# items = c.fetchall()  # assignation de la récupération de toutes les données du SGBD
# for i in items:
#     print(i)  # affichage des données précédées d'un n° de clé par ligne

"""Requête pour récupérer certaines données à partir d'un champ """
# c.execute("SELECT * FROM clients WHERE nom = 'GERALD'")  # toutes données de la ligne dont le champ nom est GERALD
# items = c.fetchall()  # assignation de la récupération de toutes les données du SGBD
# for i in items:
#     print(i)  # affichage des données

"""Autre requête pour récupérer certaines données à partir d'un champ """
# c.execute("SELECT * FROM clients WHERE nom >= 'M'")  # toutes données dont le nom commence par au moins la lettre M
# items = c.fetchall()  # assignation de la récupération de toutes les données du SGBD
# for i in items:
#     print(i)  # affichage des données

"""Autre requête pour récupérer certaines données à partir d'un champ """
# c.execute("SELECT * FROM clients WHERE nom LIKE 'M%'")  # toutes données dont le nom commence par la lettre M
# items = c.fetchall()  # assignation de la récupération de toutes les données du SGBD
# for i in items:
#     print(i)  # affichage des données

"""Requête pour limiter le nombre de données à afficher"""
# c.execute("SELECT rowid, * FROM clients ORDER BY nom DESC LIMIT 3")  # Affichage de 3 dernières données
# items = c.fetchall()
# for i in items:
#     print(i)


"----------------------------------------------------------------------------------------------------------------------"
"""                                 Suppression de toutes les données la table                                       """
"----------------------------------------------------------------------------------------------------------------------"

# c.execute("DROP TABLE clients")


"----------------------------------------------------------------------------------------------------------------------"
"""                                           Commit et fermeture                                                    """
"----------------------------------------------------------------------------------------------------------------------"

"""Commit pour toute insertion, suppression modification pour pouvoir mettre à jour les données de la table 'clients'"""
conn.commit()

"""Fermeture de la connection"""
conn.close()
