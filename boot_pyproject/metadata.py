NAME = 'boot-pyproject'
VERSION = '0.0.1'
DESCRIPTION = 'Bootstrap python project'
URL = 'https://github.com/mjalas/boot-pyproject'
AUTHOR = 'Mats Jalas'
AUTHOR_EMAIL = 'mats.jalas@gmail.com'
LICENSE = 'GNU GPLv3'
CLASSIFIERS = [
                  'Development Status :: 3 - Alpha',
                  'Intended Audience :: Developers',
                  'Topic :: Software Development :: Libraries',
                  'License :: OSI Approved :: MIT License',
                  'Programming Language :: Python :: 3.5',
              ],
EXCLUDE = [],
SETUP_REQUIRES = ['nose>=1.0', 'coverage>=4.0.3', 'pypandoc>=1.1.3'],
TEST_SUITE = 'nose.collector',
TESTS_REQUIRE = ['nose']