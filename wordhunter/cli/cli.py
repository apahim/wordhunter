"""
Command Line Interface entry-point
"""

import argparse
import logging
import sys

from pathlib import Path

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
    args = parser.parse_args()

    wordlist_dict = dict()
    with open(args.wordlist) as file_obj:
        for line in file_obj:
            wordlist_dict[line.rstrip()] = None
    log.info('Wordlist number of words: %s', len(wordlist_dict))
