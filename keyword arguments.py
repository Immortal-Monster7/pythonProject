def storyline(name = "jay", action="kicks", item="ass"): #these are the keyword arguments to take values and print multiple things
    print(name, action, item)

storyline() # this call will print default values as we have not given any input
storyline(item = "donkey") #doing this will change only the item argument and the other 2 args will hold their default value
storyline(item = 'dogs', action= "hates") #doing this will change 2 args and the other 1 arg(name) will hold default values only, this is order independent




