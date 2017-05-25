#!/usr/bin/env python
# coding=utf8
from urlparse import parse_qs
import json
import traceback
from Mongodb import AppAgentFacade  as AppAgentFacade


def processUserClick(env):
    result = {"message": "返回结果", "success": "true"}
    try:
        query = parse_qs(env['QUERY_STRING'])
        udid = query.get('udid', [''])[0]
        multipleurl = query.get('multipleurl', [''])[0]
        appid = query.get('appid', [''])[0]
        appAgentFacade =AppAgentFacade.AppAgentFacade()
        appAgentFacade.SaveUserClick(udid,multipleurl,appid)

    except:
        result["message"] = traceback.format_exc()
        result["success"] = "false"
    result = json.dumps(result)
    return  result

def processCheckIDFAs(env):
    result = {"message": "返回结果", "success": "true"}
    try:
        query = parse_qs(env['QUERY_STRING'])
        idfa = query.get('idfa', [''])[0]
        appid = query.get('appid', [''])[0]




    except:
        result["message"] = traceback.format_exc()
        result["success"] = "false"
    result = json.dumps(result)
    return  result


def processUserActive(env):
    result = {"message": "返回结果", "success": "true"}
    try:
        query = parse_qs(env['QUERY_STRING'])
        udid = query.get('udid', [''])[0]





    except:
        result["message"] = traceback.format_exc()
        result["success"] = "false"
    result = json.dumps(result)
    return  result


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