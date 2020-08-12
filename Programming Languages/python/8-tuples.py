### TUPLES : immutable arrays/lists (meaning: you can't change them once defined)


lucky_numbers = (4, 8, "fifteen", 16, 23, 42.0)
#       indexes  0  1       2      3   4   5


# lucky_numbers[0] = 90           # ERROR, because you can't change TUPLES once defined
print(lucky_numbers[0])
print(lucky_numbers[1])
print(lucky_numbers[-1])          # Counting from backwards, returns  42.0
print(lucky_numbers[2:])          # grabs everything after index position 2,
print(lucky_numbers[2:4])         # grabs values from index position 2 till 4
print(len(lucky_numbers))         # returns Length of the TUPLE
