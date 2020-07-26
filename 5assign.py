"""
Sort in increasing order but all zeros should be at right hand side.
"""

list1 =[0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
list2=[]
list3=[]
for i in list1:
    if i== 0:
        list2.append((i))
    else:
        list3.append((i))
print(sorted(list3)+(list2))


"""
Merge two lists by using one loop.
"""

list1 = [10,20,40,60,70,80]
list2 = [5,15,25,35,45,60]
list3 = list1+list2
list4 = []
print(list3)
for i in range(0,len(list3)):
    list4.append(min(list3))
    list3.remove(min(list3))
print(list4)
    
    
