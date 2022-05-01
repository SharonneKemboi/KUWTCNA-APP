from turtle import title
from flask import render_template
from app.model import Articles

from app.request import get_articles
from .import main

@main.route('/')
def index():

    articles = get_articles()

    title = 'KUWTCNA Articles'
    return render_template('index.html', title = title, news= articles)