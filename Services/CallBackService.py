#!/usr/bin/env python
# coding=utf8
from time import sleep
import datetime
from Mongodb import AppAgentFacade
import traceback
import sys
sys.path.append('..')

def Dojob():
    while True:
        try:
            appAgentFacade = AppAgentFacade.AppAgentFacade()
            appAgentFacade.CallBackUserAgents()
        except:
            print traceback.format_exc()
        print "CallBackUserAgents ok %s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sleep(5)

Dojob()
