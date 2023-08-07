#palindrom 
x = input("enter something:")
y = ""
for i in x:
    y = i+y
if (x == y):
    print("Yes,this  is pelindrom")
else:
    print("No,this is not pelindrom")