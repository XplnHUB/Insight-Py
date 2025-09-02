from setuptools import setup, find_packages

setup(
    name="insight",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "argparse",
        "google-generativeai",
    ],
    entry_points={
        "console_scripts": [
            "insight=insight.cli:main",
        ],
    },
)
