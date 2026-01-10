l = [-42, 13, -7, 29, 0, -18, 44, -31, 5, 22, -49, 11, -3, 37, -25, 8, -14, 19, -36, 4]
i= 0
m=[]
n=[]
odd=[]
even=[]
required=[]
required1=[]
required2=[]

for x in l:
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)
print(f"even numbers are,{even} and are {len(even)} in total \nodd numbers are,{odd} and are {len(odd)} in total")


while i<len(l):

    if l[i]<0:
        m.append(l[i])
    else:
        n.append(l[i])
    i +=1
print("the negative class is", m, "total numbers:", len(m))
print("the positive class is", n, "total numbers:", len(n))

for x in l:
    if x%15 ==0:
        required.append(x)
    elif x%3 ==0:
        required1.append(x)
    elif x%5==0:
        required2.append(x)

print(f"numbers divisible by 3 and 5 are,{required}")
print(f"numbers divisible by 3 are,{required1}")
print(f"numbers divisible by 5 are,{required2}")  


   



    
 
    







