splunk_saml_cli_auth - Interact with Splunk on the CLI using SAML authentication
================================================================================

|Build Status|

``splunk_saml_cli_auth`` is a helper tool for authenticating with Splunk on the
CLI when using SAML authentication. This can also be used indirectly to interact
with the Splunk REST API.

Installation
------------

``splunk_saml_cli_auth`` can be installed using pip3:

::

    pip3 install splunk_saml_cli_auth

Or, if you're feeling adventurous, can be installed directly from
github:

::

    pip3 install git+https://github.com/HurricaneLabs/splunk_saml_cli_auth.git

Usage
-----

::

    usage: splunk-saml-cli-auth [-h] [--splunkd-port SPLUNKD_PORT] [--verify-ssl]
                                url

    positional arguments:
      url                   Base URL used when logging into Splunk in Chrome

    optional arguments:
      -h, --help            show this help message and exit
      --splunkd-port SPLUNKD_PORT
                            Port on which splunkd is listening
      --verify-ssl          Re-enable SSL verification if Splunk is using a
                            verifable certificate on the splunkd port

Known Issues
------------
-  None so far!

Version History
---------------

Version 0.1.0 (2019-08-05)
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Initial release

License Info
------------

The MIT License (MIT)

Copyright (c) 2019 Hurricane Labs LLC

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

.. |Build Status| image:: https://travis-ci.org/HurricaneLabs/splunk-saml-cli-auth.svg?branch=master
    :target: https://travis-ci.org/HurricaneLabs/splunk-saml-cli-auth
