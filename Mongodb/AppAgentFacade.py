#!/usr/bin/env python
# coding=utf8


import Utilitys as Utilitys

class AppAgentFacade(object):

    def GetAppAgentDB(self):
        connection = Utilitys.Utilitys.CreateMongodbConnection()
        db = connection.appagent
        return db, connection

    def SaveUserClick(self,udid,multipleurl,appid):

        docBody ={"udid":udid,"multipleurl":multipleurl, "isAcitve":0,"appid":appid,"dateCreated":Utilitys.Utilitys.UnixTime()}

        db, connection = self.GetAppAgentDB()
        db.usersagent.insert_one(docBody)

    def SaveUserActive(self,idfa,appid):

        docBody ={"_id":idfa,"appid":appid,"dateCreated":Utilitys.Utilitys.UnixTime()}

        db,connection = self.GetAppAgentDB()

        user= db.usersagent.find_one({"udid":idfa},{"_id":1})
        if user is not None:
            db.users.find_one_and_update({"_id":idfa},docBody,{'$inc': {idfa: '1'}})

        else:
            db.users.find_one_and_update({"_id":idfa},docBody,{'$inc': {idfa: '0'}})
        return db.users


    def UpdateAppAgent(self,udid):
        db, connection = self.GetAppAgentDB()
        UserIsActive= db.usersagent.fine_one({'udid':udid})
        UserIsActive['isAcitve']= '1'
        db.usersagent.save(UserIsActive)
    def FindAppAgent(self,udid):
        db, connection = self.GetAppAgentDB()
        udidFindAppAgent=db.users.find_one({"_id":udid},{"_id":1})
        return udidFindAppAgent










