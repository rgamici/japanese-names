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

input_name = "male-count"
output_name = "male-finished"
dict_name = "edict2"


def soup(html):
    soup = BeautifulSoup(html, 'html.parser')
    ba = soup.find_all("div", id="inf")
    # print(ba[0].text)
    count = re.search(r'^.*約(.*)件', ba[0].text).group(1)
    count = count.replace(',', '')
    # print(count)
    # print(soup.prettify())
    return(count)


def prepare_dict():
    edic = open(dict_name, 'r')
    words = dict()
    for line in edic:
        word = re.search(r'^(.*?) .*$', line).group(1)
        if word not in words:
            words.update({word: None})
    return(words)


if __name__ == "__main__":
    input_file = open(input_name, 'r')
    output = open(output_name, 'w')
    words = prepare_dict()
    count = 0
    for line in input_file:
        entry = re.search(r'^(.*?) .*$', line).group(1)
        if entry in words.keys():
            print(entry + " found in edict2")
            count += 1
            output.write(line[:-1] + " -- edict2\n")
        else:
            output.write(line)
            pass
    print(str(count) + " words in dict")
    output.close()
