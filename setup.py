from setuptools import setup, find_packages

setup(
    name="dutchinnette",
    version="0.1",
    packages=find_packages(),  # will find the inner dutchinnette package
    entry_points={
        "console_scripts": [
            "codam=dutchinnette.codam:main",
        ],
    },
    python_requires=">=3.10",
)
