a={1,2,3,4,5,2,3,4}
print(set(a))
# a.add(6)
# print(a)
b={1,3,4,7,8,9,10}
c=a|b #to find union
print(c)
print(a.union(b)) #combines two sets
print(a.intersection(b)) #gives same elements from two sets
print(a.difference(b))   #find the difference,checks element of a are present in b or not if not
print(b.difference(a))