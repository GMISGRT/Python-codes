import datetime
x=datetime.datetime.now()
print(x)

import datetime

from datetime import *
x=datetime.now()
print(x)

print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)
print(x.second)
print(x.microsecond)
print(x.strftime("&a"))

y=datetime(2022, 12, 24)
print(y)
print(x.strftime("%b"))
print(x.strftime("%a"))
print(x.strftime("%w"))
print(x.strftime("%m"))
print(x.strftime("%p"))
print(x.strftime("%z"))
print(x.strftime("%X"))
print(x.strftime("%c"))

from datetime import *
date_time = "2022-06-09 09:00:00"
target = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
now = datetime.now()
print(target)