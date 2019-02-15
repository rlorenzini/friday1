#find missing number in sequence
a = [1,2,3,4,5,6,8,9]
def missing(a):
    n = len(a)
    total = (n+1)*(n+2)/2
    sum_of_a = sum(a)
    return total - sum_of_a
b = int(missing(a))
print(b)
