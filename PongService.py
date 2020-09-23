import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret key here'
    
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'message': 'Page Not Found'}), 404
    
@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({'message': 'Servier Error'}), 500

@app.route('/pong', methods=['GET'])
def pong():
    return jsonify({'message': 'Server has ponged'}), 200