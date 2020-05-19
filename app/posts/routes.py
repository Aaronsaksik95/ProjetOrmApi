from flask import Blueprint,Flask, render_template, url_for, request, flash, redirect
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from app import Article, Commentaire, Users, Like, Dislike
from app import db
import requests
import datetime
import json


posts = Blueprint('posts',__name__)

@posts.route("/news")
def apiNews():
    NEWS_API_URL = "http://newsapi.org/v2/top-headlines?sources=google-news-fr&apiKey=3a38e22cd69b41fcbd7782a981876815"
    response = requests.get(NEWS_API_URL)
    content = json.loads(response.content.decode('utf-8'))
    news = content["articles"]
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
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    return render_template('news.html', allArticles=allArticles, date=date)

@posts.route("/new", methods=['GET','POST'])
def New():
    idArt = request.args.get('id')
    articleSelect = Article.query.filter_by(id=idArt).first()
    if articleSelect is None:
        return render_template('errors/errArt.html')
    allCom = Commentaire.query.filter(Commentaire.article_id.endswith(idArt)).all()
    allCom = allCom[::-1]
    like = Like.query.filter_by(article_id=idArt).count()
    if like is None:
        like = 0
    dislike = Dislike.query.filter_by(article_id=idArt).count()
    if dislike is None:
        dislike = 0
    return render_template('new.html', articleSelect=articleSelect, allCom=allCom, like=like, dislike=dislike)

@posts.route("/like", methods=['GET'])
def like():
    if current_user.is_authenticated:
        idArt = request.args.get('id')
        verifLike = Like.query.filter_by(users_id=current_user.id, article_id=idArt).first()
        verifDislike = Dislike.query.filter_by(users_id=current_user.id, article_id=idArt).first()
        if verifLike is None:
            if verifDislike is None:
                like = Like(users_id=current_user.id, article_id=idArt)
                db.session.add(like)
                db.session.commit()
                flash('Votre like a bien été envoyé.')
            else:
                Dislike.query.filter_by(users_id=current_user.id, article_id=idArt).delete()
                like = Like(users_id=current_user.id, article_id=idArt)
                db.session.add(like)
                db.session.commit()
                flash('Votre like a bien été envoyé.')
        else:
            Like.query.filter_by(users_id=current_user.id, article_id=idArt).delete()
            db.session.commit()
            flash('Votre like a bien été annulé.')
    else: 
        flash('Veuillez vous connecter avant.')
        return redirect(url_for('users.login'))
    return redirect(url_for('.New', id=request.args.get('id')))

@posts.route("/disLike", methods=['GET'])
def DisLike():
    if current_user.is_authenticated:
        idArt = request.args.get('id')
        verifDislike = Dislike.query.filter_by(users_id=current_user.id, article_id=idArt).first()
        verifLike = Like.query.filter_by(users_id=current_user.id, article_id=idArt).first()
        if verifDislike is None:
            if verifLike is None:
                dislike = Dislike(users_id=current_user.id, article_id=idArt)
                db.session.add(dislike)
                db.session.commit()
                flash('Votre dislike a bien été envoyé.')
            else:
                Like.query.filter_by(users_id=current_user.id, article_id=idArt).delete()
                dislike = Dislike(users_id=current_user.id, article_id=idArt)
                db.session.add(dislike)
                db.session.commit()
                flash('Votre dislike a bien été envoyé.')
        else:
            Dislike.query.filter_by(users_id=current_user.id, article_id=idArt).delete()
            db.session.commit()
            flash('Votre dislike a bien été annulé.')
    else: 
        flash('Veuillez vous connecter avant.')
        return redirect(url_for('users.login'))
    return redirect(url_for('.New', id=request.args.get('id')))

@posts.route("/commentaire", methods=['GET','POST'])
def Comm():
    if current_user.is_authenticated:
        commentaireForm = request.form['comm']
        date = datetime.datetime.now()
        commentaire = Commentaire(content_com=commentaireForm, date_com=date, users_id=current_user.id, article_id=request.args.get('id'))
        db.session.add(commentaire)
        db.session.commit()
    else:
        flash('Veuillez vous connecter avant.')
        return redirect(url_for('users.login'))
    flash('Votre commentaire a bien été ajouté.')
    return redirect(url_for('.New', id=request.args.get('id')))

@posts.route("/delete", methods=['GET','POST'])
def delete():
    if current_user.is_authenticated:
        idCom = request.args.get('idCom')
        Commentaire.query.filter_by(id=idCom).delete()
        db.session.commit()
    else:
        flash('Veuillez vous connecter avant.')
        return redirect(url_for('users.login'))
    idArt = request.args.get('idArt')
    flash('Votre commentaire a bien été supprimé.')
    return redirect(url_for('.New', id=idArt))

@posts.route("/update", methods=['GET','POST'])
def update():
    if current_user.is_authenticated:
        idCom = request.args.get('id')
        updCom = request.form['update']
        Commentaire.query.filter_by(id=idCom).update(dict(content_com = updCom))
        db.session.commit()
    else:
        flash('Veuillez vous connecter avant.')
        return redirect(url_for('users.login'))
    idArt = request.args.get('idArt')
    flash('Votre commentaire a bien été modifié.')
    return redirect(url_for('.New', id=idArt))
