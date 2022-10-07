def solution(i):

    def check_Prime(x):
        count = 0
        if(x<=1): return False
        else:
            for i in range(1,x//2+1):
                if x%i==0:
                    count+=1
        return True if count==1 else False

    long_string = "2"
    last_prime = 3

    while(len(long_string)<=i+5):
        if check_Prime(last_prime) == True:
            long_string+=str(last_prime)
        last_prime+=1
        
    return long_string[i:i+5]
    

    

    