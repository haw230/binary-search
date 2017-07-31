def solved_binary_check(ls, num):
    if(ls): #check if we have an actual list
        mid = int(len(ls) / 2) #middle of list
        if(ls[mid] == num): #list at middle is number we're looking for
            return True #then it's there
        if(mid == 0): #only one element and that's not it
            return False #not there
        if(num > ls[mid]): #num is greater than middle
            return solved_binary_check(ls[mid + 1:], num) #right half
        if(num < ls[mid]): #num is less than middle
            return solved_binary_check(ls[:mid], num) #left half
    return False #empty list handed out...immediately False