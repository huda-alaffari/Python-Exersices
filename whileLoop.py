####using for loop
# n = 5
# fact = 1
# for i in range(1,n+1):
#     if(i != n): # without if , will print 1 * 2 * 3 * 4 * 5 * , to remove last * use if
#         print (i , end = " * " )
#     else:
#         print(i)
#     fact *= i 
# print()
# print(fact)


n = 5
fact = 1
i = 1
while(True):   #while(i<=n)
    if(i != n): # without if , will print 1 * 2 * 3 * 4 * 5 * , to remove last * use if
        print (i , end = " * " )
    else:
        print(i)
    fact *= i
    i +=1 # change i value
    if( i== n+1):
        break # to use break we need to if
print()
print(fact)
    