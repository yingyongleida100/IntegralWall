#!/usr/bin/env python
# coding=utf8
from urlparse import parse_qs
import json
import traceback
import sys
import os
dir_path =os.path.dirname(os.path.realpath(__file__)).replace("Web","")
if dir_path not in sys.path :
    sys.path.append(dir_path)
from Mongodb import AppAgentFacade  as AppAgentFacade

def processUserClick(env):
    result = {"message": "返回结果", "success": "true"}
    try:
        query = parse_qs(env['QUERY_STRING'])
        udid = query.get('udid', [''])[0]
        multipleurl = query.get('multipleurl', [''])[0]
        appid = query.get('appid', [''])[0]
        appAgentFacade = AppAgentFacade.AppAgentFacade()
        appAgentFacade.SaveUserClick(udid, multipleurl, appid)

    except:
        result["message"] = traceback.format_exc()
        result["success"] = "false"
    result = json.dumps(result)
    return result


# save udid into mongodb.userAgent return result

def processCheckIDFAs(env):
    result = {}
    try:
        if env['REQUEST_METHOD'].upper() == 'POST':

            try:
                request_body_size = int(env.get('CONTENT_LENGTH', 0))
            except(ValueError):
                request_body_size = 0

            request_body = env['wsgi.input'].read(request_body_size)
            query = parse_qs(request_body)
            idfas = query.get('idfa', [''])[0]
            appid = query.get('appid', [''])[0]
        elif env['REQUEST_METHOD'].upper() == 'GET':
            query = parse_qs(env['QUERY_STRING'])
            idfas = query.get('idfa', [''])[0]
            appid = query.get('appid', [''])[0]
        appAgentFacade = AppAgentFacade.AppAgentFacade()
        result = appAgentFacade.CheckIDFAs(idfas, appid)
    except:
        print traceback.format_exc()
    result = json.dumps(result)
    return result


# if idfa not in udid save idfa in to mongodb.users return result
#

def processUserActive(env):
    result = {"message": "返回结果", "success": "true"}
    try:
        query = parse_qs(env['QUERY_STRING'])
        udid = query.get('udid', [''])[0]
        appid = query.get('appid', [''])[0]
        appAgentFacade = AppAgentFacade.AppAgentFacade()
        appAgentFacade.SaveUserActive(udid, appid)


    except:
        result["message"] = traceback.format_exc()
        result["success"] = "false"
    result = json.dumps(result)
    return result


# when udid in users.idfa and creat time < one day and top(1) then change useragent.isActive = 1

def application(env, start_response):
    query = parse_qs(env['QUERY_STRING'])
    word = query.get('t', [''])[0]
    if word == 'click':
        response_body = processUserClick(env)

    elif word == 'checkidfa':
        response_body = processCheckIDFAs(env)

    elif word == 'active':
        response_body = processUserActive(env)
    else:
        response_body = "Params Error"
    response_headers = [('Content-Type', 'text/json'), ('Content-Length', str(len(response_body)))]
    start_response('200 OK', response_headers)
    return response_body
