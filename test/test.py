import unittest

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        result = "Hello, World!"
        self.assertEqual(result, "Hello, World!")

if __name__ == '__main__':
    unittest.main()