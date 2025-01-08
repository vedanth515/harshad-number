
#  printing the harshad number

num=input("enter a number:--")
res=0
for i in range(0,len(num)):
    res=res+int(num[i])  
# print("sum of the numbers:--",res)
    if int(num)%res==0:
        print("Harshad number!")
    else:
        print("Not a Harshad number")



# replacing zeros to ones and ones to zeros

num=list(input("enter a number:-"))
""
for i in range(0,len(num)):
    if num[i]=="0":
        num[i]="1"
    elif num[i]=="1":
        num[i]==0
print("".join(num))