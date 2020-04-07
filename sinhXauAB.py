count = int(input())


# Khoi tao
def init(n):
    arr = []
    for i in range(0, n):
        arr.append('A')
    return arr


# Sinh xau AB
def genNext(arr):
    l = len(arr)-1
    while (arr[l] == 'B'):
        arr[l] = 'A'
        l -= 1
    if (l >= 0):
        arr[l] = 'B'


def display(arr):
    res = ""
    for i in arr:
        res += str(i)
    print(res, end=" ")


# Check xem da la cau hinh cuoi chua
def isFinal(arr):
    for i in arr:
        if (i == 'A'):
            return False
    return True


for i in range(0, count):
    n = int(input())
    arr = init(n)
    display(arr)
    while (not isFinal(arr)):
        genNext(arr)
        display(arr)
    print()
    arr.clear()

