def addition(*args): # the asterisk before args represents many/flexible no. of arguments inside a function
    total = 0
    for n in args:
        total += n
    print(total)

addition(1,2,3,76467665,345645,34,4,6745,6)
