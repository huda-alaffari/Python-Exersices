s = [2,5,5,7,1]
x = list(s)  # x = s[:] >>> slice for start(2) and end(1) //// x = s.copy()
print(x)
x[4] = 5
print(x)
print(s)