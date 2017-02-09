"""Script for generating python project."""
import sys
import os
from command_line_parser.option_parser import CommandLineOptionParser
from command_line_parser.options import FileOption, OutputOption, Option
from src.project_config import ProjectConfiguration
from src.project_generator import ProjectGenerator
from src.metadata import VERSION
from scripts.generate_template import generate_json, generate_yaml


def main():
    """Python project generation main function."""
    file_option = FileOption()
    output_option = OutputOption()
    template_option = Option('-t', '--template', 'template', 'Generates configuration template in either yaml or json.')
    options = [file_option, output_option, template_option]
    usage = "usage: generate-project [-f config_file [-o output_path]] [-t <yaml/json>]"
    cmd_parser = CommandLineOptionParser(options, usage, VERSION)
    cmd_parser.parseArguments(sys.argv)
    if cmd_parser.template or cmd_parser.template == "":
        if cmd_parser.template == "json":
            generate_json()
        else:
            generate_yaml()
    else:
        try:
            conf_path = get_conf_path(cmd_parser)
            root_path = get_root_path(cmd_parser)
            generate_project(conf_path, root_path)
        except Exception as e:
            print("{0}".format(e.args[0]))


def get_conf_path(cmd_parser):
    """Get configuration file path."""
    if not cmd_parser.file:
        raise Exception("Could not find configuration file.")
    return cmd_parser.file


def get_root_path(cmd_parser):
    """Get root path fro project generation."""
    if cmd_parser.output:
        root_path = cmd_parser.output
    else:
        root_path = os.getcwd()
    return root_path


def generate_project(conf_file, root_path):
    """Generates the project stub."""
    config = ProjectConfiguration(conf_file)
    generator = ProjectGenerator(config)
    generator.generate(root_path)


if __name__ == '__main__':
    main()
