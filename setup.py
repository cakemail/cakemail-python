import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

requirements = [
    'six',
    'urllib3',
    'certifi',
    'python-dateutil',
    'inflection'
]

setup(
    name='cakemail',
    version='1.0',
    description='Cakemail Next-gen API client',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/cakemail/pycakemail',
    license='MIT',
    packages=['cakemail'],
    install_requires=requirements,
    zip_safe=False
)
