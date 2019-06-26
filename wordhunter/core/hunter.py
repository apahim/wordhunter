"""
Main Word Hunter module. This is where the magic happens.
"""

import logging


class Hunter:
    """
    Hunter class to aggregate all the hunting mechanisms.

    :param wordlist: The HashTable containing all the valid words
    :param matrix: The 2D array to find the words on
    :type wordlist: dict
    :type matrix: list[list]
    """

    def __init__(self, wordlist, matrix):
        self.log = logging.getLogger('wordhunter')

        self.wordlist = wordlist
        self.matrix = matrix

        self.dimension = len(matrix)
        self.total_items = self.dimension ** 2

    def run(self):
        """
        Calls all the hunting helpers.

        :return: matched unique words
        :rtype: set
        """
        matches = []
        matches.extend(self._hunt_horizontal())
        matches.extend(self._hunt_vertical())
        matches.extend(self._hunt_diagonal_from_right())
        matches.extend(self._hunt_diagonal_from_left())
        return set(matches)

    def _hunt_horizontal(self):
        """
        Searches for words horizontally, both
        from left to right and from right to left
        """
        self.log.debug('Horizontal search')

        matches = []
        rows = []

        for a in range(self.dimension):
            rows.append([(a, b) for b in range(self.dimension)])

        self.log.debug('  Rows:')
        for row in rows:
            self.log.debug('  --> %s', row)
            word = ''
            for coord in row:
                word += self.matrix[coord[0]][coord[1]]
                for x in range(len(word)):
                    temp_word = word[x:]
                    try:
                        self.wordlist[temp_word]
                        matches.append(temp_word)
                    except KeyError:
                        pass
                    try:
                        self.wordlist[temp_word[::-1]]
                        matches.append(temp_word[::-1])
                    except KeyError:
                        pass

        self.log.debug('  Matches:')
        self.log.debug('  --> %s', matches)
        return matches

    def _hunt_vertical(self):
        """
        Searches for words vertically, both
        from top to bottom and from bottom to top
        """
        self.log.debug('Vertical search')

        matches = []
        columns = []

        for a in range(self.dimension):
            columns.append([(b, a) for b in range(self.dimension)])

        self.log.debug('  Columns:')
        for column in columns:
            self.log.debug('  --> %s', column)
            word = ''
            for coord in column:
                word += self.matrix[coord[0]][coord[1]]
                for x in range(len(word)):
                    temp_word = word[x:]
                    try:
                        self.wordlist[temp_word]
                        matches.append(temp_word)
                    except KeyError:
                        pass
                    try:
                        self.wordlist[temp_word[::-1]]
                        matches.append(temp_word[::-1])
                    except KeyError:
                        pass

        self.log.debug('  Matches:')
        self.log.debug('  --> %s', matches)
        return matches

    def _hunt_diagonal_from_right(self):
        """
        Searches for words in the diagonals from the top right to the
        bottom left
        """
        self.log.debug('Diagonal search, from top right to bottom left')

        matches = []

        a_start = 0
        a_end = 0
        b_start = self.dimension
        b_end = self.dimension
        diagonals = []
        count = 0

        while count < self.total_items:
            if a_end < self.dimension:
                a_end += 1
            elif a_start < self.dimension:
                a_start += 1

            if b_start > 0:
                b_start -= 1
            elif b_end > 0:
                b_end -= 1

            a_range = range(a_start, a_end)
            b_range = range(b_start, b_end)
            assert len(a_range) == len(b_range)
            diagonal_len = len(a_range)
            count += diagonal_len

            a_iter = iter(a_range)
            b_iter = iter(b_range)

            diagonals.append([(next(a_iter), next(b_iter))
                              for _ in range(diagonal_len)])

        self.log.debug('  Diagonals:')
        for diagonal in diagonals:
            self.log.debug('  --> %s', diagonal)
            word = ''
            for coord in diagonal:
                word += self.matrix[coord[0]][coord[1]]
                for x in range(len(word)):
                    temp_word = word[x:]
                    try:
                        self.wordlist[temp_word]
                        matches.append(temp_word)
                    except KeyError:
                        pass
                    try:
                        self.wordlist[temp_word[::-1]]
                        matches.append(temp_word[::-1])
                    except KeyError:
                        pass
        self.log.debug('  Matches:')
        self.log.debug('  --> %s', matches)
        return matches

    def _hunt_diagonal_from_left(self):
        """
        Searches for words in the diagonals from the top left to the
        bottom right
        """
        self.log.debug('Diagonal search, from top left to bottom right')

        matches = []

        start = 0
        end = 0
        diagonals = []
        count = 0

        while count < self.total_items:
            if end < self.dimension:
                end += 1
            elif start < self.dimension:
                start += 1

            a_range = range(start, end)
            b_range = range(end-1, start-1, -1)
            assert len(a_range) == len(b_range)
            diagonal_len = len(a_range)
            count += diagonal_len

            a_iter = iter(a_range)
            b_iter = iter(b_range)

            diagonals.append([(next(a_iter), next(b_iter))
                              for _ in range(diagonal_len)])

        self.log.debug('  Diagonals:')
        for diagonal in diagonals:
            self.log.debug('  --> %s', diagonal)
            word = ''
            for coord in diagonal:
                word += self.matrix[coord[0]][coord[1]]
                for x in range(len(word)):
                    temp_word = word[x:]
                    try:
                        self.wordlist[temp_word]
                        matches.append(temp_word)
                    except KeyError:
                        pass
                    try:
                        self.wordlist[temp_word[::-1]]
                        matches.append(temp_word[::-1])
                    except KeyError:
                        pass
        self.log.debug('  Matches:')
        self.log.debug('  --> %s', matches)
        return matches
