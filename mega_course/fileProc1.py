myFile = open("fruits.txt")

content = myFile.read()

# the read method reads the file and moves the cursor from start to end
# therefore, if you call the exact same read method 2x in a row on same file
# it will not read the second time, b/c the cursor is already at the end

myFile.close() # close file once processing is finished. clear it from RAM.


print(content)
print(content)