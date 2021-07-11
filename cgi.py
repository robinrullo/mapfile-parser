#!C:\ms4w\Python\python.exe -u
# -*- coding: utf-8 -*-

import sys
from mappyfile.parser import Parser
from mappyfile.transformer import MapfileToDict
from mappyfile.validator import Validator

import json

def parse(s):
    """
    Parse, transform and return
    the result
    """
    p = Parser(expand_includes=False, include_comments=True)

    ast = p.parse(s)

    m = MapfileToDict(include_position=True, include_comments=True)

    d = m.transform(ast)

    return d

def validate(d):
    v = Validator()
    e = v.validate(d, add_comments=True, version=7.6)
    return e

# Read the http body and get the mapfile string
data = json.loads(sys.stdin.read())
s = data["mapfile"]


# Parse and validate the mapfile
try:
    d = parse(s)
    e = validate(d)
    output = {
        "status": "success",
        "validation": e,
        "mapfile": d
    }   
except:
    output = {
        "status": "error",
        "message": "Bad syntax in the Mapfile or Mapfile not supported",
        "validation": [],
        "mapfile": {}
    }    

# Print JSON
print('Content-type: application/json')
print('')
print(json.dumps(output, indent=4))
