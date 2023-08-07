
#prime
num=int(input("enter your number: "))
count=0
print(type(num))
for i in range (1,num+1):
    if num % i == 0 :
        count+=1

        
if count <= 2 or num==1:
    print(num ," is prime")
else:
    print(num ,"is not prime")