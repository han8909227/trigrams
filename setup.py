from setuptools import setup

setup(
    name='trigrams',
    author='Megan Flood, Han Bao, and Fortunato Maycotte',
    author_email='hbao2016@hotmail.com',
    description='Generates a book from another book using trigrams.',
    package_dir={'': 'src'},
    py_modules=['trigrams'],
    install_requires=[],
    extras_require={
        'test': ['pytest', 'pytest-watch', 'pytest-cov']
    },
)
