from fake_useragent import UserAgent
class Test(object):
    def __init__(self):
        self.ua = UserAgent()
        self.ua_type = 'random'
    
    def printd(self):
        def get_ua():
            return getattr(self.ua,self.ua_type)
        print(get_ua())

Test().printd()