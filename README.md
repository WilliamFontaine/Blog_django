# Blog_django
 
## Lancement du blog Django avec Docker:  

**Dans un premier temps, il faut avoir docker d'installer et correctement configuré sur sa machine**  

* Il faut d'abord ouvrir un terminal et se rendre dans le répertoire où se trouve manage.py. 

* On va ensuite taper la commande **`docker build --tag python-django .`**. Elle permet de créer un image pour le docker.  

* On tape ensuite la commande suivante: **`docker run --publish 8000:8000 python-django`**. Elle permet de créer un container pour notre site.  

* Une fois cette cela fait, il suffit de se rendre à l'adresse suivante: **http://127.0.0.1:8000/**  

* Il ne reste plus qu'à naviguer sur le site !  

## Lancement du blog Django sans Docker:  

* Ll faut d'abord ouvrir un terminal et se rendre dans le répertoire où se trouve manage.py.  

* On va ensuite exécuter la commande suivante avec python:  
     **`python manage.py migrate`**    
  Cette commande nous permet d'effectuer les migrations nécessaires au bon fonctionnement du blog s'il y en a.  
  
* On effectue ensuite la commande suivante:  
     **`python manage.py runserver`**    
     
* Pour accéder au site, il suffit de se rendre sur son navigateur et d'entrer l'url suivante:  
     **http://127.0.0.1:8000/**    
     
* Il ne reste plus qu'à naviguer sur le site !  

## Identifiants:  
* Vous pouvez accéder à la page d'administration avec les identifiants suivants:  
    username: admin  
    password: admin
