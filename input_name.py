for i in range(0, 10):
    string = input("what is your name?")
    count = 0
    newstring2 = ""
    s = '[@_!#$%^&*()<>?/\|}{~:]'
    for a in string:
        if (a.isnumeric()) == True :
            count += 1
            newstring2 += a
        elif a in s :
            count += 1
            newstring2 += a
    if newstring2 == "":
        print("your name is " +string)
        name=len(string)
        print(name)
        break
    else:
        print("text is invelid")
def msg():
    if newstring2 == "":
        print("thankyou! your name is submitted. ")
    else:
        print("sorry! try next time")
msg(