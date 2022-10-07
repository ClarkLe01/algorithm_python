import math

def caculate_deg(h,m):
    r = 6
    if(h < 12): return r*(h*5-m) if h*5>=m else r*(m - h*5)
    else:
        return r*((h-12)*5-m) if (h-12)*5>=m else r*(m - (h-12)*5)
h = int(input("h="))
m = int(input("m="))
if 0<=h<24 and 0<=m<=59:
    print(caculate_deg(0,0))
    print(caculate_deg(13,5))
    print(caculate_deg(15,10))
else:
    print("Nhap dung so")