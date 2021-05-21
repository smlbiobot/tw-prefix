"""
Process a Vue component and add prefix to all classes

This is mostly intended to automatically
add a prefix e.g. `tw-` to example components
on the web that does not have a prefix
- e.g. the TailwindUI library
"""
import argparse
import os
from bs4 import BeautifulSoup

def process(filepath=None):
    """
    Process the filepath
    :param filepath: source file. Use file from tests if None
    :return:
    """
    with open(filepath) as fp:
        soup = BeautifulSoup(fp, 'lxml-xml')

    print(soup)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        'file',
        help='File to process',
        default='./tests/PageHeadings.vue',
    )
    ap.add_argument(
        '-o',
        '--out',
        default=None,
        help='Output file'
    )

    args = ap.parse_args()

    process(
        filepath=os.path.abspath(args.file)
    )


if __name__ == '__main__':
    main()
