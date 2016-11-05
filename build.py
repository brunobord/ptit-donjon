from string import Template

import easyargs
import markdown
from slugify import slugify
from markdown.extensions.toc import TocExtension
from mdx_gfm import GithubFlavoredMarkdownExtension

with open('template/base.html', 'r') as fd:
    TEMPLATE = fd.read()


@easyargs
def main(git_version, version):
    """
    Build the HTML content
    """
    with open('content/ptit-donjon.md') as fd:
        source = fd.read()
    body = markdown.markdown(
        source,
        extensions=[
            GithubFlavoredMarkdownExtension(),
            TocExtension(
                permalink=True,
                slugify=slugify
            )
        ]
    )
    with open('build/index.html', 'w') as fd:
        template = Template(TEMPLATE)
        html = template.substitute({
            'body': body,
            'git_version': git_version,
            'version': version,
        })
        fd.write(html)
    print('File written: {} bytes'.format(len(html)))

if __name__ == '__main__':
    main()
