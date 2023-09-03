'''Write a Python script to display the
a) Current date and time
b) Current year
c) Month of year
d) Week number of the year
e) Weekday of the week
f) Day of year
g) Day of the month
h) Day of week
'''

#a) Current date and time
from datetime import datetime
current=datetime.now()
date_time=current.strftime("%d %m %Y %H:%M:%S")
print("current date and time:",date_time)

#b) Current year

from datetime import datetime
current=datetime.now()
year=current.strftime("%Y")
print("current_year is:",year)

#c)Month of year

from datetime import datetime
current=datetime.now()
month=current.strftime("%m %Y")
print("month of the year",month)

#d) Week number of the year
from datetime import datetime
current=datetime.now()
week=current.strftime("%w %m %Y")
print("week number of the year:",week)

#e) Weekday of the week

from datetime import datetime
current=datetime.now()
week_day=current.strftime("%A %w")
print("weekday of the week:",week_day)


#f) Day of year

from datetime import datetime
current=datetime.now()
day_year=current.strftime("%j %Y")
print("Day of the year:",day_year)

#g) Day of the month

from datetime import datetime
current=datetime.now()
day_month=current.strftime("%j %m")
print("Day of the month:",day_month)

#h) Day of week

from datetime import datetime
current=datetime.now()
day_week=current.strftime("%j %w")
print("Day of week:",day_week)
