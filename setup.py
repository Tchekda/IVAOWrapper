import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="IVAOWrapper",
    version="0.0.1",
    author="Tchekda",
    author_email="contact@tchekda.fr",
    description="Light Python Wrapper for IVAO Network",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tchekda/IVAOWrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['requests'],
    test_suite='nose.collector',
    tests_require=['nose'],
)