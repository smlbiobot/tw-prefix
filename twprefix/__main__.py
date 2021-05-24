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
        '-f',
        '--file',
        help='File to process',
        default=None,
    )
    ap.add_argument(
        '-s',
        '--string',
        help="Process a string",
        default=None
    )
    ap.add_argument(
        '-p',
        '--prefix',
        help="Prefix for the classes",
        default='tw-'
    )
    ap.add_argument(
        '-c',
        '--classnames',
        help="Convert class names directly",
        default=None,
        nargs='*'
    )
    # TODO: add option to output rendered template to file
    ap.add_argument(
        '-o',
        '--out',
        default=None,
        help='Output file'
    )

    args = ap.parse_args()

    filepath = None
    if args.file:
        filepath = os.path.abspath(args.file)

    text = None
    if args.string:
        text = args.string

    process(
        filepath=filepath,
        text=text,
        prefix=args.prefix,
        class_names=args.classnames,
    )


if __name__ == '__main__':
    main()
