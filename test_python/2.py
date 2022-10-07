from asyncio.windows_events import NULL
import random

def create_rand_arr(n):
    arr = [random.randrange(0,10000) for i in range(n)]
    return arr

def smax_in_arr(arr):
    sorted_arr = sorted(arr,reverse=True)
    fmax = sorted_arr[0]
    smax = NULL
    for i in sorted_arr:
        if i!=fmax:
            smax = i
            break
    print(fmax)
    print(smax)
    return smax

n = int(input("Nhap n = "))

arr = create_rand_arr(n)
smax = smax_in_arr(arr)
print(arr)
print(smax)








