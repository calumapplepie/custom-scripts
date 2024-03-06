#!/usr/bin/python3
from bs4 import BeautifulSoup
import json
import argparse
from pycountry import languages

parser = argparse.ArgumentParser()
parser.add_argument("book")
args = parser.parse_args()
bookname = args.book

metadata_json = {}

try:
    with open ('metadata.opf', 'r') as f:
        file = f.read()
except Exception as error:
    print("An error occurred while opening metadata.opf:\n\t", type(error).__name__, error)
    exit(1)


metadata = BeautifulSoup(file, 'xml')

metadata_json['title'] = metadata.find('dc:title').text

authors = metadata.find_all('dc:creator', attrs={"opf:role": "aut"})
metadata_json['authors'] = []
for author in authors:
    if ',' in author.text:
        metadata_json['authors'].append(" ".join(author.text.split(", ")[::-1]))
    else:
        metadata_json['authors'].append(author.text)

metadata_json['isbn'] = metadata.find('dc:identifier', attrs={"opf:scheme": "ISBN"}).text
metadata_json['language'] = languages.get(alpha_3=metadata.find('dc:language').text).name
metadata_json['tags'] = ",".join(str(tag.text) for tag in metadata.find_all('dc:subject'))
metadata_json['description'] = metadata.find('dc:description').text

json_file = bookname + ".json"
try:
    out_file = open(json_file, "w")
    json.dump(metadata_json, out_file, indent = 4)
    out_file.close()
except Exception as error:
    print("An error occurred when saving to",json_file,":\n\t", type(error).__name__, error)
    exit(1)
