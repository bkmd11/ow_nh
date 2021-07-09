from flask import render_template, url_for, redirect

from app import app


@app.route('/')
@app.route('/home')
def home():
    climb = [{
        'climb_name': 'Coat hanger abortion',
        'location': 'Imagination',
        'description': 'A totally badass climb that will destroy you',
        'getting_there': 'Just dream...',
        'picture':'unknown_willard.jpg'
    }]
    return render_template('home.html', title='OW! NH', climbs=climb)
