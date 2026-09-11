"""Assemble public/main and preview/dev without publishing repository files."""
from pathlib import Path
import shutil
import sys


def copy_site(source, target, development=False):
    target.mkdir(parents=True, exist_ok=True)
    html = (source / 'index.html').read_text()
    if development:
        html = html.replace('<head>', '<head>\n<meta name="robots" content="noindex, nofollow">', 1)
    (target / 'index.html').write_text(html)
    shutil.copytree(source / 'assets', target / 'assets', dirs_exist_ok=True)


def build(public, development, output):
    copy_site(public, output)
    copy_site(development, output / 'dev', development=True)
    (output / '.nojekyll').touch()
    if (public / 'CNAME').exists():
        shutil.copy2(public / 'CNAME', output / 'CNAME')


if __name__ == '__main__':
    build(*(Path(arg) for arg in sys.argv[1:]))
