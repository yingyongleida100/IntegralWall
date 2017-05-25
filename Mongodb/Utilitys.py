#!/usr/bin/env python
# coding=utf8
import datetime
from pymongo import MongoClient


class Utilitys(object):
    connection =None
    @staticmethod
    def CreateMongodbConnection():
        if(Utilitys.connection==None):
            mongodbServerIp="127.0.0.1"
            mongodbPort=27017
            Utilitys.connection = MongoClient(mongodbServerIp, mongodbPort, waitQueueTimeoutMS=60000)
        return Utilitys.connection

    @staticmethod
    def GetNow():
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
