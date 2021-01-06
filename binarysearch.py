def binarySearch(elem, intArr):
    m, l, h = 0, 0, len(intArr) - 1
    while l <= h:
        m = (l + h) // 2
        if elem == intArr[m]: return m
        if elem > intArr[m]:
            l = m + 1
        elif elem < intArr[m]:
            h = m - 1
        else:
            return None
print(binarySearch(13, (1,3,4,5,13,20,25,40,42,44,53)))
