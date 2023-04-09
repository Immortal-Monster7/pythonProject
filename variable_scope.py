'''jay = 69 # as this variable is created in open space outside all/both the functions, so both the functions have access to it

def alpha():
    print(jay)

def gamma():
    print(jay)

alpha()
gamma()
'''

def alpha():
    jay = 69
    print(jay)

def gamma():
    print(jay)

alpha()
gamma()
# now if we run this code it will result in error as variable jay was created inside the function alpha only so it is outside the variable scope of gamma





