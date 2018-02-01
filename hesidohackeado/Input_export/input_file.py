#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

def read_input(path):
    """ FUNCTION READ INPUT """
    extension = path.split(".")[1]
    d = []
    inputs = []
    try:
        if extension == "json":
            #Open and read the file n json format
            with open(path) as json_data:
                d =json.loads(json_data.read())
        if extension == "txt":
            with open(path) as f:
                lines = f.readlines()
                for line in lines:
                    d.append(line.rstrip('\n'))
                f.close()
        for k in d:
            inputs.append(k)
    except Exception as e:
        print e
    finally:
        return inputs