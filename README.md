# Management_Bibliotheque_Api

API BIBLIOTHEQUE DEVELOPPEMENT PYTHON FLASK
Motivations
Cette API permet de gérer une table etudiants créée dans la base de données.

Getting Started
Installing Dependencies
Python 3.9.7
pip 20.3.4 from /usr/lib/python3/dist-packages/pip (python 3.9)
Si vous n'avez pas python installé, merci de suivre cet URL pour l'installer python docs

Virtual Enviornment
Vous devez installer le package dotenv en utilisant la commande pip install python-dotenv

PIP Dependencies
Exécuter la commande ci dessous pour installer les dépendences

pip install -r requirements.txt
or
pip3 install -r requirements.txt
This will install all of the required packages we selected within the requirements.txt file.

Key Dependencies
Flask is a lightweight backend microservices framework. Flask is required to handle requests and responses.

SQLAlchemy is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

Flask-CORS is the extension we'll use to handle cross origin requests from our frontend server.

Database Setup
With Postgres running, restore a database using the plants_database.sql file provided. From the backend folder in terminal run:

psql bibliotheque < bibliotheque.sql
Running the server
From within the plants_api directory first ensure you are working using your created virtual environment.

To run the server on Linux or Mac, execute:

export FLASK_APP=api.py
export FLASK_ENV=development
flask run
To run the server on Windows, execute:

set FLASK_APP=api.py
set FLASK_ENV=development
flask run
Setting the FLASK_ENV variable to development will detect file changes and restart the server automatically.

Setting the FLASK_APP variable to flaskr directs flask to use the flaskr directory and the __init__.py file to find the application.

API REFERENCE
Getting starter

Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://localhost:5000; which is set as a proxy in frontend configuration.

Error Handling
Errors are retourned as JSON objects in the following format: { "success":False "error": 400 "message":"Bad request" }

The API will return four error types when requests fail: . 400: Bad request . 500: Internal server error . 422: Unprocessable . 404: Not found

Endpoints
. ## GET/livres

GENERAL: cet endpoint permet de récupérer la liste des étudiants 

    
SAMPLE: curl -i http://localhost:5000/livres

"Livres": [
        {
            "auteur": "Sam Smith",
            "date": "Mon, 12 Oct 2015 00:00:00 GMT",
            "editeur": "Mareuil Edition",
            "id": 9,
            "id_cat": 3,
            "isbn": "978-2-3725-4233-3",
            "titre": "Jordan there is no next"
        },
        {
            "auteur": "Jacob Aagaard",
            "date": "Tue, 14 Feb 2017 00:00:00 GMT",
            "editeur": "Olibris",
            "id": 10,
            "id_cat": 3,
            "isbn": "979-1-0971-4032-8",
            "titre": "Attaque et d‚fense aux ‚checs"
        },
        {
            "auteur": "Smith",
            "date": "Mon, 12 Oct 2015 00:00:00 GMT",
            "editeur": "Mareuil Edition",
            "id": 11,
            "id_cat": 3,
            "isbn": "978-2-3725-3",
            "titre": "Jordan"
        },

. ## GET/livres(id)

GENERAL: cet endpoint permet de Chercher un livre en particulier par son id
 
SAMPLE: curl -i http://localhost:5000/livres/3

"Identifiant": 9,
    "Livre": {
        "auteur": "Sam Smith",
        "date": "Mon, 12 Oct 2015 00:00:00 GMT",
        "editeur": "Mareuil Edition",
        "id": 9,
        "id_cat": 3,
        "isbn": "978-2-3725-4233-3",
        "titre": "Jordan there is no next"
    },
    "success": true

. ## GET/categori_livre(id_cat)

GENERAL: cet endpoint permet de Lister la liste des livres d’une catégorie
 
SAMPLE: curl -i 127.0.0.1:5000/categori_livre/14

"Id_Categorie": 14,
    "Livre": [
        {
            "auteur": "Smith",
            "date": "Mon, 12 Oct 2015 00:00:00 GMT",
            "editeur": "Mareuil Edition",
            "id": 25,
            "id_cat": 14,
            "isbn": "978-2-3725-3",
            "titre": "Jordan"
        },
        {
            "auteur": "Armel Job",
            "date": "Thu, 10 Feb 2022 00:00:00 GMT",
            "editeur": "Robert Laffont ",
            "id": 26,
            "id_cat": 14,
            "isbn": "978-2-2212-5958-0",
            "titre": "Un pŠre … soi"
        },
        {
            "auteur": "John Jefferson Selve",
            "date": "Wed, 10 Feb 2021 00:00:00 GMT",
            "editeur": "Grasset",
            "id": 27,
            "id_cat": 14,
            "isbn": "978-2-2468-2894-5",
            "titre": "Meta Carpenter"
        }
    ],
    "Total_Livre": 3,
    "success": true
}

. ## GET/categori_livre(id_cat)

GENERAL: cet endpoint permet de Chercher une catégorie par son id
 
SAMPLE: curl -i 127.0.0.1:5000//categories/3

 "Categorie": {
        "id": 3,
        "libelle_categorie": "Sport loisirs et vie pratique"
    },
    "Id_cat": 3,
    "success": true
}

. ## GET//categories

GENERAL: cet endpoint permet de Lister toutes les catégories

 
SAMPLE: curl -i 127.0.0.1:5000/categories

"Tolat_de_Livre": 7,
    "categories": [
        {
            "id": 3,
            "libelle_categorie": "Sport loisirs et vie pratique"
        },
        {
            "id": 13,
            "libelle_categorie": "Jeunesse"
        },
        {
            "id": 14,
            "libelle_categorie": "Litt‚rature"
        },
        {
            "id": 15,
            "libelle_categorie": "itt‚rature sentimentale"
        },

. ## GET/suppression_livre(id)

GENERAL: cet endpoint permet de Supprimer un livre

 
SAMPLE: curl -i 127.0.0.1:5000/suppression_livre/11

{
   "Id": 9,
    "Livre_Supprime": {
        "auteur": "Sam Smith",
        "date": "Mon, 12 Oct 2015 00:00:00 GMT",
        "editeur": "Mareuil Edition",
        "id": 9,
        "id_cat": 3,
        "isbn": "978-2-3725-4233-3",
        "titre": "Jordan there is no next"
    },
    "success": true,
    "total_livre": 4
}

. ## GET/suppression_categorie(id_cat)

GENERAL: cet endpoint permet de Supprimer un livre

 
SAMPLE: curl -i 127.0.0.1:5000/suppression_categorie/22

{
   "Categorie": {
        "id": 22,
        "libelle_categorie": "Jeunesse"
    },
    "Id": 22,
    "livre_categorie": [],
    "success": true,
    "total_livre": 5
}

. ## PATCH/modifier_livre(id_cat)

GENERAL: cet endpoint permet de Modifier les informations d’un livre

LES INFORMATIIONS  :
{
    "isbn":"978-2-2137-1823-1",
    "titre":"Ma Main",
    "date_publication":"2020-09-12",
    "auteur":"Rousseau",
    "editeur":"Plonb",
    "id_cat":14
}
 
SAMPLE: curl -i 127.0.0.1:5000/modifier_livre/25
{
    "livre": {
        "auteur": "Rousseau",
        "date": "Sat, 12 Sep 2020 00:00:00 GMT",
        "editeur": "Plonb",
        "id": 25,
        "id_cat": 14,
        "isbn": "978-2-2137-1823-1",
        "titre": "Ma Main"
    },
    "success": true,
    "updated_id": 25
}

. ## PATCH/modifier_categorie(id_cat)

GENERAL: cet endpoint permet de Modifier le libellé d’une categorie

LES INFORMATIIONS  :
{ 
    "libelle_categorie":"Fantasy"
}

SAMPLE: curl -i 127.0.0.1:5000/modifier_categorie/14
{
    "catégorie": {
        "id": 14,
        "libelle_categorie": "Fantasy"
    },
    "success": true,
    "updated_id": 14
}


## Testing
To run the tests, run
dropdb bibliotheque createdb bibliotheque psql bibliotheque_test < bibliotheque.sql python test_api.py

