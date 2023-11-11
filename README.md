# GPT Installer

A tool that uses GPT to generate installation scripts and set up projects based on READMEs or other documentation, making it easier for developers to get started with new projects.

<p align="center">
  <img src="gpt_installer.png" alt="GPT Installer">
</p>

## Features

- Extract key information from README files or any other similar documentation.
- Generate concise installation scripts for the projects.
- Set up the necessary dependencies, environment variables, and other configuration options.
- Ensure consistent and thorough setup process.
- Save time and effort, especially useful with large projects or scattered documentation.

## Installation

1. Ensure that Python and Git are installed on your local machine.
2. Run the following command in your command line to install this package via pip directly from the Git repository:

`pip install git+https://github.com/PypayaTech/gpt-installer.git`

## Examples of usage

### Console:
After installing, run `gpt-installer` in your command line. Here is an example:

```
gpt-installer extract README.md
gpt-installer generate "Install Python and pip. Run pip install -r requirements.txt"
gpt-installer run install.sh
gpt-installer install README.md
```

### Python:
You can use `gpt-installer` in your Python scripts as follows:

```python
from gpt_installer.installer import Installer

installer = Installer()
instructions = installer.extract_installation_instructions("README.md")
script = installer.generate_installation_script(instructions)
installer.run_installation_script(script)
```

## Contributing

Please, feel free to contribute to this project. If you spot any issues or have feature requests, file an issue in the issue tracker. Pull requests are also welcome.

Whether you're a seasoned developer or a beginner, `gpt-installer` can help you get started quickly and easily. It's perfect for open source projects, where documentation can often be scattered and difficult to follow. With `gpt-installer`, you can ensure that your project's setup process is consistent, reproducible, and easy to understand.

Get started with `gpt-installer` today and take the pain out of setting up your projects!
