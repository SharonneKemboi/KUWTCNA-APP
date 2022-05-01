class Articles:
    '''
    News Class  to define the news objects
    '''

    def __init__(self, title, description, imageurl, content, date, url):
        self.title = title
        self.description = description
        self.imageurl = imageurl
        self.content = content
        self.date = date
        self.url = url

