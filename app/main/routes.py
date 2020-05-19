from flask import Blueprint,Flask, render_template, request, flash, redirect
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from app import Article
from app import db
from flask_sqlalchemy import SQLAlchemy
import requests
import datetime
import json

main = Blueprint('main',__name__)
db = SQLAlchemy()


@main.route("/")
def home():
    NEWS_API_URL = "http://newsapi.org/v2/top-headlines?sources=google-news-fr&apiKey=3a38e22cd69b41fcbd7782a981876815"
    METEO_API_URL = "http://api.openweathermap.org/data/2.5/weather?q=paris,fr&appid=86bf118c5132d80d5f656123fe6302db"
    COVID_API_URL_WORLD = "https://api.covid19api.com/world/total"
    responseWorld = requests.get(COVID_API_URL_WORLD)
    contentWorld = json.loads(responseWorld.content)
    responseNews = requests.get(NEWS_API_URL)
    contentNews = json.loads(responseNews.content.decode('utf-8'))
    responseMeteo = requests.get(METEO_API_URL)
    contentMeteo = json.loads(responseMeteo.content.decode('utf-8'))
    news = contentNews["articles"]
    news = news[::-1]
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
        allArticles = allArticles[0:4]
    main = contentMeteo['main']
    cloud = contentMeteo['clouds']
    temp = main['temp'] - 273.15
    temp = round(temp, 2)
    press = main['pressure']
    humi = main['humidity']
    wind = contentMeteo['wind']['speed'] * 1.792
    wind = round(wind, 2)
    nuage = cloud['all']
    date = datetime.datetime.now().strftime('%d-%m-%Y')
    confirme = contentWorld['TotalConfirmed']
    death = contentWorld['TotalDeaths']
    recover = contentWorld['TotalRecovered']
    return render_template('home.html', allArticles=allArticles, nuage=nuage, main=main, temp=temp, press=press, humi=humi, wind=wind, date=date,confirme=confirme, death=death, recover=recover)



@main.route("/meteo", methods=['GET', 'POST'])
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
    press = main['pressure']
    humi = main['humidity']
    wind = content['wind']['speed'] * 1.792
    wind = round(wind, 2)
    nuage = cloud['all']
    date = datetime.datetime.now().strftime('%d-%m-%Y')
    return render_template('meteo.html', ville=ville, nuage=nuage, main=main, temp=temp, press=press, humi=humi, wind=wind, date=date)      


    
    
@main.route("/covid-19")
def covidInit():
    COVID_API_URL_WORLD = "https://api.covid19api.com/world/total"
    responseWorld = requests.get(COVID_API_URL_WORLD)
    contentWorld = json.loads(responseWorld.content)
    confirme = contentWorld['TotalConfirmed']
    death = contentWorld['TotalDeaths']
    recover = contentWorld['TotalRecovered']
    COVID_API_URL_PAYS = "https://api.covid19api.com/summary"
    responsePays = requests.get(COVID_API_URL_PAYS)
    contentPays = json.loads(responsePays.content)
    countries = contentPays["Countries"]
    return render_template('covid.html', countries=countries, confirme=confirme, death=death, recover=recover)


@main.route("/covid-19",  methods=['POST'])
def apiCovid():
    COVID_API_URL_PAYS = "https://api.covid19api.com/summary"
    responsePays = requests.get(COVID_API_URL_PAYS)
    contentPays = json.loads(responsePays.content)
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
    content = json.loads(response.content)
    return render_template('covid.html', content=content, pays=pays, countries=countries, confirme=confirme, death=death, recover=recover)
   
