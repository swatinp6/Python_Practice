c={"a":"hi","b":"hello"}
print(c)
#using dict(  keyword we can create a dictionary)
d=dict({"a":"hi","b":"hello"})
print(d)
#to update a value of key
d["b"]="xyz"
print(d)
#to add new key-value pair to dict
c[3]="bye"
print(c)
#to remove a specified key
c.pop("b")
print(c)
#to clear a dict
c.clear()
print(c)
#to access dict key-value
print(d["a"])
print(d.get("a"))
print(d.values())
print(d.keys())
print(d.items()) #get the tuple of d dict key-value pair
print(d.popitem()) #removes the last key
print(d)
print(d.get('c'))
print(d.setdefault('a')) #to get specified value