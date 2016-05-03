from boot_pyproject.create_setup_file import SetupTemplateBuilder


def main():
    with open("config_project.yaml", "w") as f:
        content = SetupTemplateBuilder.build_yaml()
        f.write(content)


if __name__ == '__main__':
    main()
