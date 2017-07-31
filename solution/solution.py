def solved_binary_search(ls, num, low, high):
    if(low > high):
        return -1
    mid = int((low + high) / 2)
    if(ls[mid] == num):
        return mid
    elif(num > ls[mid]):
        return solved_binary_search(ls, num, mid + 1, high)
    elif(num < ls[mid]):
        return solved_binary_search(ls, num, low, mid - 1)