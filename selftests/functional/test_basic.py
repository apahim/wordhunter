import re
import subprocess

from pathlib import Path
from unittest import TestCase


class TestBasic(TestCase):

    @staticmethod
    def run_command(args):
        cmd = ['wordhunter', *args]
        return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    def test_version(self):
        args = ['-v']
        output = self.run_command(args).stdout.decode().rstrip()
        pattern = r'^\d+.\d+.\d+$'
        self.assertTrue(re.match(pattern, output))

    def test_wordlist_valid(self):
        data = str(Path(__file__).parent.parent / 'data' / 'words.txt')
        args = ['--wordlist', data]
        result = self.run_command(args)
        self.assertEquals(result.returncode, 0)
        self.assertIn('Wordlist number of words: 62799', result.stdout.decode())

    def test_wordlist_invalid(self):
        args = ['--wordlist', 'invalid_path/words.txt']
        result = self.run_command(args)
        self.assertNotEquals(result.returncode, 0)
