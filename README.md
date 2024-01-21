# README

## Présentation :

Dans cette SAE, nous devions mettre en place une application web permetant à des utilisateurs d'acheter des billets pour un festival, et d'en consulter le contenue. De plus, nous devions aussi réaliser un module administrateur pour pouvoir gérer les événements ainsi que les groupes. 

## Installation :

### Prérequis :

- Python
- pip 
- virtualenv
- git 

### Lancement :

- Il faut d'abord cloner le dossier depuis git : `git clone https://github.com/RomainMechain/SAE_BD.git` puis  `cd SAE_BD`

- On créé ensuite l'environement virtuel : `virtualenv -p python3 env` et `source env/bin/activate`

- On installe ensuite les dépendances `pip install -r requirements.txt`

- Pour initialiser la base de donner il faut lancer la commande : `flask init_database`

- Et enfin pour lancer l'application on fait la commande : `flask run`

## Compte tests :

Pour vous connecter, vous pouvez utiliser les comptes suivants :

- Spectateur : 
    - email : spec 
    - mdp : spec
- Administrateur :
    - email : admin
    - mdp : admin

## Equipe de développement :

- Cyril Landon-Nomine
- Romain Mechain