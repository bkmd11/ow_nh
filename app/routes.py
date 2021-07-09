from flask import render_template, url_for, redirect

from app import app


@app.route('/')
@app.route('/home')
def index():
    return 'SPAM'
