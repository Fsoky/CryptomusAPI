from setuptools import setup, find_packages
from io import open


def read(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


setup(
    name="CryptomusAPI",
    version="1.0.1",
    description="Easy interaction with Cryptomus API, support for asynchronous approaches",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Fsoky",
    url="https://github.com/Fsoky/CryptomusAPI",
    author_email="cyberuest0x12@gmail.com",
    keywords="api cryptomus asyncio crypto cryptomusapi",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages()
)
