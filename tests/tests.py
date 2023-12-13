import unittest
from io import StringIO
from unittest.mock import patch
from src.ans import age_verifier

class TestAgeVerifier(unittest.TestCase):

    @patch('builtins.input', side_effect=['abc', '-1', '130', '25'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_valid_age(self, stdout_mock, input_mock):
        age_verifier()
        output = stdout_mock.getvalue()
        self.assertIn('Invalid age. Please try again.', output)
        self.assertIn('Your age is 25', output)


if __name__ == '__main__':
    unittest.main()
