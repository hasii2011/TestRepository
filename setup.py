import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()
LICENSE = (HERE / 'LICENSE').read_text()

setup(
    name="testrepository",
    version="1.0.0",
    author_email='Humberto.A.Sanchez.II@gmail.com',
    maintainer='Humberto A. Sanchez II',
    maintainer_email='humberto.a.sanchez.ii@gmail.com',
    description='For use by versionoverloard',
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/hasii2011/TestRepository.git",
    packages=[
        'testrepo',
    ],
    package_data={
        'testrepo':          ['py.typed'],
        'oglio.toXmlV10': ['py.typed']
    },
    install_requires=[
        'wxPython==4.2.0',
        'hasiicommon~=0.0.7',
        'pyutmodel~=1.3.4',
        'ogl~=0.70.0',
        'untanglepyut~=0.6.30',
    ],
)
