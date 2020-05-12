from flask import Flask, render_template, url_for, request, jsonify, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
from sqlalchemy import Table, Column, Integer, String, MetaData, Date, Text
import requests
import json
import datetime
import sqlalchemy as db

app = Flask(__name__)
bcrypt = Bcrypt(app)
meta = MetaData(app)
app.secret_key = "super secret key"
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:8889/projetFlask'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/projetFlask'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)




class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_article = db.Column(db.Text, nullable=False)
    auteur_article = db.Column(db.String(50), nullable=True)
    title_article = db.Column(db.Text, nullable=False)
    desc_article = db.Column(db.Text, nullable=False)
    content_article = db.Column(db.Text, nullable=False)
    date_article = db.Column(db.Date, nullable=False)
    source_article = db.Column(db.String(50), nullable=False)
    def __repr__(self):
        return '<Article %r>' % self.id_article

class Commentaire(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content_com = db.Column(db.Text, nullable=False)
    date_com = db.Column(db.Date, nullable=False)
    #un commentaire pour un user
    #un article a plusieur commentaire
    def __repr__(self):
        return '<Commentaire %r>' % self.id_com

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(60), unique=True)

db.create_all()
db.session.commit()

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

@app.route("/login")
def loginInit():
    return render_template('login.html')

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == "POST":
        usernameForm = request.form['username']
        passwordForm = request.form['password']
        users = Users.query.filter_by(username=usernameForm).first()
        if users is None:
            error = "Aucun compte avec " + usernameForm
        else:
            password = users.password
            if bcrypt.check_password_hash(password, passwordForm):
                login_user(users)
                return redirect(url_for('apiNews'))
            else:
                error = "Le mot de passe est incorrect"
    return render_template('login.html', error=error)

@app.route("/logout")
def logout():
    if current_user.is_authenticated:
        logout_user()
        return redirect(url_for('login'))
    else: 
        return redirect(url_for('login'))

@app.route("/sign")
def signInit():
    return render_template('sign.html')

@app.route("/sign", methods=['POST'])
def sign():
    username = request.form['username']
    password = request.form['password']
    password  = bcrypt.generate_password_hash( password ) 
    users = Users.query.filter_by(username=username).first()
    if users is None:
        users = Users(username=username, password=password)
        db.session.add(users)
        db.session.commit()
        login_user(users)
        return render_template('news.html')
    else:
        error = "Username déjà utilisé"
    return render_template('sign.html', error=error)

@app.route("/")
def home():
    users = Users.query.all() 
    return render_template('home.html', users=users)

@app.route("/news")
def apiNews():
    NEWS_API_URL = "http://newsapi.org/v2/top-headlines?sources=google-news-fr&apiKey=3a38e22cd69b41fcbd7782a981876815"
    response = requests.get(NEWS_API_URL)
    content = json.loads(response.content.decode('utf-8'))
    news = content["articles"]
    for new in news:
        image = new['urlToImage']
        auteur = new['author']
        title = new['title']
        desc = new['description']
        content = new['content']
        source = new['source']['name']
        date = new['publishedAt']
        date = date[0:10]
        verifArt = Article.query.filter_by(image_article=image).first()
        if verifArt is None:
            article = Article(image_article=image, auteur_article=auteur, title_article=title, desc_article=desc, content_article=content, date_article=date, source_article=source)
            db.session.add(article)
            db.session.commit()
        allArticles = Article.query.order_by(Article.id).all()
        allArticles = allArticles[::-1]
    return render_template('news.html', allArticles=allArticles)

@app.route("/new", methods=['GET','POST'])
def New():
    idArt = request.args.get('id')
    articleSelect = Article.query.filter_by(id=idArt).first()
    allCom = Commentaire.query.all()
    allCom = allCom[::-1]
    return render_template('new.html', articleSelect=articleSelect, allCom=allCom)


@app.route("/commentaire", methods=['GET','POST'])
def Comm():
    if current_user.is_authenticated:
        commentaireForm = request.form['comm']
        date = datetime.datetime.now()
        commentaire = Commentaire(content_com=commentaireForm, date_com=date)
        db.session.add(commentaire)
        db.session.commit()
    else:
        return redirect(url_for('login'))
    idArt = request.args.get('id')
    articleSelect = Article.query.filter_by(id=idArt).first()
    allCom = Commentaire.query.all()
    allCom = allCom[::-1]
    return render_template('new.html', articleSelect=articleSelect, allCom=allCom)

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
