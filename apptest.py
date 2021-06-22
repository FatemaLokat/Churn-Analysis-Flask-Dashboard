from pymongo import mongo_client
import pytest
from ECenter_Dashboard import app,mongo,PyMongo,Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
# from ECenter_Dashboard import flask
# from Dashboard_flask import app as flask_app
 

def test_valid_login():
    response = app.test_client().post('/login')
    app.config["BUNDLE_ERRORS"] = True
    app.secret_key = 'mysecret'

    app.config['MONGO_DBNAME'] = 'Fatema'
    app.config['MONGO_URI'] = 'mongodb+srv://Fatema:Fatema786@login.tli64.mongodb.net/test'

    mongo = PyMongo(app)
    app.config['USERNAME'] = 'Zia_8970231'
    app.config['PASSWORD'] = 'Zia231'
    app.config['WTF_CSRF_ENABLED'] = False
    assert response.status_code == 400
 
def test_valid_logout():
    response = app.test_client().get('/')
    assert response.status_code == 200
    #assert b"Goodbye!" in response.data
    #assert b"Flask User Management" in response.data
    #assert b"Logout" not in response.data
    #assert b"Login" in response.data
    #assert b"Register" in response.data
"""
def test_valid_register():
    response = app.test_client().post('/register', data=dict(name='Maya_74561021', password='Zoya0021'))
    #data=dict(name='Zoya_74560021', password='Zoya0021')
    assert response.status_code == 200
"""
def test_dashboard():
    response = app.test_client().get('/dashboard')
    assert response.status_code == 200