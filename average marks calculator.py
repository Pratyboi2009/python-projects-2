i= 1
l=[]
n = int(input("enter the number of students in class  :"))
while i<n+1:
    a= int(input(f"enter marks of roll no. {i}  :"))
    l.append(a)
    i +=1
d = max(l)
print(f"average marks of class is {sum(l)/len(l)}, \nhighest marks is {d} which is secured by roll no. {l.index(d)+1}")
