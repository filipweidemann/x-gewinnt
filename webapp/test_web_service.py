from webapp.webservice import app
from game import game
import unittest
import time
import sys
from flask import session

sys.path.insert(0, '..')

class WebserviceTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()


    def createGamePage(self):
        return self.app.get('/create')

    def submitGamePage(self, width, height, win, starting):
        return self.app.post('/create', data={'width': width, 'height': height, 'win': win, 'starting': starting}, follow_redirects=True)

    def makeBoard(self):
        return self.app.post('/create')


    def test_main_route(self):
        route = self.app.get('/')
        assert b'Welcome' in route.data
        assert b'Start a new game' in route.data

    def test_create_route(self):
        route = self.createGamePage()
        assert b'Create a new game' in route.data
        assert b'Enter the width of your board' in route.data
        assert b'Enter the height of your board' in route.data
        assert b'Enter the length' in route.data
        assert b'x or o' in route.data
        assert b'Submit' in route.data

    def test_submit_game_page(self):
        route = self.submitGamePage(3,3,3,'x')
        self.assertTrue(route.status_code == 200)
        assert b'3' in route.data
        assert b'x'

    def test_make_board(self):
        game = self.makeBoard()
        self.assertTrue(game.status_code == 200)
        with self.app as a:
            with a.session_transaction() as sess:
                self.assertIsNotNone(sess)
                self.assertTrue(b'x-in-a-row-online' in game.data)



if __name__ == '__main__':
    unittest.main()