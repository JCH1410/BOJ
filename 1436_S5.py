""" n = int(input())
nums = [0]
num = 666
while len(nums) <= (n + 1):
    if '666' in str(num):
        nums.append(num)
    num += 1
print(nums[n]) """

# 코드 읽기
def six_check(x):
    while True :
        if x%10==6:
            return True
            break
        x=x//10
        if x==0:
            break
    return False 


def triple6(x):
    i=10
    result=0
    i_return=0
    while True:
        x=x//10
        if x<100:
            break
        if x%1000 == 666:
            result=x*i
            i_return=i
        i*=10
    arr=[result,i_return]
    return arr


n=int(input())

default = 666
count=0
plus=0
while count!=n:
    result=default+plus*1000
    if six_check(plus)==True:
        arr=triple6(result)
        if arr[0]!=0:
            for i in range(arr[1]):
                i=i+arr[0]
                count+=1
                if count==n:
                    result=i
                    break
            if count==n:
                break
            plus+=1
            result=default+plus*1000
    plus+=1
    count+=1
print(result)