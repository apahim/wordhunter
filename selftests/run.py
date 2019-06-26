import sys
import unittest

from pathlib import Path


suite = unittest.TestSuite()
loader = unittest.TestLoader()
tests_dir = Path(__file__).resolve().parent
for test_folder in ['unit', 'functional']:
    suite.addTests(loader.discover(start_dir=tests_dir / test_folder,
                                   top_level_dir=tests_dir))
runner = unittest.TextTestRunner(failfast=False, verbosity=2)
result = runner.run(suite)
if result.failures or result.errors:
    sys.exit(1)
