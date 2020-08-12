### Dictionaries : same as Assosiative Arrays/ Linked Lists / Hast tables(C, Ruby) / Map(JS) / std::map(C++)

## its like a List/Array but, lets you store key-value pairs


test_grades = {
     "key"  :  "value",  #Keys neeed to unique, but values can be anything
    "Andy"  :  "B+",     # DON't FORGET the COMMA (,) 😉
    "Baron" :  "C",
    "Ryan"  :  "A",
       3    :  95.2     #you can store diferent DATA TYPES in a single Dictionary
}

print( test_grades["Andy"] )
print( test_grades[3] )

# we can return a default value if the keys don't match, if matches returns the value
print( test_grades.get("Ryan", "No Student Found"))
print( test_grades.get("Doug", "No Student Found"))
