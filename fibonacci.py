#fibonacci
num=int(input("enter your number :"))
i=0
j=""
first_value=0
second_value=1
for r in range (num):
        if i<=1:
            value=i
        else:
            value=first_value+second_value
            first_value=second_value
            second_value=value
        print(value)
        val=str(value)
        j=j+val
        i+=1
lis=list(j)
for k in range(0, len(lis)):
    lis[k] = int(lis[k])
print("list of fibonacci series :" + str(lis))