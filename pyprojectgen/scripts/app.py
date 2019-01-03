#!/bin/env python
import click

from pyprojectgen.generator.project import ProjectGenerator
from pyprojectgen.project_config import ProjectConfiguration
from pyprojectgen.template_builder import TemplateBuilder


@click.group()
def cli():
    pass


@cli.command()
@click.argument('project_configuration')
@click.argument('output_destination')
def generate(project_configuration: str, output_destination: str):
    """Generates the project stub."""
    if project_configuration.endswith('.yaml') or project_configuration.endswith('.yml'):
        config = ProjectConfiguration(project_configuration)
        generator = ProjectGenerator(config)
        generator.generate(output_destination)
    elif project_configuration.endswith('.json'):
        click.echo("JSON format not yet supported! Coming soon!")
    else:
        click.echo('File format not supported! Only Yaml or JSON formats are supported.')


@cli.group()
def template():
    pass


def generate_json():
    """Generates template in json."""
    with open("config_project.json", "w") as stream:
        content = TemplateBuilder.build_json()
        stream.write(content)


def generate_yaml():
    """Generates template in yaml."""
    with open("config_project.yml", "w") as stream:
        content = TemplateBuilder.build_yaml()
        stream.write(content)


# TODO: Uncomment when JSON format is fully supported
#@template.command()
#@click.option('--output', default=None, help='Name of output file')
#def json(output):
#    if not output:
#        output = "config_project.json"
#    with open(output, 'w') as dest:
#        content = TemplateBuilder.build_json()
#        dest.write(content)


@template.command()
@click.option('--output', default=None, help='Name of output file')
def yaml(output):
    if not output:
        output = "config_project.yml"
    with open(output, 'w') as dest:
        content = TemplateBuilder.build_json()
        dest.write(content)
