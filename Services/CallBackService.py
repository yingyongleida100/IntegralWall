#!/usr/bin/env python
# coding=utf8
from Mongodb import AppAgentFacade as AppAgentFacade
import traceback

class AppAgentFacade(object):
    def Dojob(self):
        while True:
            try:
                appAgentFacade = AppAgentFacade.AppAgentFacade()
                appAgentFacade.CallBackUserAgents()
            except:
                print traceback.format_exc()