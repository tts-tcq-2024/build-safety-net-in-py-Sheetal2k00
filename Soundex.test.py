import unittest
from Soundex import soundex

class TestSoundex(unittest.TestCase):
    
    def test_basic_cases(self):
        self.assertEqual(soundex('Robert'), 'R163')
        self.assertEqual(soundex('Rupert'), 'R163')
        self.assertEqual(soundex('Rubin'), 'R150')
        self.assertEqual(soundex('Ashcraft'), 'A261')

    def test_edge_cases(self):
        self.assertEqual(soundex(''), '0000')
        self.assertEqual(soundex('A'), 'A000')
        self.assertEqual(soundex('B'), 'B000')
        self.assertEqual(soundex('AEIOU'), 'A000')
        self.assertEqual(soundex('H'), 'H000')

    def test_special_cases(self):
        self.assertEqual(soundex('Martha'), 'M630')
        self.assertEqual(soundex('Martin'), 'M635')
        self.assertEqual(soundex('Smith'), 'S530')
        self.assertEqual(soundex('Smythe'), 'S530')

if __name__ == '__main__':
    unittest.main()
