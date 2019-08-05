"""
``splunk_saml_cli_auth`` is a helper tool for authenticating with Splunk on the
CLI when using SAML authentication. This can also be used indirectly to interact
with the Splunk REST API.
"""

import argparse
from urllib.parse import urlparse, urlunparse

import requests
from pycookiecheat import chrome_cookies


def main():
    """
    ``splunk_saml_cli_auth`` is a helper tool for authenticating with Splunk on the
    CLI when using SAML authentication. This can also be used indirectly to interact
    with the Splunk REST API.
    """

    try:
        from requests.packages import urllib3
    except ImportError:
        import urllib3

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--splunkd-port", type=int, default=8089,
                                 help="Port on which splunkd is listening")
    argument_parser.add_argument("--verify-ssl", default=False, action="store_true",
                                 help="Re-enable SSL verification if Splunk is using a verifable "
                                      "certificate on the splunkd port")
    argument_parser.add_argument("url", help="Base URL used when logging into Splunk in Chrome")
    args = argument_parser.parse_args()

    url = urlparse(args.url)

    cookie_name = "splunkd_%s" % args.splunkd_port

    cookies = chrome_cookies(args.url)
    cookies[cookie_name] = cookies["splunkd_443"]

    response = requests.get(
        urlunparse((
            url.scheme,
            "%s:%s" % (url.hostname, args.splunkd_port),
            "/services/authentication/current-context",
            "",
            "",
            ""
        )),
        # urljoin(args.url, "/services/authentication/current-context"),
        params={"output_mode": "json"},
        cookies=cookies,
        verify=False
    )

    username = response.json()["entry"][0]["content"]["username"]

    response = requests.get(
        urlunparse((
            url.scheme,
            "%s:%s" % (url.hostname, args.splunkd_port),
            "/services/server/info",
            "",
            "",
            ""
        )),
        # urljoin(args.url, "/services/authentication/current-context"),
        params={"output_mode": "json"},
        cookies=cookies,
        verify=False
    )

    hostname = response.json()["entry"][0]["content"]["host"]

    print("Save the following as `~/.splunk/authToken_%s_%s` once logged in" % (hostname,
                                                                                args.splunkd_port))
    print("-" * 80)
    print("<auth><username>%s</username><sessionkey>%s</sessionkey>"
          "<cookie>%s</cookie></auth>" % (username, cookies[cookie_name], cookie_name))
    print("-" * 80)
