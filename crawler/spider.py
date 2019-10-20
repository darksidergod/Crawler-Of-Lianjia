#!/usr/bin/env python

import requests
import re
import urlparse


def link_extractor(url):
    sv_response = requests.get(url)
    href_dat = re.findall('(?:href=")(.*?)"', sv_response.content)
    return href_dat



def crawl(target_url):
    links_found = link_extractor(target_url)
    for link in links_found:
        link = urlparse.urljoin(target_url, link)

        if "#" in link:
            link = link.split("#").[0]

        if target_url in link and link not in links_list:
            links_list.append(link)
            print(link)
            crawl(link)


links_list = []
attack_url = "<attack-url>"
crawl(attack_url)
