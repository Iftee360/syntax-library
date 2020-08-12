### L I S T S
## quite similar to ARRAYS in other languages, but all DATA TYPES can be stored in single List


lucky_numbers = [4, 8, "fifteen", 16, 23, 42.0]
#       indexes  0  1      2      3   4    5
#              int  int  string  int  int  float

lucky_numbers[0] = 90
print(lucky_numbers[0])                 # 4
print(lucky_numbers[1])                 # 8


print(lucky_numbers[-1])                # 42

#just like Strings, you can get subsection of the lists
print(lucky_numbers[2:])                # ['fifteen', 16, 23, 42.0]
print(lucky_numbers[2:4])               # ['fifteen', 16]

#you can also get length of an Array
print(len(lucky_numbers))


### N Dimensional Lists


numberGrid =    [   [ 1, 2 ]  ,  [ 3, 4 ]    ]         # 2D array/list
#indexes:         [0][0, 1]    [1][0, 1]

numberGrid[0][1] = 99

print(numberGrid[0][0])             # 1
print(numberGrid[0][1])             # 99




### L I S T     F U N C T I O N S


friends = []
friends.append("Oscar")             # append elements to the list
friends.append("Angela")
friends.insert(1, "Kevin")          # inset elements in a certain index position

# friends.remove("Kevin")           # remove certain elements from the list
print( friends )
print( friends.index("Oscar") )     # get the index value of an Array/List
print( friends.count("Angela") )    # returns how many times an element show up in a list
friends.sort()                      # Sorts a List (if strings = alphabetically, if num = serially)
print( friends )
friends.clear()
print( friends )
