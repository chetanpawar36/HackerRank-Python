# """____Question: Square of Number____"""


#-->Calculate the squaring of each number
    
n = int(input("enter till which number to find (no_to_find - 1): "))

i = 0

for i in range (0,n):
    i = i*i
    print(i)
    
while i < n:
    print(i)
    i += 1