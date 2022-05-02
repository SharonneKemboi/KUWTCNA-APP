from flask import render_template
from app import app
from urllib import error

@app.errorhandler(404)
def four_Ow_four(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('404.html'),404


@app.errorhandler(error.HTTPError)
def http_error(error):
    return render_template('404.html'), 404