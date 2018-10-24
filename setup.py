import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

install_reqs = [
    'requests',
]

setuptools.setup(
    name="acrosure_sdk",
    version="1.0.1",
    install_requires=install_reqs,
    author="Jetarin Chokchaipermpoonphol",
    author_email="jetarin.min@gmail.com",
    description="SDK for Acrosure api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jetarin-min/acrosure-py-sdk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
