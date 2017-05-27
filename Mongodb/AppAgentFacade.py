#!/usr/bin/env python
# coding=utf8
import Utilitys as Utilitys
import pymongo
import requests
import traceback
import sys
sys.path.append('..')


class AppAgentFacade(object):
    def GetAppAgentDB(self):
        connection = Utilitys.Utilitys.CreateMongodbConnection()
        db = connection.appagent
        return db, connection

    def SaveUserClick(self, udid, multipleurl, appid):

        docBody = {"udid": udid, "multipleurl": multipleurl, "isAcitve": 0, "iscallback": 0, "appid": appid,
                   "dateCreated": Utilitys.Utilitys.UnixTime()}

        db, connection = self.GetAppAgentDB()
        db.usersagent.insert_one(docBody)

    def SaveUserActive(self, udid, appid):

        docBody = {"_id": udid, "appid": appid, "dateCreated": Utilitys.Utilitys.UnixTime()}#create users table
        db, connection = self.GetAppAgentDB()
        user = db.users.find_one({"_id": udid}, {"_id": 1})#search for udid in users table
        if user is None:
            db.users.replace_one({"_id": udid}, docBody, upsert=True)#if not in users insert it
            query = {"udid": udid, "dateCreated": {"$gte": Utilitys.Utilitys.UnixTime() - 3600 * 24}}#re users table udid = udid
            docUserAgent = db.usersagent.find_one(query, sort=[("dateCreated", pymongo.ASCENDING)])#find usersagent udid = udid sort in time
            if docUserAgent is not None:
                isAcitve = docUserAgent["isAcitve"]
                if isAcitve == 0:
                    db.usersagent.update_one({"_id": docUserAgent["_id"]}, {"$set": {"isAcitve": 1}})#change isAcitve ==1

    def CheckIDFAs(self, idfas, appid):
        listIdfas = idfas.split(",")
        dicResult = {}
        db, connection = self.GetAppAgentDB()
        for idfa in listIdfas:
            user = db.users.find_one({"_id": idfa}, {"_id": 1})
            if user is None:
                dicResult[idfa] = 0
            else:
                dicResult[idfa] = 1
        return dicResult
#
    def CallBackUserAgents(self):
        db, connection = self.GetAppAgentDB()
        findResult = db.usersagent.find({"isAcitve": 1, "iscallback": 0}, {"_id": 1, "multipleurl": 1, "udid": 1})
        count = 0
        for item in findResult:
            count += 1
            multipleurl = item["multipleurl"]
            try:
                requests.get(multipleurl)
            except:
                    print traceback.format_exc()

            db.usersagent.update_one({"_id": item["_id"]}, {"$set": {"iscallback": 1}})
            print count, item["udid"]

