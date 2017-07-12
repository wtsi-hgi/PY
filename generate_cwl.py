#!/bin/python

import requests
import os
import json
import sys
from bs4 import BeautifulSoup

# import json2cwl.py



r = requests.get("https://software.broadinstitute.org/gatk/documentation/tooldocs/3.5-0/")
data = r.text

soup = BeautifulSoup(data, "html.parser")
#print(soup)

url_list = []

for sub in soup.find_all('tr'):
    for stuff in sub.find_all('td'):
        for a in stuff.find_all('a', href = True):
            url_list.append(a['href'] + ".json")

for x in url_list:
    print(x)

# directory = sys.argv[1]
# version = sys.argv[2]

# dirFiles = os.listdir(directory)
