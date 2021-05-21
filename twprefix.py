"""
Process a Vue component and add prefix to all classes

This is mostly intended to automatically
add a prefix e.g. `tw-` to example components
on the web that does not have a prefix
- e.g. the TailwindUI library
"""
import argparse
import os

def process(filepath):
    pass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('file', help='File to process')
    ap.add_argument('-o', '--out', default=None, help='Output file')

    args = ap.parse_args()

    process(
        filepath=os.path.abspath(args.file)
    )


if __name__ == '__main__':
    main()
