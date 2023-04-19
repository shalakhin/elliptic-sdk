import setuptools

with open('README.md', 'r') as f:
    description = f.read()

setuptools.setup(
    name="elliptic",
    version="0.0.1",
    author="Olexandr Shalakhin",
    author_email="olexandr@shalakhin.com",
    description=description,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
