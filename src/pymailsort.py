#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys, os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

LOGFILENAME = None
DEFAULTDIR = ""

import datetime
import email
import re
from optparse import OptionParser

def header_regex_classifier(headername, value):
    regexes = [
        ('To', '.*' , 'PYMAILSORTERROR')
    ]
    configfile = "bin/pymailsort_cfg.py"
    if os.path.isfile(configfile):
        from pymailsort_cfg import regexes

    for (headerfilter, regex, result) in regexes:
        if headername != headerfilter:
            continue
        compiledre = re.compile("^%s$" % regex, re.MULTILINE | re.DOTALL)
        if compiledre.match(value):
            log("sorting to %s because %s matches %s in %s" % (result, value, regex, headername))
            return result

    return None

def process_mail(mailfile):
    log("checking new mail")
    msg = email.message_from_file(mailfile)

    for part in msg.walk():
        for headername, value in part.items():
            classification = header_regex_classifier(headername, value)
            if classification is not None:
                return classification
    return DEFAULTDIR

def process_mail_wrapper(mailfile):
    try:
        return process_mail(mailfile)
    except:
        return DEFAULTDIR

def log(line):
    if LOGFILENAME is None:
        return
    filehandle = open(LOGFILENAME, 'a')
    timestamp = datetime.datetime.now().isoformat()
    print("%s %s" % (timestamp, line), file=filehandle)
    filehandle.close()

def main(args, mailfile):
    parser = OptionParser(description="""
    this is the pymailsort main script
    """.strip())

    parser.add_option("--logfilename",
                        dest    = "logfilename",
                        action  = "store",
                        help    = "logfilename",
                        default = None
    )
    (options, args) = parser.parse_args(args)

    global LOGFILENAME
    LOGFILENAME = options.logfilename
    return process_mail_wrapper(mailfile)

if __name__ == '__main__':
    mailbox = main(sys.argv[1:], sys.stdin)
    if mailbox == "":
        print("")
    else:
        print("/.INBOX.%s" % mailbox)
