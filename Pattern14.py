"""
A Program To Print The Following Pattern.

A 
A B 
A B C 
A B C D 
A B C D E 

"""
#Program code to print above pattern

for x in range(65,70):
    for y in range(65,x+1):
        print(chr(y),end=" ")
    print()

"""
OUTPUT:

C:\python3.7\python.exe C:/Users/lenovo/PycharmProjects/1frog/Python_Pattern/Pattern14.py
A 
A B 
A B C 
A B C D 
A B C D E 

"""
