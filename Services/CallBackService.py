#!/usr/bin/env python
# coding=utf8
from time import sleep
import datetime
import traceback
import sys
import os
dir_path = sys.path.append(os.path.dirname(os.path.realpath(__file__)).replace("Services",""))
if dir_path not in sys.path :
    sys.path.append(dir_path)
from Mongodb import AppAgentFacade

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
