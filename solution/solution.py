def solved_binary_check(ls, num):
    mid = int(len(ls) / 2) #middle of list
    if(ls[mid] == num): #if middle is the number
        return True #then it's in the list
    if(mid <= 1): #if the list has one element and it's not num
        return False #it's not in the list
    if(ls[mid] > num): #if list at middle is greater than num
        return solved_binary_check(ls[mid + 1:], num) #search 
    if(ls[mid] < num):
        return solved_binary_check(ls[:mid - 1], num)