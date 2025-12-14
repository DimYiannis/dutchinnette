from setuptools import setup, find_packages

setup(
    name="dutchinnette",
    version="0.1.0",
    author="Codam Community",
    description="Automated testing tool for Codam's Python curriculum",
    packages=find_packages(),
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "codam=dutchinnette.codam:main",
            "dutchinnette=dutchinnette.codam:main",
        ],
    },
    # ... more metadata
)