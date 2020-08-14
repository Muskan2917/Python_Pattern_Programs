"""
A Program To Print The Following Pattern.

1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5 

"""
#Program code to print above pattern

for x in range(1,6):
    for y in range(5,x-1,-1):
        print(x,end=" ")
    print()
    
"""
OUTPUT:

C:\python3.7\python.exe C:/Users/lenovo/PycharmProjects/1frog/Python_Pattern/Pattern16.py
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5 

"""
