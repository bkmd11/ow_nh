from flask import render_template, url_for, redirect, flash, request
from flask_login import current_user, login_user, login_required

from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename

from app import app, db
from app.forms import LoginForm, NewRouteForm
from app.models import Admin, Climb

import os


@app.route('/')
@app.route('/home')
def home():
    climb = Climb.query.all()
    return render_template('home.html', title='OW! NH', climbs=climb)


@app.route('/admin_login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user_email = Admin.query.filter_by(email=form.email.data).first()
        if user_email is None or not user_email.check_password(form.password.data):
            flash('Invalid credentials')
            return redirect(url_for('admin_login'))
        login_user(user_email, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('login.html', title='Admin', form=form)


@app.route('/add_climb', methods=['GET', 'POST'])
@login_required
def add_climb():
    form = NewRouteForm()
    if form.validate_on_submit():
        name = form.name.data
        location = form.location.data
        description = form.description.data
        directions = form.directions.data
        picture_file = request.files['picture']
        picture_name = secure_filename(picture_file.filename)

        picture_file.save(os.path.join('app/static/', picture_name))

        new_climb = Climb(climb_name=name,
                          location=location,
                          picture_path=picture_name,
                          description=description,
                          getting_there=directions)

        db.session.add(new_climb)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_climb.html', form=form)
# TODO need to build in security to this
