# ProjetOrmApi

GROUPE A6:
Aaron Saksik
Alexis Morin
Yohan Stoecklé

Procédure de lancement du projet:

- git clone https://github.com/Aaronsaksik95/ProjetOrmApi.git

-  Tapez la commande pip install -r requirements.txt sur le terminal.

- Créez une base de donnée "projetOrmApi" complètement vide sur phpMyAdmin.
    
    si vous êtes sur Wamp utiliser la ligne suivante : 
      app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/projetOrmApi'
    
    si vous êtes sur Mamp utiliser la ligne suivante : 
      app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:8889/projetOrmApi'
      
- Ouvrez un terminal depuis l'environnement "projetOrmApi" 

- Allez dans le dossier "ProjetOrmApi" à l'aide de la commande cd

- Faites un python app.py

- Plus qu'à admirer le site Web depuis localhost:5000
