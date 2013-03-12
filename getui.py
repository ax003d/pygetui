#!/usr/bin/env python
# coding: utf-8

__version__ = '0.1'
__author__  = 'ax003d@gmail.com'

'''
Python SDK for getui server API.

Usage:
1. Replace APPID, APPKEY, MASTERSECRET for your own values
2. Set test_client in last lines for testing
3. run:
   python getui.py
   The console will show JSON response from getui.
'''

import md5
import simplejson
import types
import urllib
import urllib2

APPID = ''
APPKEY = ''
MASTERSECRET = ''
APIURL = 'http://sdk.open.api.igexin.com/service'

PUSH_TYPE_TRANSMISSION = 'TransmissionMsg' # Not supported yet
PUSH_TYPE_LINK         = 'LinkMsg'
PUSH_TYPE_NOTIFY       = 'NotifyMsg'


def push_notification(title, message, push_type, subscribers,
                      link=None):
    params = {}
    params['appkey'] = APPKEY
    params['pushTitle'] = title
    params['pushType'] = push_type
    params['tokenMD5List'] = subscribers

    params['type'] = 2
    params['action'] = 'pushSpecifyMessage'
    params['offline'] = True
    params['offlineTime'] = 2
    params['priority'] = 1

    msg = {}
    if push_type == PUSH_TYPE_LINK:
        msg['linkMsgIcon'] = 'ic_launcher.png'
        msg['linkMsgTitle'] = title
        msg['linkMsgContent'] = message
        msg['linkMsgUrl'] = link
    elif push_type == PUSH_TYPE_NOTIFY:
        msg['notifyMsgIcon'] = 'ic_launcher.png'
        msg['notifyMsgTitle'] = title
        msg['notifyMsgContent'] = message
        msg['transmissionContent'] = ''
        msg['transmissionType'] = 1
    params['msg'] = msg

    sign = [MASTERSECRET]
    for i in sorted(params.keys()):
        if type(params[i]) in [types.StringType, types.IntType, types.LongType]:
            sign.append(i)
            sign.append(str(params[i]))
    params['sign'] = md5.md5(''.join(sign)).hexdigest()

    data = simplejson.dumps(params)
    req = urllib2.Request(APIURL, data)
    response = urllib2.urlopen(req)
    print response.read()
    

if __name__=='__main__':
    test_client = 'xxx'
    push_notification('link title', 'link message', 
                      PUSH_TYPE_LINK, [test_client],
                      link='http://sichu.sinaapp.com')
    push_notification('notify title', 'notify message', 
                      PUSH_TYPE_NOTIFY, [test_client])
