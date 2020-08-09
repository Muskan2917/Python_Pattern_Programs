"""
A Program To Print The Following Star(*) Pattern Using While Loop

*       
* *     
* * *   
* * * * 
* * * * * 
* * * * * *
* * * * * * *
* * * * * * * *

"""
#Program code to print above pattern

num=int(input("Enter the number of rows: "))
row=0
while row<num:
    star=row+1
    while star>0:
        print("*",end=" ")
        star=star-1
    row=row+1
    print()   

"""
OUTPUT:
C:\python3.7\python.exe C:/Users/lenovo/PycharmProjects/1frog/Python_Pattern/Pattern2.py
Enter the number of rows: 8
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * * 
* * * * * * * * 

"""
