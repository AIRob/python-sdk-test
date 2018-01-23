#-*- coding:utf-8 -*-
"""
测试Python SDK开发接口
"""

class PythonSDKAPI():
    def __init__(self, attr=None):
        self.attr = attr
 
    def __getattr__(self, attr):
        #应该先判断传入的attr是否已经存在
        return PythonSDKAPI(attr)
 
    def __call__(self, **kwargs):
        return self._request(**kwargs)
 
    def _request(self, **kwargs):
        param = ''
        for k,v in kwargs.items():
            param = '%s=%s' % (k, v)
        url = 'http://aiapi.org/%s?%s' % ( self.attr,param) 
        return  url
 
if __name__ == '__main__':
    apitest = PythonSDKAPI()
    print (apitest.datapi(datapi_id=128))
    print ("Python SDK Test OK!")


