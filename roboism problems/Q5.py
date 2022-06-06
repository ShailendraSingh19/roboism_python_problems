print("Put the array of intergers seperated by spaces ")
var = input()
list_1=list(var.split(" "))
list_2 = [0]*99
for i in range(0, 100):
    list_1[i] = int(list_1[i])
for i in range(0,100):
    ele=(list_1[i]-1)
    (list_2[ele])=(list_2[ele])+1
#print(list1)
#print(list2)
for i in range(0,100):
    if list_2[i]==2:
        print("Repeated no. is: "+str(i+1))
        break


