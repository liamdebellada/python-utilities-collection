totalDistance, total, totalLength, ppms, askFair = 0,0,0,[],True
while askFair:
    try:
        numberOfFairs = int(input("Enter number of fairs (2-8): "))
        askFair = (lambda x: False if numberOfFairs >= 2 and numberOfFairs <= 8 else True)(True)
        if askFair: print('Please enter a number from 2-8.')
    except ValueError:
        print('Invalid input, please enter a number from 2-8.')

class Fair():
    def __init__(self, length, totalCost, distance, ppm):
        self.length = length
        self.totalCost = totalCost
        self.distance = distance
        self.ppm = ppm

def createFair(f):
    print(f'\nEnter information for fair: {f+1}')
    setupFair = True
    while setupFair:
        try:
            length = float(input("Enter length: "))
            totalCost = float(input("Enter total cost: "))
            distance = float(input("Enter distance: "))
            ppm = totalCost / length
            return Fair(length, totalCost, distance, ppm)
        except ValueError:
            print('Invalid entry')

fairs = {f: createFair(f) for f in range(0, numberOfFairs)}
for fairNum, fair in fairs.items():
    totalDistance += fair.distance
    total += fair.totalCost
    totalLength += fair.length

highestVal = max([fairs[data] for data in fairs], key=lambda val: val.ppm)
avgDpf = totalDistance / len(fairs)
avgFc = total / len(fairs)
avgLd = totalLength / len(fairs)
print(f"\nFair statistics:\nTotal Distance: {totalDistance}\nTotal cost: {total}\nTotal Length: {totalLength}\n\nAverage distance per fare: {avgDpf}\nAverage fare cost: {avgFc}\nAverage length duration: {avgLd}\n\nMost lucrative Fair data: \nLength:{highestVal.length}\nTotal cost: {highestVal.totalCost}\nDistance: {highestVal.distance}")