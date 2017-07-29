
class Kls(object):

    def __init__(self, data):
        self.data = data

    def printd(self):
        print(self.data)

    @staticmethod
    def smethod(*arg):
        print('Static:', arg)

    @classmethod
    def cmethod(cls, *arg):
        print('cls:', arg)

ik = Kls(12)
ik.printd()
ik.smethod(11)
ik.cmethod(13)
Kls.smethod()
Kls.cmethod()


class Datetest(object):
    day = 0
    month = 0
    year = 0
    def __init__(self,year=0,month=0,day=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def get_date(cls,date_as_string):
        year,month,day = map(int,date_as_string.split('-'))
        date = cls(year,month,day)
        return date

    def out_date(self):
        print('year:',self.year)
        print('month:',self.month)
        print('day:',self.day)

ymd = Datetest.get_date('2017-07-14')
ymd.out_date()