# # Opening a file
# file = open("my_file.txt")

# # Reading a file
# contents = file.read()
# print(contents)

# # Closing a file
# file.close()

# Opening a file with a "with" keword
# So we do noit need to specify the closing state of the file
# The "with" keyword is going to managed the file directly, as son as we are done with the file, it will closes down
# In Python, the with keyword acts as a context manager that automatically handles resource allocation and cleanup. It guarantees that external resources (such as files, network sockets, or database connections) are closed or released properly, even if your code throws an error or an exception inside the block.
#By default the file is opened as a read-only mode
with open("my_file.txt") as file:
    # Reading a file
    contents = file.read() #It returns a string
    print(contents)

# Writing a file, we open it in writing mode
# It overwrites all content in the file
with open("my_file.txt", mode="w") as file:
    file.write("New text")

# appending to a file. We set the mode to a as append and the text will be appended.
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text")

# If the file does not exist,in writing mode the file will be created by default
# It overwrites all content in the file
with open("my_file_2.txt", mode="w") as file:
    file.write("New text")