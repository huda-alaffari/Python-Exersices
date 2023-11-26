#######
##Printing all elements of a list in a single row, separated by spaces. 
# list_ = [1,4,5,8,9,7,6]
# for i in list_:
#     print(i, end= " ")

######
## Computing the product of all elements in a list.
# list_ = [1,4,5,8,9,7,6]
# for i in list_:
#     print(i*2, end= " ")


######
##Counting how many elements in a list are negative. 
# sum_=0
# list_ = [1,4,5,8,9,7,6,-1,-2]
# for i in list_:
#     if(i<0):
#       sum_ +=1
# print(sum_)


s= [1,4,5,8,9,7,6,-1,-2]
s.insert(1,9)
print(s)
print("append: ") ### add to end
s.append(9)
print(s)
print("pop: ") ## remove the end
s.pop()
s.pop()
print(s)
s.remove(-1)
print(s)
        