from setuptools import setup, find_packages


with open("readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="mousesens",
    version="0.2",
    description="Change the mouse sensitivity",
    author="Juan Molina Riddell",
    author_email="jmriddell@protonmail.ch",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jmriddell/mousesens",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: English",
        "Topic :: Desktop Environment",
        "Topic :: Utilities",
    ],
    packages=find_packages(),
    intall_requires=["Click"],
    entry_points=dict(console_scripts=["mousesens=mousesens.cli:cli"]),
)
