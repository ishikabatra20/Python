# Consider the following dictionary.
a={"name":"Aman",
"from":"india",
"marks":[92,98,96]}


# • a.items(): Returns a list of (key,value)tuples.
print(a.items())
# • a.keys(): Returns a list containing dictionary's keys.
print(a.keys())
# • a.update({"friends":}): Updates the dictionary with supplied key-value pairs.
print(a.get("name"))
# • a.get("name"): Returns the value of the specified keys (and value is returned)
a.update({"friends":"Yashvi"})
print(a)
a.update({"name": "Akhil"})
print(a)
print(a.get("marks"))

print(a.get("name")) #o/p:-Akhil
print(a["name"])     #o/p:-Akhil
# but
#this one is more recommended
print(a.get("name1"))    #o/p:- None
# print(a["name1"])       #o/p:- Error

a.clear()
print (a) #{}