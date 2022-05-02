from flask import render_template,request,redirect,url_for
from app.model import Articles
from app.request import get_articles,search_news
from .import main


@main.route('/')
def index():

    articles = get_articles()

    title = 'KUWTCNA Articles'

    
    return render_template('index.html', title = title, news= articles)
    

@main.route('/search/<article_name>')
def search(article_name):
    '''
    View function to display the search results
    '''
    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('search',article_name=search_news))
    else:
     article_name_list = article_name.split(" ")
     article_name_format = "+".join(article_name_list)
     searched_article = search_news(article_name_format)
     title = f'search results for {article_name}'
     return render_template('search.html',article = searched_article)    