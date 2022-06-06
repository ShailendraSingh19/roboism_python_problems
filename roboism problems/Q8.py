


print("Enter the string:")
inp=input()
sum=0
for i in range(0,len(inp)):
    if inp[i]>='0' and inp[i]<='9':
        sum = sum + int(inp[i])

print(sum)
