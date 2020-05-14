# ProjetOrmApi

- git clone 

- Importez le fichier environment.yml dans "Environments" sur Anaconda pour créer un environnement dédié à l'application.

- Créez une base de donnée "projetOrmApi" complètement vide sur phpMyAdmin.
    
    si vous êtes sur Wamp utiliser la ligne suivante : 
      app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/projetOrmApi'
    
    si vous êtes sur Mamp utiliser la ligne suivante : 
      app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:8889/projetOrmApi'
      
- Ouvrez un terminal depuis l'environnement "projetOrmApi" 

- Allez dans le dossier "ProjetOrmApi" à l'aide de la commande cd

- Faites un python projetOrmApi.py

- Plus qu'à admirer le site Web depuis localhost:5000
