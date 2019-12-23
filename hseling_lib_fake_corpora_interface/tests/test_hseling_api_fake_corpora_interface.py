import unittest

import hseling_api_fake_corpora_interface


class HSELing_API_Fake_corpora_interfaceTestCase(unittest.TestCase):

    def setUp(self):
        self.app = hseling_api_fake_corpora_interface.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to hseling_api_Fake Corpora Interface', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
