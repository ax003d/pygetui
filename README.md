pygetui
=======

个推服务器端 Python 版

Features
========

目前支持NotifyMsg和LinkMsg两种类型的消息推送，支持离线消息推送。


Examples
========

```
from pygetui import *
    
gx = GXPushClient(appid='your appid',
                  appkey='your appkey',
                  mastersecret='your mastersecret')
test_client = 'xxx'
gx.push_notification('link title', 'link message',
                      PUSH_TYPE_LINK, [test_client],
                      link='http://www.baidu.com')
gx.push_notification('notify title', 'notify message',
                      PUSH_TYPE_NOTIFY, [test_client])
                         
```
