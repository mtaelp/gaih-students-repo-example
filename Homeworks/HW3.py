def prime_first(number):
    if number<500:
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                print(number)



def prime_second(number):
    if number>=500:
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                print(number)



for i in range(1001):
    prime_first(i)
    prime_second(i)
