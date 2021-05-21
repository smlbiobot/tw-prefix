"""
Process a Vue component and add prefix to all classes

This is mostly intended to automatically
add a prefix e.g. `tw-` to example components
on the web that does not have a prefix
- e.g. the TailwindUI library
"""
import argparse
import os
import re

from bs4 import BeautifulSoup


def prettify_with_space(
        s: BeautifulSoup,
        encoding=None,
        formatter="minimal",
        indent: int = 2
):
    """
    Re-indent the BS4 output
    https://stackoverflow.com/questions/15509397/custom-indent-width-for-beautifulsoup-prettify
    """
    r = re.compile(r'^(\s*)', re.MULTILINE)
    return r.sub(r'\1' * indent, s.prettify(encoding, formatter))


def process(filepath=None, prefix='tw-', indent=2):
    """
    Process the filepath
    :param filepath: source file. Use file from tests if None
    :return:
    """
    with open(filepath) as fp:
        soup = BeautifulSoup(fp, 'lxml-xml')

    tags_with_class = soup.find_all(attrs={'class': True})

    for tag in tags_with_class:
        class_names = tag['class'].split(' ')
        tag['class'] = ' '.join([f"{prefix}{c}" for c in class_names])

    tags_with__class = soup.find_all(attrs={':class': True})
    for tag in tags_with__class:
        value = tag[':class']
        replacements = []
        matches = re.findall(r'\'(.+?)\'', value)
        for m in matches:
            src = m
            if ' ' in m:
                class_names = m.split(' ')
                dst = ' '.join([f"{prefix}{c}" for c in class_names])
            else:
                dst = f"{prefix}{src}"
            replacements.append(
                dict(src=src, dst=dst)
            )

        if replacements:
            for r in replacements:
                value = value.replace(r['src'], r['dst'])

        tag[':class'] = value

    print(prettify_with_space(soup, indent=indent))


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
