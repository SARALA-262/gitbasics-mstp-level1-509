def addition(a,b):
    c=a+b
    print(c)
def prime(i):
    fact=0
    for j in range(1,i+1):
        if i%j==0:
            fact+=1
    if fact==2:
        return True
    else:
        return False