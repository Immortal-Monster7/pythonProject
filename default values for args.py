def get_gender(sex = 'unknown'): #we have assigned the default value of the variable sex as 'Unknown'
    if sex == 'm':
        sex = "Male"
    elif sex == 'f':
        sex = "Female"
    print(sex)

get_gender() # as the parenthesis is empty, the function will print out the default value i.e 'Unknown'
get_gender('m')




