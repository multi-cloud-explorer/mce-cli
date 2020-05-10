import os

from setuptools import setup, find_packages

install_requires = [
    'python-decouple',
    'python-dotenv',
    'requests',
]

tests_requires = [
    'pytest>=5.4.1',
    'pytest-cov',
    'pytest-pep8',
    'pytest-vcr',
    'vcrpy',
    'bandit',
    'flake8',
    'coverage',
    'responses',
    'freezegun',
]

dev_requires = [
    'pylint',
    'ipython',
    'autopep8',
    'black',
]

doc_requires = [
    'Sphinx>=3.0',
    'sphinx_rtd_theme',
    'sphinx-click',
    'sphinx-autodoc-typehints'
]

extras_requires = {
    'tests': tests_requires,
    'dev': dev_requires,
    'doc': doc_requires,
    'gevent': [
        'gevent',
        'gevent-openssl',
    ]
}

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='mce-cli',
    version="0.1.0",
    description='Rest Client for MCE Explorer',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/multi-cloud-explorer/mce-cli.git',
    license='GPLv3+',
    packages=find_packages(exclude=("tests",)),
    include_package_data=True, 
    tests_require=tests_requires,
    install_requires=install_requires,
    extras_require=extras_requires,
    test_suite='tests',
    zip_safe=False,
    author='Stephane RAULT',
    author_email="stephane.rault@radicalspam.org",
    python_requires='>=3.7',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    entry_points={
        'console_scripts': [
            #'mce-az = mce_cli.cli:main',
        ],
    }
)
