import unittest
from selenium import webdriver
from imdb import imdbsearch
from wiki import wikisearch

class FindLink(unittest.TestCase):
    movie = input("Enter the movie name (EX : RRR, Pushpa: The Rise - Part 1): ")
    def setUp(self):
        self.browser = webdriver.ChromiumEdge()

    def test_link(self):
       imdb=imdbsearch(self.movie, self.browser)
       wiki = wikisearch(self.movie, self.browser)

       assert imdb[0]==wiki[0], "Release date doesn't match"
       assert imdb[1] == wiki[1], "Country doesn't match"

    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()