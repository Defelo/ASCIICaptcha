from setuptools import setup, find_packages
from os import environ

setup(
    name="ASCIICaptcha",
    version="1.0.0",
    url="https://github.com/Defelo/ASCIICaptcha",
    author="Defelo",
    author_email="elodef42@gmail.com",
    description="A Python Library to generate simple ASCII Captchas",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=open("requirements.txt").read().splitlines(),
)
