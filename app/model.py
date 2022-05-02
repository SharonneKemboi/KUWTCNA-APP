class Articles:
    '''
    News Class  to define the news objects
    '''

    def __init__(self, title, description, urlToImage, content, date, url):
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.content = content
        self.date = date
        self.url = url

