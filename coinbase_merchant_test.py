#!/usr/env python

import ConfigParser
from coinbase.wallet.client import Client

Config = ConfigParser.ConfigParser()
Config.read('./config.ini')


def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1


coinbase_api = ConfigSectionMap('Credentials')['api']
coinbase_secret = ConfigSectionMap('Credentials')['secret']

#COINBASE
