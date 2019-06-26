"""
Command Line Interface entry-point
"""

import argparse

from wordhunter.core.version import VERSION


def main():
    """
    Parses the command line arguments and runs the application
    """
    parser = argparse.ArgumentParser(prog='wordhunter',
                                     description='Word Hunter')
    parser.add_argument('-v', '--version', action='version', version=VERSION)
