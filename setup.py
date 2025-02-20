"""Setup script to install the package."""

from setuptools import find_packages
from setuptools import setup


setup(
    name='receipt_processor',
    version='1.0.0',
    description='Challenge submission to process receipts',
    author='Zoe Krueger',
    author_email='zofetch@zkrueger.com',
    packages=find_packages(),
    package_data={'receipt_processor': ['**/*.json']},
    include_package_data=True,
    install_requires=[
        'click==8.1.7',
        'flask-restx==1.3.0',
        'wheel==0.45.1',
    ]
)
