from unittest import TestCase

from wordhunter.core.hunter import Hunter


class TestHunter(TestCase):
    def test_hunter(self):
        matrix = [['a', 'b', 'c', 'd'],
                  ['e', 'f', 'g', 'h'],
                  ['i', 'j', 'k', 'l'],
                  ['m', 'n', 'o', 'p']]

        wordlist = {'ab', 'jkl',  # Horizontal, left to right
                    'nm', 'lkji',  # Horizontal, right to left
                    'fjn', 'dhl',  # Vertical, top to bottom
                    'mie', 'okgc',  # Vertical, bottom to top
                    'be', 'hkn',  # Diagonal from left, top to bottom
                    'ifc', 'nkh',  # Diagonal from left, bottom to top
                    'bgl', 'in',  # Diagonal from right, top to bottom
                    'ni', 'pkfa'  # Diagonal from right, bottom to top
                    }
        hunter = Hunter(wordlist=wordlist, matrix=matrix)
        result = hunter.run()
        self.assertEquals(len(result), len(wordlist))
        for item in result:
            self.assertIn(item, wordlist)
