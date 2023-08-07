num = input("enter your number :")
    count = 0
    cout = 0
    j=0
    k=0
    for i in num:
        k = int(i)
        cout += 1
    
    for l in num:
        m = int(l)
        j = m**cout
        count += j
    z=count
    print(z)
    
    y=int(num)
       
    if z == y:
        print("armstrong number")
    else:
        print("Number is not armstrong")