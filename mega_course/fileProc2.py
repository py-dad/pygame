with open('Files/fruits.txt', 'a+') as myFile: # add + after 'a' to both append and read
    myFile.seek(0) # move cursor back to top of file after read/write
    content = myFile.read()

print(content)
   

# with context manager closes file implicitly
# after it is done processing it
    



