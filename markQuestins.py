# M = ["a", "b", "a","a","c","b"]
# n=6
# i = 1
# counter = 0
# while (True):
#     if(i == 1):
#         message = input("Enter First Answer ")
#         if(message == M[0]):
#             counter+=1
#         else:
#             counter = 0
#                 
# print(counter)    
mark = 0
answer = "abaacbb"
Uanswre = input("Enter your answer: ")
for i in range(len(answer)):
    if(Uanswre[i] == answer[i]):
        mark+=1
    else:
        print(i+1, end=" ")
print()        
print(mark, "out of", len(answer))        
    