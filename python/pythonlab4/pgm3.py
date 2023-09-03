#Write a Python program to convert unix timestamp string to readable date

from datetime import datetime
timestamp=1591014926
datetime =datetime.fromtimestamp(timestamp)
print("Date_time_object:",datetime)
d=datetime.strftime("%m %d %Y,%H:%M:%S")
print("Date:",d)
