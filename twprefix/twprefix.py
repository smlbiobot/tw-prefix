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


def prefix_name(name: str, prefix: str) -> str:
    """
    Convert class name with prefix.
    Handle special case where prefix needs to be after variant
    e.g. md:text-xl -> md:tw-text-xl
    :param name: Name of the class
    :param prefix: Prefix, e.g. tw-
    :return:
    """
    if ':' in name:
        variant, c_name = name.split(':')
        s = f"{variant}:{prefix}{c_name}"
    else:
        s = f"{prefix}{name}"
    return s


def convert(src: str, prefix='tw-', indent=2) -> str:
    """
    Convert the source string to processed string
    :param src:
    :param prefix:
    :param indent:
    :return:
    """
    soup = BeautifulSoup(src, 'lxml-xml')
    tags_with_class = soup.find_all(attrs={'class': True})

    for tag in tags_with_class:
        class_names = tag['class'].split(' ')
        tag['class'] = ' '.join([prefix_name(c, prefix) for c in class_names])

    tags_with__class = soup.find_all(attrs={':class': True})
    for tag in tags_with__class:
        value = tag[':class']
        replacements = []
        matches = re.findall(r'\'(.+?)\'', value)
        for m in matches:
            src = m
            if ' ' in m:
                class_names = m.split(' ')
                dst = ' '.join([prefix_name(c, prefix) for c in class_names])
            else:
                dst = prefix_name(src, prefix)
            replacements.append(
                dict(src=src, dst=dst)
            )

        if replacements:
            for r in replacements:
                value = value.replace(r['src'], r['dst'])

        tag[':class'] = value

    return prettify_with_space(soup, indent=indent)


def process(filepath=None, prefix='tw-', indent=2):
    """
    Process the filepath
    :param filepath: source file. Use file from tests if None
    :return:
    """

    with open(filepath) as fp:
        src = fp.read()

    dst = convert(
        src,
        prefix=prefix,
        indent=indent,
    )

    print(dst)
