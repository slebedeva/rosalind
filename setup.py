from setuptools import setup, find_packages

setup(
    name="rosalind",
    version="1.0.0",
    author="Svetlana Lebedeva",
    description="Basic functions to work with biological sequences.",
    long_description=open("README.rst").read(),
    url="https://github.com/slebedeva/rosalind",
    license="MIT",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "rosalind = mypackage.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
