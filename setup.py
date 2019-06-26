from setuptools import setup, find_packages


setup(name='wordhunter',
      packages=find_packages(exclude=('selftests*',)),
      version=open("VERSION", "r").read().strip(),
      author='Amador Pahim',
      author_email='amador@pahim.org',
      python_requires='>=3.6',
      install_requires=[''],
      entry_points={
            'console_scripts': ['wordhunter = wordhunter.cli.cli:main']}
      )
