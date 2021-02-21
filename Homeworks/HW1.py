import random

a = [[], [], []]
while 1:
    b = random.randint(0, 99999)
    if b > 1:
        for i in range(2, b):
            if (b % i) == 0:
                print(b, "is not a prime number")
                break
        else:
            print(b, "is a prime number")
            if len(a[0]) < 3:
                a[0].append(b)
            elif len(a[1]) < 3:
                a[1].append(b)
            elif len(a[2]) < 3:
                a[2].append(b)
            else:
                break



    else:
        print(b, "is not a prime number")
for i in a:
    print(i)
