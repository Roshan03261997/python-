# Creating FLAMES game.

name1 = input("Enter the name1").lower()
name2 = input("Enter the name2").lower()
name1 = name1.replace(" ","")
name2 = name2.replace(" ","")
for i in name1:
    for j in name2:
        if i==j:
            name1.replace(i,"",1)
            name2.replace(j,"",1)
            break
count = len(name1+name2)
print("The number of element is :",count)
if count>0 :
    list1 =["F","L","A","M","E","S"]
    while len(list1)>1:
        c = count%len(list1)
        idx = c-1
        if idx >= 0:
            left = list1[:idx]
            right = list1[idx+1:]
            list1 = right+left
        else:
            list11 = list1[:len(list1)-1]
    print(list1[0])

else:
    print(" enter an valid name")







