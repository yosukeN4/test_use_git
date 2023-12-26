import datetime

class DateTimeHelper(object):
    """ date and datetime に作用する機能を持つクラス """
    def today(self):
        """ return datetime of today """
        return datetime.datetime.now()
    
    def date(self):
        return self.today().strftime("%d/%m/%Y")
    
    def weekday(self):
        return self.today().strftime("%A")

    def us_to_indian(self, date):
        mm,dd,yy = date.split('/')
        yy = int(yy)
        if yy <= 16:
            yy += 2000
        date_obj = datetime.date(year=yy, month=int(mm), day=int(dd))
        return date_obj.strftime("%d/%m/%Y")