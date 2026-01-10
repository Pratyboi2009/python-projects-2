#wap to check whether number is prime
# n = int(input("enter a number :",))
# for i in range(2,n):
#     if n%i==0:
#         print("number is not a prime")
#         break
# else:
#     print("number is prime")

#wap to find all prime numbers between 1 to 100
l =[]
m = 1
def prime(n):
    if n<2:
        return 0
    elif n ==2:
        return 1
    elif n%2==0:
        return 0
    else:
        for i in range(3,int(n**0.5)+1,2):
             if n%i==0:
                 return 0
                 
        return 1
f= int(input("enter the upper limit till which you want to find prime numbers:"))       
while m<f+1:
    if prime(m)==1:
        l.append(m)
    m +=1
print(l)
                 


    
