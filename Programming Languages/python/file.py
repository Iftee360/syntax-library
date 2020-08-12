### F I L E

#file_object = open("file_name", "mode")


## Write

file = open("tutorial.txt", "w+")   # w means write & '+' sign means both read & write
file.write("Hey, This is your first file in python\n")
print("Wrinting Successful!\n")
file.close()


## Append

file = open("tutorial.txt", "a+")  # a means append
file.write("This line was Appended\n")
print("Line Append Successful!\n")
file.close()


## READ


file = open("tutorial.txt", "r")

# read file in one step
# if file.mode() == "r":
      #use read() function to read the contents
#     contents = file.read()
#     print(contents)

# or, if your file is too big, use readlines() to read individual lines separately
file1 = file.readlines()
file.close()              #reading done, close file

for i in file1 :
    print(i)




"""
Mode      Description


'r' 	  This is the default mode. It Opens file for reading.

'w'    	  This Mode Opens file for writing.
          If file does not exist, it creates a new file.
          If file exists it truncates the file.

'x' 	  Creates a new file. If file already exists, the operation fails.

'a' 	  Open file in append mode. If file does not exist, it creates a new file.

't' 	  This is the default mode. It opens in text mode.

'b' 	  This opens in binary mode.

'+' 	  This will open a file for reading and writing (updating)

"""
