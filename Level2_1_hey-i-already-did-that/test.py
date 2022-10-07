import math
from random import randint

# Lấy ngẫu nhiên số có độ dài n
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def solution_testcase(n,b):

    def convert_DecNumber_toBase(n,b):

        if (n < 0) or (b<2) or (b>16):
            return
            
        if b == 10: return str(n)

        sb = ""
        m = 0
        remainder = n

        while remainder > 0:
            if b>10:
                m = remainder%b
                if m >= 10:
                    sb = sb+str(chr(55+m))
                else:
                    sb = sb+str(m)
            else:
                sb = sb + str(remainder%b)
            remainder = int(remainder/b)
        return "".join(reversed(sb))

    def convert_BaseNumber_toDec(n,b):
        if b == 10: return "".join(n)
        dec = 0
        for i in range(len(n)):
            dec += int(n[i])*math.pow(b,len(n)-1-i)
        return int(dec)

    temp_n = n
    k = len(temp_n)
    arr_bag = [temp_n]
    result = 0
    while True:
        x = sorted([int(i) for i in temp_n],reverse=True)
        x = [str(i) for i in x]
        y = x[::-1]
        x = convert_BaseNumber_toDec(x,b)
        y = convert_BaseNumber_toDec(y,b)
        z = convert_DecNumber_toBase(int(x)-int(y),b)
        temp_n = z

        while len(temp_n) < k:
            temp_n = '0'+temp_n
        # print(temp_n)
        if temp_n in arr_bag:
            result = len(arr_bag[arr_bag.index(temp_n):])
            # print(temp_n)
            break
        else:
            arr_bag.append(temp_n)
        

    return result


class Solution:

    def __init__(self, num, base):
        self.num = num
        self.base = base
        self.accuracy = 10

    def ternary(self, n):
        if n == 0:
            return '0'
        nums = []
        while n:
            n, r = divmod(n, self.base)
            nums.append(str(r))
        return ''.join(reversed(nums))

    def add_full_len(self, n):
        len_n = len(n)
        sub = abs(len_n-len(self.num))
        if sub < 0:
            return n + '0'*sub
        return n

    def gen_x_y(self, n):
        list_str = [i for i in n]
        list_str.sort()
        return int(''.join(list_str), self.base), int(''.join(list_str[::-1]), self.base)

    def find(self):
        time = 0
        values_list = set()
        values_circle = set()
        start_circle = 0
        n = self.num
        
        while True:
            x, y = self.gen_x_y(n)
            z = y-x
            z = self.ternary(z)
            values_list.add(z)
            time += 1
            if time > len(values_list):
                time = len(values_list)
                values_circle.add(z)
                start_circle += 1
                if start_circle > len(values_circle) + self.accuracy:
                    return len(values_circle)
            else:
                values_circle = set()
                start_circle = 0
            n = self.add_full_len(z)


for i in range(2,10):
    n = random_with_N_digits(i)
    print("===============================",n,"===============================")
    print("Test: ",int(solution_testcase(str(n),10)))
    print("Solve: ", int(Solution(str(n), 10).find()))


# diff result
# n = 72 | b = 10
# n = 64 | b = 10
# n = 67 | b = 10
# n = 80 | b = 10
