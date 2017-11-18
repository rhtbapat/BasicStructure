from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='MyLibrary',
    version='0.0.1',
    description='Sample Package to Demonstrate Structure for Python Code',
    long_description=readme,
    author='Rohit Bapat',
    author_email='rhtbapat@gmail.com',
    url='https://github.com/rhtbapat/BasicStructure',
    license=license,
    packages=find_packages()
)