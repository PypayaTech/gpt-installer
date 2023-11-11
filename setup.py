from setuptools import setup, find_packages


with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="gpt-installer",
    version="0.1",
    url="https://github.com/PypayaTech/gpt-installer",
    author="PypayaTech",
    readme="README.md",
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "gpt-installer = gpt_installer.main:main"
        ]
    },
)
