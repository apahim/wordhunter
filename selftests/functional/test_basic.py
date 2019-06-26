import re
import subprocess

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
