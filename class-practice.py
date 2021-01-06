class setup():
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def getName(self):
        return self.name

    def getStatus(self):
        return self.status


bools = {
    "true" : True,
    "false" : False
}

for item in bools:
    print(item)

for key, value in bools.items():
    print(f'String representation: {key}, Boolean representation: {value}')

data = {}

def getValues(x):
    for key, value in x.items():
        return value

arrofdict = [{"test": 1}, {"test2": 2}]
print(arrofdict)
print([getValues(x) for x in arrofdict])

testlist = [1,2,4,3]

for count, i in enumerate(testlist):
    print(f'Counter value: {count}, Item at counter value index: {i}')

query = input("Enter search query for testlist: ")

try:
    print(list(filter(lambda x: x==int(query), testlist)))
except:
    print("invalid")

checking = True
while checking:
    name = input("Enter name: ")
    status = input("Enter status (true/false): ")

    try:
        data[name] = setup(name, bools[status])
    except:
        print("One or more fields are invalid")

    if len(data) == 3:
        checking = False

for x in data:
    print("Objects:", x)

getData = True
while getData:
    selection = input("Enter one of the objects name: ")
    try:
        res = data[selection]
        print(f'{res.name} -> {res.getStatus()}') 
    except:
        print("Object name not found")
    
