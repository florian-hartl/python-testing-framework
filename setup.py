from setuptools import setup

with open('README.md', 'r') as f:
  long_description = f.read()

setup(
   name='python-testing-framework',
   version='1.0.0',
   author='Florian Hartl',
   url='https://github.com/florian-hartl/python-testing-framework',
   license='LICENSE',
   description='Workshop for setting up a testing framework in Python',
   long_description=long_description,
   packages=['python_testing_framework'],
)
