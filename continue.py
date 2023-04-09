takenNos = [1,2,3,4,15]

print("here are the available numbers")

for n in range(1,20):
    if n in takenNos:
        continue
    print(n)


#continue will take you to the start of the loop if the above condition is met and will ignore the code below "continue"
#if the above condition is not met then it will follow the code written below "continue"
