#Write a Python program to sum all the items in a list
def sum_list(item):
    sum=0
    for x in item:
        sum+=x
        return sum
    print(sum_list([2,3,-4]))