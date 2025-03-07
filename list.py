a=[10,20,30]
print(a)
#append=>adds a single element to a list
a.append(40)
print(a)
#extend()=>adds a one or more elements to a list
a.extend([50,60,70])
print(a)
#insert()=>adds a element to a specified index
a.insert(2,"list")
print(a)
#pop()=>remove a element and indexing should be given to remove an element from list
a.pop(1)
print(a)
#remove()=>removes an element and we should give a value to be deleted
a.remove(40)
print(a)
#del()=>to remove
a.__delitem__(1)
print(a)
for x in a[1:4]:
    print(x,end=" ")

