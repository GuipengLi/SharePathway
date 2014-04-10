from distutils.core import setup

setup(
    name = 'sharepathway',
    packages = ['sharepathway'], # this must be the same as the name above
    version = '0.1.0',
    description = 'A Python package for KEGG pathway enrichment analysis with multiple gene lists',
    author = 'Guipeng Li',
    author_email = 'guipenglee@gmail.com',
    url = 'https://github.com/GuipengLi/sharepathway',   # use the URL to the github repo
    download_url = 'https://github.com/GuipengLi/sharepathway/tarball/0.1.0', # I'll explain this in a second
    keywords = ['detection', 'pathway', 'enrichment', 'share', 'multiple gene lists'], # arbitrary keywords
    classifiers = [],
    long_description=open('README.md').read(),
    install_requires=["numpy >= 1.6.0", "scipy >= 0.12.0"],
)