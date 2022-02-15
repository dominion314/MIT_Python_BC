1.Convert the following into code that uses a while loop.

prints 2
prints 4
prints 6
prints 8
prints 10
prints Goodbye!

Answer:

    n = 2
    while n < 12:
        print(n)
        n = n+2
    print('Goodbye!')

2.Convert the following into code that uses a while loop.

prints Hello!
prints 10
prints 8
prints 6
prints 4
prints 2

Answer:

    num = 10
    print('Hello!')
    while num > 0:
        print(num)
        num -= 2

3.Write a while loop that sums the values 1 through end, inclusive. end is a variable that we define for you. So, for example, if we define end to be 6, your code should print out the result: 

21 which is 1 + 2 + 3 + 4 + 5 + 6.

Answer:

    total = 0
    current = 1
    while current <= end:
        total += current
        current += 1

    print(total)