from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask import Flask
from sqlalchemy.orm import relationship
import sqlalchemy as db

from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager
from flask import Flask
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:8889/projetOrmApi'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/projetOrmApi'
app.secret_key = "super secret key"
bootstrap = Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'
db = SQLAlchemy()
db.init_app (app) 



@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    commentaires = relationship('Commentaire', backref='user')
    like = db.relationship('Like', backref='user', uselist=False)
    dislike = db.relationship('Dislike', backref='user', uselist=False)
    def __repr__(self):
        return '<Users %r>' % self.id


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    image_article = db.Column(db.Text, nullable=True)
    auteur_article = db.Column(db.String(200), nullable=True, default="Inconnu")
    title_article = db.Column(db.Text, nullable=False)
    desc_article = db.Column(db.Text, nullable=False)
    content_article = db.Column(db.Text, nullable=False)
    date_article = db.Column(db.Date, nullable=False)
    source_article = db.Column(db.String(50), nullable=False)
    like_article = db.Column(db.Integer, nullable=True, default=0)
    dislike_article = db.Column(db.Integer, nullable=True, default=0)
    commentaires = relationship('Commentaire', backref='article')
    like = relationship('Like', backref='article')
    dislike = relationship('Dislike', backref='article')
    def __repr__(self):
        return '<Article %r>' % self.id

class Like(db.Model):
    __tablename__ = 'like'
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))

class Dislike(db.Model):
    __tablename__ = 'dislike'
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))

class Commentaire(db.Model):
    __tablename__ = 'commentaire'
    id = db.Column(db.Integer, primary_key=True)
    content_com = db.Column(db.Text, nullable=False)
    date_com = db.Column(db.Date, nullable=False)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))
    def __repr__(self):
        return '<Commentaire %r>' % self.id_com




with app.app_context():
    db.create_all()


from app.main.routes import main
from app.posts.routes import posts
from app.users.routes import users

app.register_blueprint(main)
app.register_blueprint(posts)
app.register_blueprint(users)