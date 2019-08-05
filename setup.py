from setuptools import setup


VERSION = "0.1.1"


with open("README.rst", "r") as f:
    long_description = f.read()


setup(
    name="splunk-saml-cli-auth",
    version=VERSION,
    author="Steve McMaster",
    author_email="mcmaster@hurricanelabs.com",
    py_modules=["splunksecrets"],
    description="Helper for authenticating to Splunk on CLI when using SAML auth",
    long_description=long_description,
    install_requires=[
        "pycookiecheat",
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "splunk-saml-cli-auth = splunk_saml_cli_auth:main",
        ]
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 5 - Production/Stable",
    ],
    bugtrack_url="https://github.com/HurricaneLabs/splunk-saml-cli-auth/issues",
)
