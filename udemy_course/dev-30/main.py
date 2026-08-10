# FileNotFound
# with open ("a_file.txt") as file:
#   file.read()

# KeyError
# a_dictionary ={"key" :"value"}
# value = a_dictionary["non_existent_key"]

# Index Error
# fruit_list=["Apple", "Banana", "Pear"]
# fruit_list[3]

# TypeError
# text= "abc"
# print(text + 5)

# Catching exceptions
# try: -> Something that might cause an exception
# except: -> Do this if there was an exception
# else: -> Do this if there were no exceptions
# finally: -> Do this no matter what happens


try:
    file = open("a_file.txt")
    file.read()
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")


# Raising your own exceptions
height = float(input("Height: "))
weight = int(input("Weight: "))
bmi = weight / height**2

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")
