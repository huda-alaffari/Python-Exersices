# calculate sum of digits as integer ex: 1723
#1723%10 >>>> 3
#172%10 >>>2
#17%10 >>>7


n=int(input("->"))
sum_=0
while(n !=0):
    sum_+=n%10
    n=n//10
print(sum_)    