"""Elliptic SDK setup.py."""
import setuptools

with open('README.md', 'r') as readme_file:
    description = readme_file.read()

setuptools.setup(
    name='elliptic_sdk',
    version='0.0.6',
    author='Olexandr Shalakhin',
    author_email='olexandr@shalakhin.com',
    description=description,
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
