import unittest
# from unittest.mock import patch
from task import AI



class TestAI(unittest.TestCase):
        
        def setUp(self):
            print('setUp')
            self.ai = AI('Josh', 'Chelsea')

        def tearDown(self):
            print('tearDown\n')

        def test_know_user(self):
            # print('test_email')
            self.assertEqual (self.ai.know_user, 'Nice to meet you Josh. You support a great club in Chelsea')

            self.ai.username = 'John'
            self.ai.club = 'arsenal'

            self.assertEqual(self.ai.know_user, 'Nice to meet you John. You support a great club in arsenal')



if __name__ == '__main__':
    unittest.main()
