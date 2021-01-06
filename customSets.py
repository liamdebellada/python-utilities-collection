arr = [1,1,"d","d"] #this will not work for dicts, as they are unhashable and cannot be used as keys
print([x for x,v in {x: arr.count(x) for x in arr}.items()])