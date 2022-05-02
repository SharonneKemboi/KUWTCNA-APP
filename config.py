import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=e1748305ab8746c89ef63618e01e7b8e'
    NEWS_API_KEY = os.environ.get('e1748305ab8746c89ef63618e01e7b8e')



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


config_options = {
    'development' : DevConfig,
    'production' : ProdConfig
}