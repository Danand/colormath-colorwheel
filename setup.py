import colormath

from setuptools import setup

LONG_DESCRIPTION = open("README.md").read()

CLASSIFIERS = [
    "Development Status :: 2 - Pre-Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Topic :: Artistic Software",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.11",
]

KEYWORDS = "color colorwheel"

setup(
    name="colormath-colorwheel",
    version=colormath.VERSION,
    description="Custom color wheel extension for `colormath`.",
    long_description=LONG_DESCRIPTION,
    author="Andrey Danilov",
    author_email="danand@inbox.ru",
    url="https://github.com/Danand/colormath-colorwheel",
    download_url="http://pypi.python.org/pypi/colormath-colorwheel/",
    packages=["colormath"],
    platforms=["Platform Independent"],
    license="MIT",
    classifiers=CLASSIFIERS,
    keywords=KEYWORDS,
    install_requires=["colormath>=3.0.0"],
)
