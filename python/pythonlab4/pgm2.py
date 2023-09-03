#Write a Python program to subtract five days from current date

from datetime import datetime,timedelta
current=datetime.now()-timedelta(5)
print("Subtract five days from current date:",current)