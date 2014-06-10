from distutils.core import setup

setup(
    name = 'sharepathway',
    packages = ['sharepathway'], # this must be the same as the name above
    version = '0.2.1',
    description = 'A Python package for KEGG pathway enrichment analysis with multiple gene lists',
    author = 'Guipeng Li',
    author_email = 'guipenglee@gmail.com',
    url = 'https://github.com/GuipengLi/sharepathway',   # use the URL to the github repo
    keywords = ['detection', 'pathway', 'enrichment', 'share', 'multiple gene lists'], # arbitrary keywords
    classifiers = [],
    long_description=open('README.md').read(),
    install_requires=["numpy >= 1.6.0", "scipy >= 0.12.0"],
)
