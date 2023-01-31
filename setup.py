# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

def get_picklebuilder_version():
    # load picklebuilder.picklebuilder from local path.
    # (Lots of work, just to get the version info)
    from os.path import join, dirname
    import sys
    picklebuilder_path = join(dirname(__file__), 'picklebuilder', 'picklebuilder.py')
    if sys.version_info >= (3, 5):
        # requires Python 3.5 or up.
        import importlib.util
        spec = importlib.util.spec_from_file_location('picklebuilder.picklebuilder', picklebuilder_path)
        picklebuilder = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(picklebuilder)
    else:
        # Python 2.7 support
        import imp
        picklebuilder = imp.load_source('picklebuilder.picklebuilder', picklebuilder_path)
    return picklebuilder.__version__


long_desc = '''
Sphinx_ extension to build and write pickle files.

In itself, the extension is fairly straightforward -- it takes the parsed
reStructuredText file from Sphinx_ and pickles it.

.. _Sphinx: http://sphinx-doc.org/
'''

requires = ['Sphinx>=4.0', 'docutils']

setup(
    name='picklebuilder',
    version=get_picklebuilder_version(),
    url='https://github.com/SamWilsn/picklebuilder',
    download_url='http://pypi.python.org/pypi/picklebuilder',
    license='BSD 2-Clause',
    author='Sam Wilson',
    author_email='sam.wilson@ethereum.org',
    description='Sphinx extension to output pickle files.',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Software Development :: Documentation',
        'Topic :: Text Processing :: Markup :: reStructuredText',
    ],
    platforms='any',
    python_requires='>=3.7',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=requires,
)
