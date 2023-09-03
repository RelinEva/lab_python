#Write a Python program to get days between two dates. Go to the editor 
#Exampe: days between 28/02/2000 and  28/02/2001

from datetime import date
t1=date(2001,2,28)
t2=date(2000,2,28)
t3=t1-t2
print(t3.days)
