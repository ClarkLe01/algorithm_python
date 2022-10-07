import random


def create_rand_arr(n):
    arr = [random.randrange(0,10000) for i in range(n)]
    return arr

def fmax_in_arr(arr):
    return sorted(arr,reverse=True)[0]

n = int(input("Nhap n = :"))

arr = create_rand_arr(n)
print(arr)
print(fmax_in_arr(arr))