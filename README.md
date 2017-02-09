# Python project generator
[![Build Status](https://travis-ci.org/mjalas/pyprojectgen.svg?branch=master)](https://travis-ci.org/mjalas/pyprojectgen)

Generate base file structure for python project required for creating a python package.

## Installation

Python 3.5+ is currently required for installing de tool.
There are currently two different ways of installing the application.

Through pip:
```
pip install pyprojectgen
```

Manually:
```
git clone https://github.com/mjalas/pyprojectgen.git
cd pyprojectgen
python setup.py install
```

The application is installed under the name 'generate-project'

## Usage

The tool has two main feature:
- generate project configuration template file
- generate project structure based on a configuration file

### Generate configuration template

To generate the configuration template run the following command:
```
generate-project -t yaml
```
This generates a config_project.yml file. Then fill in the project metadata in the template file,
so it can be used to generate the project structure.

### Generate project structure

The simplest way to generate the project structure is to run the following command:
```
generate-project -f <config_file_path>
```
This will generate the project stub into the current folder.
To specify a different location to generate the project stub, run the following command:
```
generate-project -f <config_file_path> -o <output_path>
```
