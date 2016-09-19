try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
      name='CSVrope',
      version='0.1',
	  license='Creative Commons Attribution 4.0 International license',
      author='thumbo',
      install_requires=['nose'],
      packages=['csvrope'],
      description='A set of row-operations for CSV files.',
      long_description=open('README.rst').read(),
      )