#!/usr/bin/env python3

import requests
import sys
from datetime import datetime

API_KEY = ""
FQDN = ""
RRSET_NAME = ""
RRSET_TYPE = ""

TTL = 500

def get_public_ipv4():
    res = requests.get("https://4.ident.me")
    return res.text

def update_record(api_key, fqdn, rrset_name, rrset_type, ip, ttl):
    api_url = "https://api.gandi.net/v5/livedns/domains/" + fqdn + "/records/" + rrset_name + "/" + rrset_type
    headers = {"Authorization": "ApiKey " + api_key, "Content-Type": "application/json; charset=utf-8"}
    data = '{"rrset_values" : ["' + ip + '"], "rrset_ttl": ' + str(ttl) + '}'
    response = requests.put(api_url, data=data, headers=headers)
    return response.status_code, response.json()

PUB_IP = get_public_ipv4()

print("[+] " + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

if PUB_IP == "":
    print("[!] Couldn't get public IP ! Aborting.")
    sys.exit(-1)
else:
    print("[+] Updating DNS record name '" + RRSET_NAME + "' of type '" + RRSET_TYPE + "' for domain '" + FQDN + "' to '" + PUB_IP + "' ...")
    status, content = update_record(API_KEY, FQDN, RRSET_NAME, RRSET_TYPE, PUB_IP, TTL)

    if status != 201:
        print(f"[-] Error ! HTTP Status: {status}; Message: {content}")
    else:
        print(f"[+] DNS record successfully updated: {content}")

    print("[*] Done.\n")
    sys.exit(0)

