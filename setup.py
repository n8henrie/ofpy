import os

long_description = 'Add tasks to OmniFocus from the command line.'

# Markdown to RST documentation https://coderwall.com/p/qawuyq
try:
    import pypandoc
except (IOError, ImportError):
    long_description = open('README.md').read()
else:
    long_description = pypandoc.convert('README.md', 'rst')


from distutils.core import setup
setup(
    name='ofpy',
    packages=['ofpy'],
    version='0.12',
    description='Add tasks to OmniFocus from Linux',
    long_description=long_description,
    author='Nathan Henrie',
    author_email='nate@n8henrie.com',
    url='http://n8henrie.com/2014/09/ofpy',
    download_url='https://github.com/n8henrie/ofpy/tarball/0.12',
    keywords=['omnifocus', 'productivity', 'tasklist'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 3.4'
        ],
)
