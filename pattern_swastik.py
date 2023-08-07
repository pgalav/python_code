#swastika
n=11
for i in range(n):
    for j in range(n):
        if j==0 and i < 5 \
                or j==10 and i >5 \
                or i==0 and j>5 \
                or i==10 and j<5 \
                or i==5 or j==5 \
                or i==2 and j==2 or i==2 and j==8 \
                or i==8 and j==2 or i==8 and j==8:
            print("#  ", end="")
        else:
            print("   ", end="")

    print("\r")