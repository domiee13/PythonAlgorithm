isFinal = False


def init(n):
    arr = []
    for i in range(1, n + 1):
        arr.append(i)
    return arr


def display(arr):
    res = ""
    for i in arr:
        res += str(i)
    print(res)


def gen(arr):
    global isFinal
    l = len(arr)
    j = l - 2
    while (arr[j] > arr[j + 1]):
        j -= 1
    print(j)
    print(arr[j])
    if (j >= 0):
        k = len(arr) - 1
        print(j, k)
        while (arr[j] > arr[k]):
            k -= 1
        # print('arr[j] = ', arr[j])
        # print('arr[k] = ', arr[k])
        arr[j], arr[k] = arr[k], arr[j]
        # print('arr[j] = ', arr[j])
        # print('arr[k] = ', arr[k])
        print(arr[:j+1],arr[j+1:][::-1])
        arr = arr[:j + 1] + arr[j + 1:][::-1]
    else:
        isFinal = True


n= int(input())
arr = init(n)
while(not isFinal):
    gen(arr)
