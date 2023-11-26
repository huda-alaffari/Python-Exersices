#encrypt
message ="HELLO"
x= 0
while(x<len(message)):
    new = ord(message[x])+3
    print(chr(new),end="")
    x+=1

#decrypt
message ="hello"
x= 0
while(x<len(message)):
    new = ord(message[x])-3
    print(chr(new),end="")
    x+=1