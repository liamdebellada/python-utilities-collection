string = "ihavveduplicates"
#kinda long way of doing it:
# print("Duplicates in string are:", ",".join(list(filter(lambda l: l != None, [(lambda d, z: d if z > 1 else None)(d, v) for d, v in {x: [y for y in string].count(x) for x in string}.items()]))))

#shorter way of doing it :)
print([k for k,v in {x: [y for y in string].count(x) for x in string}.items() if v > 1])

print(string[::-1])