from flask import Flask,render_template
import pymysql
import json
import configparser
import sqlite3
from project1_env.Lib.shutil import Error

config = configparser.ConfigParser()
config.read('variables.cfg')
USERNAME = config.get('DATOS','USERNAME')
PASSWORD = config.get('DATOS','PASSWORD')
HOST  = config.get('DATOS','HOST')
DB = config.get('DATOS',"DB_APP")

app = Flask(__name__)

"""
api/v1/countries/:id/states/:id/cities/:id

"""

@app.route('/index')
def index():
    return render_template("index.html")


def create_connection():
    db = pymysql.connect("localhost", "root", "", "upch")
    #db = pymysql.connect(HOST, USERNAME, PASSWORD, DB)
    #db = pymysql.connect(db=DB, user=USERNAME, passwd=PASSWORD, host=HOST, port=3306)
    return  db

@app.route('/api/v1/contries',methods=['GET'])
def Paises():
    cursor = create_connection().cursor()
    cursor.execute("SELECT id,name from countries")
    data = cursor.fetchall()
    m = json.dumps(data)
    return m

@app.route('/api/v1/contries/<id>/states')
def Estados(id):
    cursor = create_connection().cursor()
    cursor.execute("SELECT id,name from states where country_id= '%s'" %(id))
    data = cursor.fetchall()
    m = json.dumps(data)
    return m

@app.route('/api/v1/states/<id>/cities')
def Cities(id):
    cursor = create_connection().cursor()
    #SELECT * from cities where state_id =
    cursor.execute("SELECT id,name from cities where state_id = '%s'"%(id))
    data = cursor.fetchall()
    m = json.dumps(data)
    return m


if __name__ == '__main__':
    app.run()
