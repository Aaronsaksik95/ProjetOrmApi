from flask import Flask, render_template, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
import requests
import json
import datetime
import sqlalchemy as db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:8889/projetApiOrm'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/projetApiOrm'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Article(db.Model):
    id_article = db.Column(db.Integer, primary_key=True)
    title_article = db.Column(db.Text, nullable=False)
    content_article = db.Column(db.Text, nullable=False)
    date_article = db.Column(db.DateTime, nullable=False)
    journal_article = db.Column(db.String(50), nullable=False)
    def __repr__(self):
        return '<Article %r>' % self.id_article

class Commentaire(db.Model):
    id_com = db.Column(db.Integer, primary_key=True)
    content_com = db.Column(db.Text, nullable=False)
    date_com = db.Column(db.DateTime, nullable=False)
    def __repr__(self):
        return '<Commentaire %r>' % self.id_com

class Users(db.Model):
    id_user = db.Column(db.Integer, primary_key=True)
    nom_user = db.Column(db.String(50), nullable=False)
    prenom_user = db.Column(db.String(50), nullable=False)
    email_user = db.Column(db.String(100), nullable=False)
    password_user = db.Column(db.Text, nullable=False)
    def __repr__(self):
        return '<Users %r>' % self.id_user


@app.route("/")
def home():
    users = Users.query.all() 
    return render_template('home.html', users=users)

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/sign", methods=['POST'])
def sign():
    nom = request.form['nom']
    prenom = request.form['prenom']
    mail = request.form['mail']
    password = request.form['password']
    u = Users(nom, prenom, mail, password)
    db.session.add(u)
    db.session.commit()
    return render_template('sign.html')

@app.route("/news")
def apiNews():
    return render_template('news.html')


@app.route("/meteo", methods=['GET', 'POST'])
def apiMeteo():
   
    if request.method == 'GET':
       ville = request.args.get('name')
    elif request.method == 'POST':
       ville = request.form['ville']
    METEO_API_URL = "http://api.openweathermap.org/data/2.5/weather?q={},fr&appid=86bf118c5132d80d5f656123fe6302db".format(
        ville)
    response = requests.get(METEO_API_URL)
    content = json.loads(response.content.decode('utf-8'))
    if response.status_code != 200:
        return render_template("errors/500.html"), 500
    main = content['main']
    cloud = content['clouds']
    temp = main['temp'] - 273.15
    temp = round(temp, 2)
    temp_min = main['temp_min'] - 273.15
    temp_max = main['temp_max'] - 273.15
    press = main['pressure']
    humi = main['humidity']
    wind = content['wind']['speed'] * 1.792
    wind = round(wind, 2)
    nuage = cloud['all']
    date = datetime.datetime.now().strftime('%d-%m-%Y')
    return render_template('meteo.html', ville=ville, nuage=nuage, main=main, temp=temp, temp_min=temp_min, temp_max=temp_max, press=press, humi=humi, wind=wind, date=date)      


    
    
@app.route("/covid-19")
def covidInit():
    COVID_API_URL_WORLD = "https://api.covid19api.com/world/total"
    responseWorld = requests.get(COVID_API_URL_WORLD)
    contentWorld = json.loads(responseWorld.content.decode('utf-8'))
    confirme = contentWorld['TotalConfirmed']
    death = contentWorld['TotalDeaths']
    recover = contentWorld['TotalRecovered']
    COVID_API_URL_PAYS = "https://api.covid19api.com/summary"
    responsePays = requests.get(COVID_API_URL_PAYS)
    contentPays = json.loads(responsePays.content.decode('utf-8'))
    countries = contentPays["Countries"]
    return render_template('covid.html', countries=countries, confirme=confirme, death=death, recover=recover)


@app.route("/covid-19",  methods=['POST'])
def apiCovid():
    COVID_API_URL_PAYS = "https://api.covid19api.com/summary"
    responsePays = requests.get(COVID_API_URL_PAYS)
    contentPays = json.loads(responsePays.content.decode('utf-8'))
    countries = contentPays["Countries"]
    glob = contentPays["Global"]
    confirme = glob['TotalConfirmed']
    death = glob['TotalDeaths']
    recover = glob['TotalRecovered']
    pays = request.form['pays']
    date = request.form['date'] + "T00:00:00Z"
    COVID_API_URL = "https://api.covid19api.com/live/country/{}/status/confirmed/date/{}".format(
        pays, date)
    response = requests.get(COVID_API_URL)
    content = json.loads(response.content.decode('utf-8'))
    return render_template('covid.html', content=content, pays=pays, countries=countries, confirme=confirme, death=death, recover=recover)
   

@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
