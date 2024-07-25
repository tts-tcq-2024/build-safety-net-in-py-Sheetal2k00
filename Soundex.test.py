import unittest
from Soundex import soundex

class TestSoundex(unittest.TestCase):
    def test_soundex(self):
        self.assertEqual(soundex("User"), "U260")
        self.assertEqual(soundex("Calm"), "C450")
        self.assertEqual(soundex("India"), "I530")
        self.assertEqual(soundex("Kumta"), "K530")
        
if __name__ == "__main__":
    unittest.main()
