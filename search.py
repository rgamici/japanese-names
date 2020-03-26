#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import codecs
import time
import re
import random
from fake_useragent import UserAgent
from urllib.request import Request, urlopen
import urllib.parse
from bs4 import BeautifulSoup

# Local Vars

input_name = "input"
output_name = "output"

ua = UserAgent()  # From here we generate a random user agent
proxies = []  # Will contain proxies [ip, port]
no_proxy = True


def get_proxies():
    global proxies
    # Retrieve latest proxies
    proxies_req = Request('https://www.sslproxies.org/')
    proxies_req.add_header('User-Agent', ua.random)
    proxies_doc = urlopen(proxies_req).read().decode('utf8')

    soup = BeautifulSoup(proxies_doc, 'html.parser')
    proxies_table = soup.find(id='proxylisttable')

    # Save proxies in the array
    for row in proxies_table.tbody.find_all('tr'):
        proxies.append({
            'ip':   row.find_all('td')[0].string,
            'port': row.find_all('td')[1].string
        })
    proxies = proxies[:75]  # trim it to allow no proxy more often
    print("Got new proxies")


# Retrieve a random index proxy (we need the index to delete it if not working)
def random_proxy():
    global no_proxy
    if len(proxies) < 10:  # list almost exhausted
        get_proxies()
        no_proxy = True
    return random.randint(0, len(proxies) - 1)


def get_no_proxy(entry):
    # url https://search.yahoo.co.jp/search?p=
    url = ("https://search.yahoo.co.jp/search?p="
           + urllib.parse.quote(entry, encoding="utf-8"))
    try:
        html = urllib.request.urlopen(url)
        return(html)
    except:
        return(-1)


def get_proxy(entry, proxy_index):
    proxy = proxies[proxy_index]
    url = ("https://search.yahoo.co.jp/search?p="
           + urllib.parse.quote(entry, encoding="utf-8"))
    req = Request(url)
    # req.add_header('User-Agent', ua.random)
    req.set_proxy(proxy['ip'] + ':' + proxy['port'], 'http')
    # Make the call
    try:
        html = urlopen(req).read().decode('utf8')
        return(html)
    except:  # If error, delete this proxy and find another one
        return(-1)


def soup(html):
    soup = BeautifulSoup(html, 'html.parser')
    ba = soup.find_all("div", id="inf")
    # print(ba[0].text)
    count = re.search(r'^.*約(.*)件', ba[0].text).group(1)
    count = count.replace(',', '')
    # print(count)
    return(count)
    # print(soup.prettify())


if __name__ == "__main__":
    input_file = open(input_name, 'r')
    output = open(output_name, 'r+')
    results = list()
    get_proxies()
    # Choose a random proxy
    proxy_index = random_proxy()
    first_scan = True
    for line in input_file:
        if first_scan:
            entry = re.search(r'^(.*?) .*$', line).group(1)
            check_output = output.readline()
            if re.search(r'^'+entry, check_output):
                # already searched
                # print("Already searched " + entry)
                # print(line[:-1] + " -- " + "0")
                continue
                pass
            else:
                first_scan = False
        # Found entries that were not searched yet
        # print(str(entry) + " - " + str(line))
        while True:
            if no_proxy:
                result = get_no_proxy(entry)
                if result != -1:  # no page error
                    count = soup(result)
                    break
                else:
                    print("Failed to scrap with no proxy")
                    no_proxy = False
            else:
                result = get_proxy(entry, proxy_index)
                if result != -1:
                    count = soup(result)
                    break
                else:
                    proxy = proxies[proxy_index]
                    del proxies[proxy_index]
                    print('Proxy ' + proxy['ip'] + ':' +
                          proxy['port'] + ' deleted.')
                    proxy_index = random_proxy()
        print(line[:-1] + " -- " + count)
        output.write(line[:-1] + " -- " + count + "\n")
        output.close()
        output = open(output_name, 'a')
    output.close()
