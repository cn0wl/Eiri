#!/usr/bin/env python

import json
import eml_parser
import datetime
import sys
from art import *

def usage():
    tprint("Eiri")
    print("usage: python3 Eiri.py [service] [arquivo.eml] \n")

def outlook(dict_t):
    print("[From]: " + dict_t["header"]["header"]["from"][0])
    print("[To]: " + dict_t["header"]["to"][0])
    print("[X-Sender-IP]: " + dict_t["header"]["header"]["x-sender-ip"][0])
    print("[Message-ID]: " + dict_t["header"]["header"]["message-id"][0] + "\n")
    print("[Authentication-Results]: " + dict_t["header"]["header"]["authentication-results"][0] + "\n")

    print("[Received-SPF]: " + dict_t["header"]["header"]["received-spf"][0] + "\n")


def gmail(dict_t):
    print("[From]: " + dict_t["header"]["header"]["from"][0])
    print("[To]: " + dict_t["header"]["to"][0])
    print("[Message-ID]: " + dict_t["header"]["header"]["message-id"][0] + "\n")
    print("[Authentication-Results]: " + dict_t["header"]["header"]["authentication-results"][0] + "\n")
    print("[Received-SPF]: " + dict_t["header"]["header"]["received-spf"][0] + "\n")



def json_serial(obj):
    serial = obj.isoformat()
    return serial

with open(sys.argv[2], 'rb') as file:
    raw_email = file.read()

ep = eml_parser.EmlParser()
parsed_eml = ep.decode_email_bytes(raw_email)

dump = json.dumps(parsed_eml, indent=2, default=json_serial)
dict_t = json.loads(dump)

usage()

if (sys.argv[1].upper() == "OUTLOOK"):
    outlook(dict_t)
elif (sys.argv[1].upper() == "GMAIL"):
    gmail(dict_t)