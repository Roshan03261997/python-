list1 = [1,2,3,4,5,7,9]
list2 = ["a","b","c","d","e"]
dict1 = {}
len1 = min(len(list1),len(list2))
print(dict1.update( {list1[each] : list2[each] for each in range(len1)}))
print(dict1)
