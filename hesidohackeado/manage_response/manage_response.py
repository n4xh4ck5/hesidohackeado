#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

def manage_response(response):
    #var's local
    users =[]
    results =[]
    found = []

    try:

        data = response.json()
        print "\n[*]checking email account: " + data['query']
        print "Email Hacked: " + data['status']
        print "Results: " + str(data['results'])
        users.append(str(data['query']))
        results.append(str(data['results']))
        found.append(str(data['status']))

    except Exception as e:
        print "Exception in manage_response " + str(e)
    finally:
        return users,results,found