
from ast import dump
from itertools import count
import os
from unicodedata import category
from flask import Flask, abort, jsonify, Request, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import sys
from dotenv import load_dotenv
#Pour protéger le mot de passe
from urllib.parse import quote_plus
load_dotenv()

app= Flask(__name__)
password = quote_plus(os.getenv('db_password'))
host = quote_plus(os.getenv('hostname'))
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:{}@{}:5432/bibliotheque'.format(password, host)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)


class Categorie(db.Model):
    __tablename__="categories"
    id_cat = db.Column(db.Integer, primary_key=True)
    libelle_categorie= db.Column(db.String(50), nullable=False)
    id_livre = db.relationship('Livre', backref='categories', lazy=True)
            
    def update(self):
        db.session.commit() 
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format_cat(self):
        return {
        'id':self.id_cat,
        'libelle_categorie':self.libelle_categorie
        }

class Livre(db.Model):
    __tablename__="livres"
    id = db.Column(db.Integer, primary_key= True)
    isbn = db.Column(db.String(25), nullable= False)
    titre = db.Column(db.String(50), nullable= False)
    date_publication= db.Column(db.DateTime, nullable= False)
    auteur = db.Column(db.String(30), nullable= False)
    editeur = db.Column(db.String(50), nullable= False)
    id_cat = db.Column(db.Integer, db.ForeignKey('categories.id_cat'), nullable= False)

            
    def update(self):
        db.session.commit() 
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
       
    def format_liv(self):
        return {
        'id':self.id,
        'id_cat':self.id_cat,
        'isbn':self.isbn,
        'titre':self.titre,
        'date':self.date_publication,
        'auteur':self.auteur,
        'editeur':self.editeur
            }
            
    


db.create_all()

#####################################
#
#   Endpoint La liste des Livres
#
#####################################

@app.route('/livres')
def liste_livre():
    livre=Livre.query.all()
    formater=[liv.format_liv() for liv in livre]
    return jsonify(
        {
            'Success':True,
            'Total_de_livre':len(livre),
            'Livres':formater
        }
    )
#render_template('index.html', data=livre)
#####################################
#
#   Endpoint Rechercher un livre
#
#####################################


@app.route('/livres/<int:id>')
def rechercher(id):

    livre =Livre.query.get(id)
    if livre is None:
        abort(404)
    else:
        return jsonify(
            {
                'success':True,
                'Identifiant':id,
                'Livre':livre.format_liv()

            }
        )

#########################################################
#
#   Endpoint Lister la liste des livres d’une catégorie
#
#########################################################


@app.route('/categori_livre/<int:id_ca>')
def recuperer(id_ca):
    categorie = Categorie.query.get(id_ca)
        
    if categorie is None:
        abort(404)
    else:
        query = Livre.query.filter_by(id_cat = id_ca)
        livre = query.all()
        formater=[liv.format_liv() for liv in livre]
        return jsonify(
            {
                'success':True,
                'Id_Categorie':id_ca,
                'Total_Livre':query.count(),
                'Livre':formater
            }
        )
   


#####################################
#
#   Endpoint La liste des catégories
#
#####################################

@app.route('/categories')
def lister_ts_categorie():
    categorie = Categorie.query.all()
    formated_categories=[ cat.format_cat() for cat in categorie]
    return jsonify(
        {
            'success':True,
            'Tolat_de_Livre':len(categorie),
            'categories': formated_categories
        }
    )
#########################################################
#
#   Endpoint  Chercher une catégorie par son id
#########################################################
    

@app.route('/categories/<int:id_cat>')
def recherche_cat(id_cat):
    categorie = Categorie.query.get(id_cat)
    #formatCat=[cat.format for cat in categorie]
    if categorie is None:
        abort(404)
    else:
        return jsonify(
            {
                'success':True,
                'Id_cat':id_cat,
                'Categorie':categorie.format_cat()
            }
        )


#########################################################
#
#   Endpoint  Supprimer un livre
#
#########################################################

@app.route('/suppression_livre/<int:id>')
def suppression_livre(id):
    livre = Livre.query.get(id)
    if livre is None:
        abort(404)
    else :
        livre.delete()
        return jsonify(
            {
                'success':True,
                'Id':id,
                'Livre_Supprime':livre.format_liv(),
                'total_livre':Livre.query.count()

            }
        )


#########################################################
#
#   Endpoint  Supprimer une categorie
#
#########################################################
@app.route('/suppression_categorie/<int:id_ca>')
def suppression_categorie(id_ca):
    categorie = Categorie.query.get(id_ca)
    if categorie is None:
        abort(404)
    else :
        livre= Livre.query.filter_by(id_cat = id_ca)
        livre.delete()
        categorie.delete()
        formater=[liv.format_liv() for liv in livre]
        return jsonify(
            {
                'success':True,
                'Id':id_ca,
                'Categorie':categorie.format_cat(),
                'livre_categorie':formater,
                'total_livre':Categorie.query.count()
            }
        )
    


#########################################################
#
#   Endpoint  Modifier les informations d’un livre
#
#########################################################

@app.route('/modifier_livre/<int:id>',methods=['PATCH'])
def modifier_livre(id):
    
    livre=Livre.query.get(id)
    if livre is None:
        abort(404)
    else:
        body=request.get_json()
        livre.isbn=body.get('id')
        livre.isbn=body.get('isbn')
        livre.titre=body.get('titre')
        livre.date_publication=body.get('date_publication')
        livre.auteur=body.get('auteur')
        livre.editeur=body.get('editeur')
        livre.id_cat=body.get('id_cat')
        livre.update()
        return jsonify({
            'success':True,
            'updated_id':id,
            'livre':livre.format_liv()
            }
        )

#########################################################
#
#   Endpoint Modifier le libellé d’une categorie
#
#########################################################
@app.route('/modifier_categorie/<int:id_cat>',methods=['PATCH'])
def modifier_categorie(id_cat):
    #try:
    categorie=Categorie.query.get(id_cat)
    if categorie is None:
        abort(404)
    else:
        body=request.get_json()
        categorie.libelle_categorie=body.get('libelle_categorie')
        categorie.update()
        return jsonify({
            'success':True,
            'updated_id':id_cat,
            'catégorie':categorie.format_cat()
            }
        )
    #except:
        abort(400)
   

@app.errorhandler(404)
def not_fond(error):
    return jsonify( {
        'success':False,
        'error':404,
        'message':'Not Found'
    }), 404

@app.errorhandler(500)
def not_fond(error):
    return jsonify( {
        'success':False,
        'error':500,
        'message':'Internal server error'
    }), 500