"""
Process a Vue component and add prefix to all classes

This is mostly intended to automatically
add a prefix e.g. `tw-` to example components
on the web that does not have a prefix
- e.g. the TailwindUI library
"""
import argparse
import os

from twprefix.twprefix import process


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        'file',
        help='File to process',
        default='./tests/PageHeadings.vue',
    )
    # TODO: add option to output rendered template to file
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
