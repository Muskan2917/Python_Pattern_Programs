"""
A Program To Print The Following Star(*) Pattern Using For Loop

*       
* *     
* * *   
* * * * 

"""
#Program code to print above pattern
for i in range(1,5):
    for j in range(1,5):
        if j<=i:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print( )
    

"""
OUTPUT:
C:\python3.7\python.exe C:/Users/lenovo/PycharmProjects/1frog/Python_Pattern/Pattern1.py
*       
* *     
* * *   
* * * * 
"""
