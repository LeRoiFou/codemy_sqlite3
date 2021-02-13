
"""Import du fichier où se trouve le programme des bases de données, sous la forme d'un module"""

import main

"""Affichage de toutes les données de la table 'clients'"""
main.show_all()
print('*'*50)

"""Ajout d'une donnée dans la table 'clients' et affichage de toutes les données"""
main.add_one('WHITE', 'Walter', 'heinsenberg@meta.com')
main.show_all()
print('*'*50)

"""Suppression d'une donnée de la table 'clients' et affichage de toutes les données"""
main.delete_one('7')
main.show_all()
print('*'*50)

"""Ajout de plusieurs données dans la table 'clients' et affichage de toutes les données"""
my_liste = [('DUPONT', 'Michel', 'mdupont@yahoo.fr'),
            ('CHURCHILL', 'Winston', 'wwg2@gmail.com'),
            ('AYMARD', 'Jean', 'jaymard@aol.com')]
main.add_many(my_liste)
main.show_all()
print('*'*50)

"""Suppression de données de la table 'clients' et affichage de toutes les données"""
main.delete_one('7')
main.delete_one('8')
main.delete_one('9')
main.show_all()
print('*'*50)

"""Affichage d'une donnée de la table 'clients'"""
main.email_lookup('mozart@gmail.com')
