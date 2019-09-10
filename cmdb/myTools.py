import hashlib


class myTools():
    #字符串加密
    def encryption(str):
        if  len(str)==0 or str.isspace():
            return None
        m = hashlib.md5()
        m.update(str.encode(encoding="utf-8"))
        str = m.hexdigest()
        return str
