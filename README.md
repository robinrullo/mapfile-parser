# Mapfile Parser

This is a simple API using the python mapfile parser [mappyfile](https://github.com/geographika/mappyfile) through CGI of MS4W to parse Mapfiles to JSON.



## Installation:

- Clone this repo to */ms4w/apps/*
- Run script **install-mappyfile-ms4w.py**
- Copy **httpd_mapfile-parser.conf** to */ms4w/httpd.d/*

## Usage:

Send request (all http methods supported) with a JSON body and the Mapfile to parse into it:

```json
{
    "mapfile": "MAP ... END"
}
```



It always return the status:

- `success`

```json
{
    "status": "success",
    "mapfile": {
        "__type__": "map",
        "__comments__": {}
    }
}
```

- `error`

```json
{
    "status": "error",
    "message": "Bad syntax in the Mapfile or Mapfile not supported",
    "mapfile": {}
}
```

