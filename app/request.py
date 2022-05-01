import urllib.request, json

from .model import Articles

# getting the API_KEY
api_key = None

# getting the URL
base_url = None


def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_articles():
    '''
    This will get the JSON response to the URL request
    '''
    get_articles_url = base_url.format(api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            print(articles_results_list)
            articles_results = process_results(articles_results_list)
            

    return articles_results

