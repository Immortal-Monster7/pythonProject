fw = open('textfile.txt', 'w') #the 'w' signifies that we are opening a file and writing into it
fw.write("Hello this is Jay\n") # .write is used to write into a file
fw.write("Goodbye")
fw.close() #the fw.close will close the file contents then and there and save memory
# fw  = file write for convenience

fr = open("textfile.txt", 'r') # 'r' is the notation to read a file and we've used fr for convenience as file-read
#now, we need a variable to store the contents of the textfile.txt so we will make a new variable
text = fr.read() #this will save the text in the file to a variable called text
print(text) #this will print the contents of the textfile.txt which were stored in the variable text onto the screen
fr.close() #this will close the file object and the text contents will be displayed onto the screen





