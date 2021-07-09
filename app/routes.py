from flask import render_template, url_for, redirect

from app import app


@app.route('/')
@app.route('/home')
def home():
    climb = [{
        'climb_name': 'Unknown OffWidth Willard Pond',
        'location': 'Willard Pond',
        'description': '''Start with a decent hand and fist jam. Kick a foot up into the constriction 
                        and try to find the good holds''',
        'getting_there': 'Just dream...',
        'picture': 'unknown_willard.jpg'
    }]
    return render_template('home.html', title='OW! NH', climbs=climb)


