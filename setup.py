from setuptools import setup, find_packages
import os
from os import path

# Get the long description from the README file
long_description = ""
if 'TRAVIS' in os.environ:
    try:
        here = path.abspath(path.dirname(__file__))
        from pypandoc import convert

        if path.exists(path.join(here, 'README.md')):
            long_description = convert('README.md', 'rst')
    except ImportError:
        print("warning: pypandoc module not found, could not convert Markdown to RST")


VERSION = '0.0.4'

setup(
    name='pyprojectgen',
    version=VERSION,
    description='Generates python project structure.',
    # long_description=long_description,
    url='https://github.com/mjalas/pyprojectgen',
    author='Mats Jalas',
    author_email='mats.jalas@gmail.com',
    license='GNU GPLv3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(exclude=[]),
    install_requires=[
        'PyYAML>=3.11',
        'Click==7.0'
    ],
    setup_requires=[
        'nose>=1.0',
        'coverage>=4.0.3',
        'PyYAML>=3.11',
        'Click==7.0'
    ],
    test_suite='nose.collector',
    tests_require=[
        'nose',
        'coverage>=4.0.3',
        'PyYAML'
    ],
    entry_points={
        'console_scripts': [
            'generate-project=scripts.generate_project:main'
        ],
    },
)
