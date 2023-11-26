# calculate sum of digits as string ex: 1723

i = 0
n = input("->")
sum_ = 0
while(i<len(n)):
    # take the index i 
    sum_+=int(n[i])
    i+=1
print(sum_)    