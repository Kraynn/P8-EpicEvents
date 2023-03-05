# Epic Events - Projet #12
__________________________

Le programme a pour objet la création d'une CRM permettant le suivi et la gestion des clients ainsi que la création d'évènements.
Le CRM évolue avec les modèles d'objet suivants:
- Utilisateurs
- Clients
- Contrats
- Evènements

Les utilisateurs sont distingués en trois catégories:
Manager - gestion d’ensemble du système
Sales - suivi de clients, création de contrat et d’évènements
Support - suivi de clients et des évènements


______________
HOW TO INSTALL
--------------

Importation des scripts:
---------------------------

Télécharger et extaire le contenu du repertoire https://github.com/Kraynn/P8-EpicEvents dans le répertoire local. 
> 
Puis déplacer le contenu dans le repertoire local voulu.


Ou cloner le répertoire via github en utilisant la commande:
> git clone github.com/Kraynn/P8-EpicEvents


__________________________________________________________
Création de l'environnement virtuel:
------------------------------------
Exectuer les commandes suivantes dans l'invité de commande au sein du répertoire local voulu:
>
>python -m venv epicevents

>epicevents\Scripts\activate.bat

>pip install -r requirements.txt


Configuration de la base de donnée PostgreSQL:
----------------------------------------------

> Installer l'outil de configuration [PgAdmin](https://www.postgresql.org/download/windows/) et configurer votre base de données en choissisant un mot de passe. 

> Modifier le paramètre DATABASES du projet django dans settings.py avec les valeurs suivantes avec le mot de passe choisi:
* 'ENGINE':'django.db.backends.postgresql_psycopg2',
* 'NAME':'postgres',
* 'USER':'postgres',
* 'PASSWORD':'*******',
* 'HOST':'localhost',
* 'PORT':'5432',
      
> Effectuer les mirgrations avec les commandes:
* python manage.py makemigrations
* python manage.py migrate

___________________________________________________



Lancer le serveur :
----------------------

A partir de l'environnement virtuel créé, s'assurer d'être dans le fichier "epicevents" puis exécuter la commande suivante:
>
>python manage.py runserver

Les requêtes de l'api se font sur le serveur local à l'adresse suivante:
 > 127.0.0.1:8000
 
 
Création du manager et des groupes:
-----------------------------------
  
Créer un administrateur et/ou des managers avec la commande:
> python manage.py createsuperuser

> Se connecter en tant qu'administrateur/manager à l'adresse suivante:
* http://127.0.0.1:8000/admin/
* Créer les groupes "support" et "sales" en cliquant sur "Groups"
  


Postmman :
----------------------

L'ensemble des routes de requêtes est documenté sur Postman:
> [Documentation](https://documenter.getpostman.com/view/23482099/2s93JnV71D)

***************************








