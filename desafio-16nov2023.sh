#!/usr/bin/bash

: '
Faça um script que:

1) Acesse o site https://www.debian.org/security/dsa;
2) Para cada DSA na lista obtida no passo 1, acesse
sua respectiva página e salve o CVE;
3) Imprima na tela o número do DSA seguido de seu
CVE;
'

URL="https://www.debian.org/security/dsa"

debian_dsa=$(curl -s https://www.debian.org/security/dsa | grep href| cut -d ';' -f3 | sed s/\&....$// 2>-)


#echo -e $debian_dsa

for dsa_link in $debian_dsa; do
    dsa=$(echo $dsa_link | rev | cut -d '/' -f 1 | rev)
    cve=$(curl -s $dsa_link | grep -Eo CVE-[[:digit:]]{4}-[[:digit:]]* | sort -u | tr '\n' ' ' )
    if [ -z "$cve" ]; then
        cve="No CVE Found!"
    fi
    echo -e "$dsa: $cve"
done
