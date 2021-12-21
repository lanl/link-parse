import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="linkparse",
    version="1.0.0",
    author="Bhnauka Mahanama",
    author_email="bhanuka@lanl.gov",
    description="Link header parsing library for mementos",
    keywords=["Memento", "Link Header", "Web archiving"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lanl/link-parse",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development"
    ],
    python_requires=">=3.7",
)