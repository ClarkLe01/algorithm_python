import math

def is_prime(x):
    if x < 2: return False
    elif x==2 or x==3:return True
    else:
        s = 0
        for i in range(1,x//2):
            if x%i==0: s+=1
        return True if s == 1 else False


def analysis_prime_n(n):
    count = 2
    tmp = []
    while n != 1:
        if n%count == 0:
            if is_prime(count):
                tmp.append(count)
                n=n/count
        else:
            count+=1
    tmp = [str(x) for x in tmp]
    return "x".join(tmp)

n = int(input("Nhap n = "))
if n>0:
    print(analysis_prime_n(n))
else:
    print("Nhap so nguyen duong")

        
