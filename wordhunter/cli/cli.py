"""
Command Line Interface entry-point
"""

import argparse
import logging
import sys

from pathlib import Path

from wordhunter.core.matrix import generate
from wordhunter.core.version import VERSION


def _validate_wordlist(value):
    """
    Helper function to validate the wordlist file.
    :param value: the path to the wordlist file
    :return: the pathlib.Path instance of the wordlist file
    """
    wordlist_file = Path(value)
    if not wordlist_file.is_file():
        raise argparse.ArgumentTypeError(f'File {value} not found.')

    return wordlist_file


def main():
    """
    Parses the command line arguments and runs the application
    """
    log = logging.getLogger(__name__)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter(fmt='%(message)s'))
    log.addHandler(handler)
    log.setLevel(logging.INFO)

    parser = argparse.ArgumentParser(prog='wordhunter',
                                     description='Word Hunter')
    parser.add_argument('-v', '--version', action='version', version=VERSION)
    parser.add_argument('-w', '--wordlist', required=True,
                        type=_validate_wordlist,
                        help='The file with the list of '
                             'words to search for matches on.')
    parser.add_argument('-d', '--dimension', default=15,
                        type=int,
                        help='The matrix dimension size. Example: is the'
                             'dimension is 5, the matrix will be 5 x 5 '
                             '(25 items). Defaults to 15.')
    args = parser.parse_args()

    matrix = generate(args.dimension)
    log.info('Matrix %sx%s:', args.dimension, args.dimension)
    for line in matrix:
        log.info('  %s', line)

    wordlist_dict = dict()
    with open(args.wordlist) as file_obj:
        for line in file_obj:
            wordlist_dict[line.rstrip()] = None
    log.info('Wordlist number of words: %s', len(wordlist_dict))
