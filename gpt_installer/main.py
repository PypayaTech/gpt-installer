import argparse
from gpt_installer.installer import Installer


def main():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest="command")

    parser_extract = subparsers.add_parser("extract")
    parser_extract.add_argument("readme", help="The README file path")

    parser_generate = subparsers.add_parser("generate")
    parser_generate.add_argument("input", help="The README file path or instructions")

    parser_run = subparsers.add_parser("run")
    parser_run.add_argument("script", help="The installation script")

    parser_install = subparsers.add_parser("install")
    parser_install.add_argument("readme", help="The README file path")

    args = parser.parse_args()

    installer = Installer()

    if args.command == "extract":
        print(installer.extract_installation_instructions(args.readme))
    elif args.command == "generate":
        print(installer.generate_installation_script(args.input))
    elif args.command == "run":
        installer.run_installation_script(args.script)
    elif args.command == "install":
        instructions = installer.extract_installation_instructions(args.readme)
        script = installer.generate_installation_script(instructions)
        installer.run_installation_script(script)


if __name__ == "__main__":
    main()
