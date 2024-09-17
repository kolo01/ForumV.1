
# Documentation Du Projet de Groupe FORUM V1
****
Ce projet vise à etablir les bases pour la realisation du backend d'un forum
****
## Realiser par:
   | Nom | Prenom | Profil GitHub |
   | ----------- | ----------- | ----------- |
   |  TIAN | Bi Toa Ange |[tayane1](https://github.com/tayane1)  |
   | NYOA | 	Ama Marie-Colombe |[Marie-Colombe](https://github.com/Marie-Colombe) |
   | KONE | KOLOTIOLOMAN D. |[kolo01](https://github.com/kolo01) |
    
****
## Fonctionnalités

- #### Gestion du forum
#
            - Création d'un nouveau forum
            - Liste des forums existants
            - Récupération des détails d'un forum
            
 - #### Gestion des sujets
#
            - Création d'un nouveau sujet dans un forum
            - Liste des sujets d'un forum
            - Récupération des détails d'un sujet
           


- #### Gestion des messages
#
            - Création d'un nouveau message dans un sujet
            - Liste des messages d'un sujet
          

****

## Comment executer notre application

- ### Prerequis
    Avoir `Python` installé sur sa machine, verifiable en tapant dans son terminal 
    ````sh
    python --version 
    ````` 
    Vous devez avoir un resultat similaire a cette ligne (la version peut ne pas etre la même)
            ![Imgur](https://i.imgur.com/EHqP7VE.png)
    - Si pas fait au préalable, vous pouvez télécharger le fichier d'installation sur [ le site officiel de PYTHON](https://www.python.org/downloads/)
             ![Imgur](https://i.imgur.com/A2iH1rj.png)
    - Avoir  `Postgresql` installé sur sa machine , si vous l'avez pas, vous pouvez le telecharger [ICI](https://www.postgresql.org/download/)
    - Avoir  `GIT` installé sur sa machine (`Optionnel`), si vous l'avez pas, vous pouvez le telecharger [ICI](https://git-scm.com/downloads)


- #### Créer un dosssier pour contenir tout notre projet
- #### Ouvrir un terminal et se deplacer jusqu'au dossier 
   
                      
### ***Tout ce qui suis doit être saisie dans le terminal***
- >  #### Creer l'environnement virtuel avec 
    #
    ````sh
    python -m venv env
    ````
        
        
- > #### Activer son environnement virtuel
    #
    ````sh 
    .\env\Scripts\activate
    ```` 
- > #### Telecharger le projet avec  [ce lien](https://github.com/kolo01/ForumV.1/archive/refs/heads/main.zip) ou avec la commande
   #
    ````sh 
    git clone https://github.com/kolo01/ForumV.1.git
    ```` 
- > ### Apres telechargement, s'assurer d'avoir l'environnement virtuel ainsi que les dossiers et fichiers du projet telecharges dans le  dossier (celui creer au depart et sur qui pointe notre terminal)

- > ### Vous devrez avoir ceci
    ![Imgur](https://i.imgur.com/o6lo6PN.png)
    ###### Si ce n'est pas le cas, veuillez deplacer le dossier src et le fichier requirements.txt

- > #### Installer les dependances de notre projet
    ###
     ````sh 
    pip install -r requirements.txt
    ```` 

- > #### On s'assure d'avoir creer une base de donnée dans Postegresql et on verifie la configuration dans le fichier settings.py contenu dans le dossier forum.

    ![Imgur](https://i.imgur.com/zmFELG2.png)





- > #### On lance nos migrations avec 
    ###
    ````sh 
        python src\manage.py makemigrations 
    ```` 
    ````sh
        python src\manage.py migrate 
    ```` 

- > #### On lance notre projet 
    ###
    ````sh  
    python src\manage.py runserver
     ```` 
    
- > #### On va dans le navigateur et on tape
    ###
    ````sh
    http://127.0.0.1:8000
    ````
   
