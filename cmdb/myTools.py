import hashlib
import json


class myTools():
    #字符串加密
    def encryption(str):
        if  len(str)==0 or str.isspace():
            return None
        m = hashlib.md5()
        m.update(str.encode(encoding="utf-8"))
        str = m.hexdigest()
        return str
class myHttpReturnData():
    def returnAnswer(self,_type=0,_answer='',_errors=''):
        data = {
            'type':_type,
            'answer':_answer,
            'errors':_errors
        }
        return json.dumps(data)