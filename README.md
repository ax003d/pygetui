pygetui
=======

个推服务器端 Python 版

Features
========

目前支持NotifyMsg和LinkMsg两种类型的消息推送，支持离线消息推送。


Examples
========
import getui

client_id = 'xxx'
push_notification('link title', 'link message', 
                  getui.PUSH_TYPE_LINK, [client_id],
                  link='http://www.baidu.com')
push_notification('notify title', 'notify message', 
                  getui.PUSH_TYPE_NOTIFY, [client_id])
