#!/usr/bin/env python
# coding=utf8
import datetime
import uuid
import Utilitys as Utilitys

class AppAgentFacade(object):

    def GetAppAgentDB(self):
        connection = Utilitys.Utilitys.CreateMongodbConnection()
        db = connection.appagent
        return db, connection

    def SaveUserClick(self,udid,multipleurl,appid):

        docBody ={"udid":udid,"multipleurl":multipleurl, "isAcitve":0,"appid":appid,"dateCreated":Utilitys.Utilitys.GetNow()}

        db, connection = self.GetAppAgentDB()
        db.users.insert_one(docBody)

        pass
    pass