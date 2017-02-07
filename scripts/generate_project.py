"""Script for generating python project."""
import sys
import os
from command_line_parser.option_parser import CommandLineOptionParser
from command_line_parser.options import FileOption, OutputOption
from src.project_config import ProjectConfiguration
from src.project_generator import ProjectGenerator

def main():
    """Python project generation main function."""
    file_option = FileOption()
    output_option = OutputOption()
    options = [file_option, output_option]
    cmd_parser = CommandLineOptionParser(options, "", "")
    cmd_parser.parseArguments(sys.argv)
    if not cmd_parser.file:
        print("Could not find configuration file.")
    if cmd_parser.output:
        root_path = cmd_parser.output
    else:
        root_path = os.getcwd()
    config = ProjectConfiguration(cmd_parser.file)
    generator = ProjectGenerator(config)
    generator.generate(root_path)

if __name__ == '__main__':
    main()
