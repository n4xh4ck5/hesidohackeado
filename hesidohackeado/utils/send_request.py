#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

def send_request (url):
    response = None

    try:
        response = requests.get(url,timeout=15,allow_redirects=False)

    except Exception as e:
        print "Exception in send_request" + str(e)

    finally:
        return response
