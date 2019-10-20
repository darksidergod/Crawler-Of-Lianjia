#!/usr/bin/env python

import requests


def get_request(url):
        try:
            get_response = requests.get("https://" + url)
            return get_response

        except requests.exceptions.ConnectionError:
            pass

target_url = "<target_url>"


with open("<name of domains to guess", 'r') as word_list:
    for word in word_list:
        stripped_word = word.strip()
        test_url = stripped_word+ "." + target_url
        response = get_request(test_url)

        if response:
            print("[+] Subdomain found." + " It is " + test_url)
