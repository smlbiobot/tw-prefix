from setuptools import find_packages, setup

import os
import re
import codecs


def open_local(paths, mode="r", encoding="utf8"):
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), *paths)

    return codecs.open(path, mode, encoding)

with open_local(["twprefix", "__version__.py"], encoding="latin1") as fp:
    try:
        version = re.findall(
            r"^__version__ = \"([^']+)\"\r?$", fp.read(), re.M
        )[0]
    except IndexError:
        raise RuntimeError("Unable to determine version.")

setup_kwargs = {
    "name": "twprefix",
    "version": version,
    "url": "https://github.com/smlbiobot/tw-prefix/",
    "license": "MIT",
    "author": "See-ming Lee (SML)",
    "author_email": "seeminglee@gmail.com",
    "description": (
        "Process a Vue component with Tailwind CSS classes and add prefixes to all classes."
    ),
    "packages": find_packages(),
    "platforms": "any",
    "python_requires": ">=3.7",
    "classifiers": [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    "entry_points": {"console_scripts": ["twprefix = twprefix.__main__:main"]},
}


setup(**setup_kwargs)