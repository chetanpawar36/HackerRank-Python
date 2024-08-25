# """____Question: Python If-Else____"""


n = int(input("enter the number to analyze: "))     #-->input to analyze number


if n%2 != 0:     #-->Q1.If n is odd, print Weird
    print("Weird")
  

elif 2 <= n <= 5:     #-->Q2.If n is even and in the inclusive range of 2 to 5, print Not Weird
    print("Not Weird")


elif 6 <= n <= 20:     #-->Q3.If n is even and in the inclusive range of 6 to 20, print Weird
    print("Weird")


else:     #-->Q4.If n is even and greater than 20, print Not Weird
    print("Not Weird")
    
    