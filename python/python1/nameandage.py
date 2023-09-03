"""Write a program that asks the user to enter their name and their age. 
Print out a message that greets them and that tells them the year that they will turn 100 years old."""


name=input("Enter your name")
age=input("Enter your age")
hundred=2023 + (100 - age)
print("Hi" ,name, "you will turn 100 years old in the year",hundred)
