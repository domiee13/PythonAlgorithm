isFinal = False
res = []
arr = []  # Chi dung voi bien toan cuc ?


# Chua tim duoc cach fix voi bien cuc bo

def init(n):
    arr = []
    for i in range(1, n + 1):
        arr.append(i)
    return arr


def display(arr):
    res = ""
    for i in arr:
        res += str(i)
    print(res, end=" ")


def gen():
    global isFinal
    global arr
    l = len(arr)
    j = l - 2
    while arr[j] > arr[j + 1]:
        j -= 1
    if j >= 0:
        k = len(arr) - 1
        while arr[j] > arr[k]:
            k -= 1
        arr[j], arr[k] = arr[k], arr[j]
        arr = arr[:j + 1] + arr[j + 1:][::-1]
    else:
        isFinal = True

count = int(input())
for i in range(0,count):
    n = int(input())
    arr = init(n)
    while not isFinal:
        # display(arr)
        res.append(list(arr))  # Shallow copies
        # print(res)
        gen()
    for item in res[::-1]:
        display(item)
    print()
    arr.clear()
    res.clear()
    isFinal = False