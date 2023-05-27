#factorial with recursion
def fact(x):
    if x==1 or x==0:
        return 1
    return x*fact(x-1)
print(fact(6))


#factorial with while loop
def fact(x):
    num=x
    if x==0:
        return 1
    while x>1:
        num=num*(x-1)
        x=x-1
    return num
print(fact(6))


#factorial with for loop

def fact(x): 
    num = 1
    for i in range(1, x + 1):
        num = num * i
    return num
print(fact(6))