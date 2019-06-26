"""
Load the version into an Python object so other modules
can programmatically have the current version
"""

import pkg_resources

try:
    VERSION = pkg_resources.get_distribution("wordhunter").version
except pkg_resources.DistributionNotFound:
    VERSION = "unknown.unknown"
