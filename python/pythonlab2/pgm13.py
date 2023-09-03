#Write a Python program to generate all sublists of a list

def sublist(l):
    sublist([])
    for i in range(len(l)+1):
        for j in range (i+1,len(l)+ 1):
            sli=l(i:j)
            sublist.append(sli)
            return sublist
        l=list
        n=int(input("Enter the size of thge list:"))
        print("Enter the elements of the list:")                                                               
        for i in range (int(n)):
            e= int(input())
            l.append(e)
            print("Enter list is :{}".format(l))
            print("possible sublists are:".sublist(1))


