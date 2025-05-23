from setuptools import setup, find_packages

setup(
    name="infiltr8",
    version="1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests",
        "rich"
    ],
    entry_points={
        "console_scripts": [
            "infiltr8 = infiltr8.main:main"
        ]
    },
    author="HmadSec",
    description="A Python CLI toolkit for basic web app pentesting tasks",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)