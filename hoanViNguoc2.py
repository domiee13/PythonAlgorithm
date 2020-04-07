# Chua toi uu duoc chuong trinh . . .
isFinal = False
arr = []


def init(n):
    for i in range(1, n + 1)[::-1]:
        arr.append(i)
    return arr


def display(a):
    res = ""
    for i in a:
        res += str(i)
    print(res, end=" ")


def gen():
    global isFinal
    global arr
    l = len(arr)
    j = l - 2
    while arr[j] < arr[j + 1]:
        j -= 1
    if j >= 0:
        k = l - 1
        while arr[j] < arr[k]:
            k -= 1
        arr[j], arr[k] = arr[k], arr[j]
        arr = arr[:j + 1] + arr[j + 1:][::-1]
    else:
        isFinal = True

n = int(input())
arr = init(n)
while not isFinal:
    display(arr)
    gen()