from unittest import TestCase

from wordhunter.core.hunter import Hunter


class TestHunter(TestCase):
    def test_hunter(self):
        matrix = [['a', 'b', 'c', 'd'],
                  ['e', 'f', 'g', 'h'],
                  ['i', 'j', 'k', 'l'],
                  ['m', 'n', 'o', 'p']]

        wordlist = {'ab': None, 'jkl': None,  # Horizontal, left to right
                    'nm': None, 'lkji': None,  # Horizontal, right to left
                    'fjn': None, 'dhl': None,  # Vertical, top to bottom
                    'mie': None, 'okgc': None,  # Vertical, bottom to top
                    'be': None, 'hkn': None,  # Diagonal from left, top to bottom
                    'ifc': None, 'nkh': None,  # Diagonal from left, bottom to top
                    'bgl': None, 'in': None,  # Diagonal from right, top to bottom
                    'ni': None, 'pkfa': None  # Diagonal from right, bottom to top
                    }
        hunter = Hunter(wordlist=wordlist, matrix=matrix)
        result = hunter.run()
        self.assertEquals(len(result), len(wordlist))
        for item in result:
            self.assertIn(item, wordlist)
