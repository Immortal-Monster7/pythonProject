def health_rating(age, apples_eaten, cigs_smoked):
    rating = (100-age) + (apples_eaten * 3.0) - (cigs_smoked * 5)
    print(rating)

jays_data = [21,5,10]
health_rating(*jays_data) #this asterisk before the dataset will extract all the arguments in it and use it in the function
#the other way of doing it is long , look below
health_rating(jays_data[0], jays_data[1], jays_data[2])



