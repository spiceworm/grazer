from setuptools import setup, find_packages


with open('README.md') as f:
    _readme = f.read()

with open('LICENSE') as f:
    _license = f.read()

setup(
    name='grazer',
    version='0.1.0',
    description='Asynchronously grab arbitrary HTML elements',
    long_description=_readme,
    author='spiceworm',
    url='https://github.com/spiceworm/grazer',
    license=_license,
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4 >= 4.12.3",
        "PyYAML >= 6.0.1",
        "requests >= 2.31.0",
    ],
)
