import math

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

