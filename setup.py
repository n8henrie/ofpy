"""setup.py
Setup file for ofpy.
https://github.com/n8henrie/ofpy
"""

# Markdown to RST documentation https://coderwall.com/p/qawuyq
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError, RuntimeError) as e:
    try:
        with open('README.md') as r:
            long_description = r.read()
    except (OSError, IOError) as e:
        long_description = 'Add tasks to OmniFocus from Linux'

VERSION = '0.25'

from distutils.core import setup
setup(
    name='ofpy',
    packages=['ofpy'],
    version=VERSION,
    description='Add tasks to OmniFocus from Linux',
    long_description=long_description,
    author='Nathan Henrie',
    author_email='nate@n8henrie.com',
    url='http://n8henrie.com/2014/09/ofpy',
    download_url='https://github.com/n8henrie/ofpy/tarball/{}'.format(VERSION),
    keywords=['omnifocus', 'productivity', 'tasklist'],
    entry_points={
        'console_scripts': 'ofpy = ofpy.ofpy:main'
        },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4'
        ],
)
