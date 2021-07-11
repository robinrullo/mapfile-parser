#!C:\ms4w\Python\python.exe -u
# -*- coding: utf-8 -*-

import sys
from mappyfile.parser import Parser
from mappyfile.transformer import MapfileToDict

import json

def parse(s):
    """
    Parse, transform and return
    the result
    """
    p = Parser(expand_includes=False, include_comments=True)

    ast = p.parse(s)

    m = MapfileToDict(include_position=False, include_comments=True)

    d = m.transform(ast)

    return d


# Store the http body
data = json.loads(sys.stdin.read())

s = data["mapfile"]


# parse the mapfile and print json
try:
    output = {"status": "success", "mapfile": parse(s)}  
    
except:
    output = {"status": "error", "message": "Bad syntax in the Mapfile or Mapfile not supported", "mapfile": {}}    

print('Content-type: application/json')
print('')
print(json.dumps(output, indent=4))

