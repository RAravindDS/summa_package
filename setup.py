import setuptools

with open('README.md', 'r', encoding='UTF-8') as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "summa_package"
AUTHOR_USER_NAME = "RAravindDS"
SRC_REPO = "summa_package"
AUTHOR_USER_EMAIL = "aravindan22052001@gmail.com"
DESCRIPTION = "summa package documentation"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_USER_EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues", }
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")


)

""" This py file helps to setup the basic configuration like user name, package name, etc. 
    - That's all don't complicate with this."""
