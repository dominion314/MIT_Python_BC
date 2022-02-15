Below are some short Python programs. For each program, answer the associated question.

Try to answer the questions without running the code. Check your answers, then run the code for the ones you get wrong.

This question is going to ask you what some simple loops print out. If you're asked what code like this prints:

    num = 5
    if num > 2:
        print(num)
        num -= 1
    print(num)

write what it prints out, separating what appears on a new line by a comma and a space. So the answer for the above code would be:

    5, 4

Note: What does +=, -=, *=, /= stand for?

    a += b is equivalent to a = a + b

    a -= b is equivalent to a = a - b

    a *= b is equivalent to a = a * b

    a /= b is equivalent to a = a / b

1.
    num = 0
    while num <= 5:
        print(num)
        num += 1

    print("Outside of loop")
    print(num)

Answer:

    0,1,2,3,4,5, 'Outside of loop', 6

2.
    numberOfLoops = 0
    numberOfApples = 2
    while numberOfLoops < 10:
        numberOfApples *= 2
        numberOfApples += numberOfLoops
        numberOfLoops -= 1
    print("Number of apples: " + str(numberOfApples))

Answer:

    infinite loop

3.
    num = 10
    while num > 3:
        num -= 1
        print(num)

Answer:

    9,8,7,6,5,4,3

4.
    num = 10
    while True:
        if num < 7:
            print('Breaking out of loop')
            break
        print(num)
        num -= 1
    print('Outside of loop')

Answer:

    10,9,8,7, 'Breaking out of loop','Outside of loop'

5.
    num = 100
    while not False:
        if num < 0:
            break
    print('num is: ' + str(num))

Answer:

    infinite loop