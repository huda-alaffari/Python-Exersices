num = int (input("Enter number from 1-100"))
sum_=0
for i in range(1,num):
        if(num % i == 0):
           sum_+=i
if(sum_ == num):           
    print("The intered is perfect")
else:
    print("The intered is not perfect")
        