class Clock(object):
    def __init__(self, hours = 0, minutes = 0, seconds = 0 ):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return "the time is {h} hours, {m} minutes and {s} seconds.".format(h = self.hours,
        m = self.minutes, s = self.seconds)

    def get_minute(self):
        return self.minutes

#my_clock = Clock(7,15,35)
#print(my_clock)
#print(my_clock.hours)

class Calender(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return "the date is {y}/{m}/{d}".format(y = self.year, m = self.month, d = self.day)

    def get_year(self):
        return self.year

#mycal = Calender(1399, 7, 18)
#print(mycal)
#print(mycal.year)

class Calclock(Clock, Calender):
    def __init__(self, hours, minutes, seconds, year, month, day, decade):
        Clock.__init__(self, hours, minutes, seconds)
        Calender.__init__(self, year, month, day)
        self.decade = decade

    def __str__(self):
        return "time = {h}:{n}:{s} , date = {y}/{m}/{d}, decade = {D}".format(h=self.hours, n=self.minutes, s=self.seconds,
        y = self.year, m=self.month, d=self.day, D=self.decade)

mycc = Calclock(hours=7, minutes=15, seconds=35, year=1399, month=7, day=18, decade=14)
print(mycc)

print(mycc.get_year())
print(mycc.get_minute())
