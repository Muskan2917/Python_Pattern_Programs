"""
A Program To Print The Following Pattern.

A 
B B 
C C C 
D D D D 
E E E E E 

"""
#Program code to print above pattern

for x in range(65,70):
    for y in range(65,x+1):
        print(chr(x),end=" ")
    print()
    
"""
OUTPUT:

C:\python3.7\python.exe C:/Users/lenovo/PycharmProjects/1frog/Python_Pattern/Pattern13.py
A 
B B 
C C C 
D D D D 
E E E E E 

"""
