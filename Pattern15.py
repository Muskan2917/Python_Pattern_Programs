"""
A Program To Print The Following Pattern.

* * * * * 
* * * * 
* * * 
* * 
* 

"""
#Program code to print above pattern

for x in range(1,6):
    for y in range(6,x,-1):
        print("*",end=" ")
    print()
    
"""
OUTPUT:

C:\python3.7\python.exe C:/Users/lenovo/PycharmProjects/1frog/Python_Pattern/Pattern15.py
* * * * * 
* * * * 
* * * 
* * 
* 

"""
