
	
#ASSIGNMENT 1

	
port1 = {21:"FTP",22:"SSH",23:"telnet",80:"http"}
port2 = {}
port2=([(values,keys) for keys,values in port1.items()])
print ("Original dictionary is : ",port1) 

print ("Dictionary after swapping is :  ",port2) 
  

#ASSIGNMENT 2

list1=[(1,2),(3,4),(5,6),(4,5)]
list2=[]
def add(a,b):
	n=a+b 
	return n
  
for i in range(len(list1)): 
	(a,b)=list1[i]
	list2.append(add(a,b))
print(list2)


#ASSIGNMENT3

list1=[(1,2,3),[1,2],['a','hit','less']]
list2=[]
for i in list1: 
	for j in i:
		list2.append(j)
print(list2)