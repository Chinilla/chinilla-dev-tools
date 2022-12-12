#!/usr/bin/env python

from setuptools import find_packages, setup

with open("README.md", "rt") as fh:
    long_description = fh.read()

dependencies = [
    "chinilla-blockchain==1.3.0",
    "packaging",
    "pytest",
    "pytest-asyncio",
    "pytimeparse",
]

dev_dependencies = [
    "flake8",
    "mypy",
    "types-aiofiles",
    "types-click",
    "types-cryptography",
    "types-pkg_resources",
    "types-pyyaml",
    "types-setuptools",
    "black==21.12b0",
    "isort",
    "pre-commit",
    "pylint",
]

setup(
    name="chinilla_dev_tools",
    version="1.2",
    packages=find_packages(exclude=("tests",)),
    author="Edward Teach",
    entry_points={
        "console_scripts": ["chdv = chdv.cmds.cli:main"],
    },
    package_data={
        "": ["*.clvm", "*.clvm.hex", "*.clib", "*.clsp", "*.clsp.hex"],
    },
    author_email="edward@chinilla.com",
    setup_requires=["setuptools_scm"],
    install_requires=dependencies,
    url="https://github.com/Chinilla",
    license="https://opensource.org/licenses/Apache-2.0",
    description="Chinilla development commands",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Security :: Cryptography",
    ],
    extras_require=dict(
        dev=dev_dependencies,
    ),
    project_urls={
        "Bug Reports": "https://github.com/Chinilla/chinilla-dev-tools",
        "Source": "https://github.com/Chinilla/chinilla-dev-tools",
    },
)
