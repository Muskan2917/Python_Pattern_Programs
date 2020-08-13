"""
A Program To Print The Following Pattern.

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

"""
#Program code to print above pattern

for x in range(1,6):
    for y in range(1,x+1):
        print(y,end=" ")
    print()
    
"""
OUTPUT:

C:\python3.7\python.exe C:/Users/lenovo/PycharmProjects/1frog/Python_Pattern/Pattern12.py
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

"""
