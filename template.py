import os
import logging
from pathlib import Path  # this will take care of path

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s]: %(message)s"
)

# getting the project name
while True:
    project_name = input("Enter the project Name: ")
    if project_name != '':
        break

logging.info(f"Creating Project by name: {project_name}")


# creating the list of files
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integeration/__init__.py",
    "init_setup.sh",  # this helps to setup the conda env
    "requirements_dev.txt",   # used for our dev environent like pytest
    "requirements.txt",
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini",  # this helps to test our package in various environments
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(
            f"Creating a directory at: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(
                f"Creating a new file: {filename} at path: {filepath}")

    else:
        logging.info(f"file is already present at: {filepath} ")


""" In Short we are creating all the files for our project setup that is essentially needed for our project, templat.py means pypi package project folder setup process. 
    - Just use this code. Don't get overwhelemed about seeing this code. 
"""
