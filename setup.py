from setuptools import setup, find_packages


VERSION = "1.0.0"

setup(
    name="splunk-saml-cli-auth",
    version=VERSION,
    author="Steve McMaster",
    author_email="mcmaster@hurricanelabs.com",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    description="Helper for authenticating to Splunk on CLI when using SAML auth",
    long_description_content_type="text/markdown",
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
    ]
)
