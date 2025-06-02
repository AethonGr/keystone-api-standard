from setuptools import find_packages, setup

# Read the content of the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read the content of the requirements file
with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

# Setup configuration
setup(
    name="keystone-api-standard",
    version="0.1.0",
    author="AETHON Engineering",
    author_email="info@aethon.gr",
    description="A robust and modular framework designed to standardize logistics operations APIs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AethonGr/keystone-api-standard",
    packages=find_packages(include=["api", "api.*"]),
    package_data={
        "api.endpoints": ["*.yaml"],
    },
    install_requires=requirements,
    license="GPL-3.0-only",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: System :: Networking",
    ],
    python_requires=">=3.10",
)
