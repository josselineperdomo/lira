import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="pylearn",
    version="0.0.1rc1",
    author="Python Ecuador",
    author_email="ecuadorpython@gmail.com",
    description="Tutorial interactivo de Python en tu terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={"pylearn": ["*.rst"]},
    install_requires=[],
    extras_require={"dev": ["black"], "tests": ["pytest"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    project_urls={
        "Homepage": "https://github.com/pythonecuador/pylearn/",
        "Source Code": "https://github.com/pythonecuador/pylearn/",
        "Issue Tracker": "https://github.com/pythonecuador/pylearn/issues",
    },
)
