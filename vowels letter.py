v="aoeui"
counter = 0
message = input("Enter a text:")
for chr1 in message:
    if(chr1.lower() in v):
        counter+=1
print(counter)       