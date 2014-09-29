'''setup.py
Setup file for ofpy.
https://github.com/n8henrie/ofpy
'''

# Markdown to RST documentation https://coderwall.com/p/qawuyq
try:
    import pypandoc
except (IOError, ImportError):
    with open('README.md') as r:
        long_description = r.read()
else:
    long_description = pypandoc.convert('README.md', 'rst')


from distutils.core import setup
setup(
    name='ofpy',
    packages=['ofpy'],
    version='0.14',
    description='Add tasks to OmniFocus from Linux',
    long_description=long_description,
    author='Nathan Henrie',
    author_email='nate@n8henrie.com',
    url='http://n8henrie.com/2014/09/ofpy',
    download_url='https://github.com/n8henrie/ofpy/tarball/0.14',
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
