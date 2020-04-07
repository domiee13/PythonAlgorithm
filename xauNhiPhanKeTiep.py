n = int(input())

def genNext(inputStr):
    l = len(inputStr)
    arr = []
    for i in inputStr:
        arr.append(int(i))
    j = len(arr) - 1
    while (arr[j]==1 and j>=0):
        j = j - 1
    if (j<0):
        res = ('0'*l)
        return res
    arr[j] = 1
    for i in range(j+1, len(arr)):
        arr[i] = 0
    res = ""
    for i in arr:
        res += str(i)
    return res

for i in range(0,n):
    inputStr = input()
    print(genNext(inputStr))

