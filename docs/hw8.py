def iseven(n):
    if n%2 == 0:
        return True
    else:
        return False

def count_evens(lst):
    count=0
    for i in lst:
        if iseven(i):
            count+=1
    return count
lst = [1,2,3,4,5,6,7,8,9,10]
print(f"The number of evens are:{count_evens(lst)}")
