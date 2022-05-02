import unittest
from app.model import Articles



class ArticlesTest(unittest.TestCase):
    """
    Test class to test the behavior of the News class
    """

    def setUp(self):
        """
        Set up method that will run before every test
        """
        self.articles_object = Articles("")

    def test_instance(self):
        self.assertTrue(isinstance(self.articles_object, Articles))

    def test_init(self):
        '''
        test_init test case to test if the News object is initialized properly
        '''

        self.assertEqual(self.articles_object.title, "The many lives of Billy Wilder. - Noah Isenberg")
        self.assertEqual(self.articles_object.description,
                         "As a young man, Wilder fashioned himself in the image of the American hard-boiled newspaperman with a ubiquitous snap-brim hat and a rhetorical brio, spit, and swagger. ")
        self.assertEqual(self.articles_object.imageurl,
                         "https://www.thenation.com/wp-content/uploads/2022/04/Isenberg-Wilder-illo-getty_img.jpg")
        self.assertEqual(self.articles_object.content,
                         "Among the many stories that Billy Wilder liked to tell late in his life was the one he recounted with great gusto the night he received the Irving G. Thalberg Memorial Award at the 1988 Academy Awards ceremony.Shortly... [+1500 chars]")
        self.assertEqual(self.articles_object.date, "2022-05-01T23:38:08Z")
        self.assertEqual(self.articles_object.url, "https://www.thenation.com/article/culture/billy-wilder-biography/index.html")
