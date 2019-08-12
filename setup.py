from setuptools import setup, find_packages
from os.path import join, dirname
from shutil import rmtree

NAME = 'project_name'
VERSION = __import__('project_name').__version__
AUTHOR = 'author_name'
AUTHOR_EMAIL = 'author_email'
URL = 'https://project_url.com'
KEYWORDS = [
    'here', 'must', 'be', 'some', 'key',
    'words', 'for', 'your', 'project',
]


def description():
    """Add long description from README.md file."""
    return open(join(dirname(__file__), 'README.md')).read()


def remove_eggs():
    """Remove eggs files after packaging."""
    return rmtree(NAME + '.egg-info')


setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    description='Few words about your project',
    long_description=description(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[],  # Requires for project
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=KEYWORDS,
)

remove_eggs()
