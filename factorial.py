#Factorial of a Number
def fact(x):
    if x==0:
        return 1
    else:
        return x*(fact(x-1))
num=int(input("enter your number :"))
print("factorial is:"+str(fact(num)))