from string import Template

import easyargs
import markdown
from slugify import slugify
from markdown.extensions.toc import TocExtension
from mdx_gfm import GithubFlavoredMarkdownExtension

with open('template/base.html', 'r') as fd:
    TEMPLATE = fd.read()


@easyargs
def main(version, git_version, commit):
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

    # Version build
    if git_version != version:
        # It's not a tag
        version = '{}-{}'.format(version, commit)

    with open('docs/index.html', 'w') as fd:
        template = Template(TEMPLATE)
        html = template.substitute({
            'body': body,
            'version': version,
        })
        fd.write(html)
    print('File written: {} bytes'.format(len(html)))

if __name__ == '__main__':
    main()
