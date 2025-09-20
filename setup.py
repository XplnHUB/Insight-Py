from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="insight-cli-sarang",
    version="0.2.1",
    description="A Python-based CLI tool that analyzes codebases and generates detailed reports",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ExplainHub/Insight-Py",
    author="Arpit Sarang",
    author_email="arpitsarang2020@gmail.com",
    license="MIT",
    keywords="cli, code-analysis, gemini-api, static-analysis, developer-tools",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Environment :: Console",
    ],
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "google-generativeai",
    ],
    entry_points={
        "console_scripts": [
            "insight-cli=insight.cli:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/ExplainHub/Insight-Py/issues",
        "Source": "https://github.com/ExplainHub/Insight-Py",
    },
)
