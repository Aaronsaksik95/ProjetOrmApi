from flask import Blueprint,Flask, render_template, url_for, request, flash, redirect
from app.users.forms import LoginForm, RegisterForm
from app import Article, Commentaire, Users, Like, Dislike
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
users = Blueprint('users',__name__)

@users.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        users = Users.query.filter_by(username=form.username.data).first()
        if users:
            if check_password_hash(users.password, form.password.data):
                login_user(users, remember=form.remember.data)
                flash('Vous êtes bien connecté en tant que ' + form.username.data)
                return redirect(url_for('main.home'))
            else:
                flash('Mot de passe ou identifiant incorrect')
        else:
            flash('Mot de passe ou identifiant incorrect')
    return render_template('login.html', form=form)

@users.route("/deleteProfil")
def DeleteProfil():
    compte = current_user.username
    Commentaire.query.filter_by(users_id=current_user.id).delete()
    Like.query.filter_by(users_id=current_user.id).delete()
    Dislike.query.filter_by(users_id=current_user.id).delete()
    Users.query.filter_by(id=current_user.id).delete()
    db.session.commit()
    logout_user()
    flash('Le compte ' + compte + ' a bien été supprimé.')
    return redirect(url_for('main.home'))


@users.route("/logout")
def Logout():
    compte = current_user.username
    if current_user.is_authenticated:
        logout_user()
        flash('Vous êtes bien déconnecté du compte ' + compte +' .')
        return redirect(url_for('main.home'))
    else: 
        return redirect(url_for('user.login'))

@users.route("/sign", methods=['GET', 'POST'])
def Sign():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        users = Users.query.filter_by(username=form.username.data).first()
        usersEmail = Users.query.filter_by(email=form.email.data).first()
        if users is None:
            if usersEmail is None:
                new_user = Users(username=form.username.data, email=form.email.data, password=hashed_password)
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=form.remember.data)
                flash('Vous êtes bien connecté en tant que ' + form.username.data)
                return redirect(url_for('main.home'))
            else:
                flash('Identifiant ou Email déjà utilisé')
        else:
            flash('Identifiant ou Email déjà utilisé')
        
    return render_template('sign.html', form=form)
