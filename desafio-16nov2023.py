#!/usr/bin/python3

import requests
import xmltodict
import re


"""
Faça um script que:

1) Acesse o site https://www.debian.org/security/dsa;
2) Para cada DSA na lista obtida no passo 1, acesse
sua respectiva página e salve o CVE;
3) Imprima na tela o número do DSA seguido de seu
CVE;
"""

URL = "https://www.debian.org/security/dsa"

debian_dsa = requests.get(URL)

debian_dsa_json = xmltodict.parse(debian_dsa.text)

itens = debian_dsa_json['rdf:RDF']['item']

for i in itens:
    print(i['title'].split(" ")[0], end=": ")
    pattern = '.*(https://.*)">'
    mo = re.match(pattern,i['description'])
    dsa_url = mo.group(1)
    resp = requests.get(dsa_url)
    cve_pattern = r'CVE-\d*-\d*'
    mo_cve = re.findall(cve_pattern, resp.text, re.MULTILINE)
    if mo_cve:
        print(' '.join(set(mo_cve)))
    else:
        print("No CVE Found!")


