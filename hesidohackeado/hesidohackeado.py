#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from argparse import RawTextHelpFormatter
import argparse

from Input_export.export_file import export_results
from manage_response.manage_response import manage_response
from Input_export.input_file import read_input
from utils.send_request import send_request


def banner():
    """ FUNCTION MAIN """
    print """   
		 _                _     _         _                _                  _      ___  
		| |              (_)   | |       | |              | |                | |    |__ \ 
		| |__   ___   ___ _  __| | ___   | |__   __ _  ___| | _____  __ _  __| | ___   ) |
		| '_ \ / _ \ / __| |/ _` |/ _ \  | '_ \ / _` |/ __| |/ / _ \/ _` |/ _` |/ _ \ / / 
		| | | |  __/ \__ \ | (_| | (_) | | | | | (_| | (__|   <  __/ (_| | (_| | (_) |_|  
		|_| |_|\___| |___/_|\__,_|\___/  |_| |_|\__,_|\___|_|\_\___|\__,_|\__,_|\___/(_)  


      """
    print " \n"
    print """ *** Tool to check if a mail account has been hacked thought 'He sido hackeado' API (https://hesidohackeado.com)
      ** Author: Ignacio Brihuega Rodriguez a.k.a N4xh4ck5
      ** Version 1.0
      ** DISCLAMER: This tool was developed for educational goals. 
      ** Github: https://github.com/n4xh4ck5/
      ** The author is not responsible for using to others goals.
      ** A high power, carries a high responsibility!"""


def help():
    """FUNCTION HELP"""

    print  """ \nTool to check if a mail account has been hacked thought 'He sido hackeado' API (https://hacked-emails.com)
      Example of usage: python hesidohackeado.py -a test@example.com"""


def main(argv):

    """FUNCTION MAIN"""
    parser = argparse.ArgumentParser(description="Tool to verify if a mail account has been hacked throught 'He sido hackeado' API (https:/hacked-emails.com)", formatter_class=RawTextHelpFormatter)
    parser.add_argument('-a','--address', help="Account email which you would like to search",required=False)
    parser.add_argument('-i', '--input', help="File in .txt or json which the email accounts", required=False)
    parser.add_argument('-e', '--export', help="File in xlsx format which the results(y/n)",required=False)
    args = parser.parse_args()

    email = args.address
    path = args.input
    output = args.export

    banner()
    help ()
    #URL API He sido hackedo
    url = "https://hacked-emails.com/api?q="
    input_email = []
    response = None
    #var's to export
    users = []
    results = []
    found = []

    #Treatements input

    if output is None:
        output = 'n'
    output = output.lower()
    if (output != 'y' and output != 'n'):
        print "Incorrect output format selected."
        exit(1)

    if path is not None:
        input_email = read_input(path)
        for email in input_email:
            response = send_request(url+email)
            # Call function to manage results
            users, results,found = manage_response(response)

    else:
        response = send_request(url+email)
        # Call function to manage results
        users,results,found = manage_response(response)

    #Export results
    if output == 'y':
        export_results(users,results,found)

if __name__ == "__main__":
    main(sys.argv[1:])
