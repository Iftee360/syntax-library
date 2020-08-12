###  S T R I N G S


greeting = "Hello"
#indexes:   01234

print( len(greeting) )   # returns LENGTH of the String

print( greeting[0] )     # returns 'H'
print( greeting[1] )     # returns 'e'

# Counting backwards with (-) sign
print( greeting[-1] )    # returns 'o'
print( greeting[-2] )    # returns 'l'



#String Find : we can see if a string contains another string


#if its there then it will print out the index position it starts with, like

print( greeting.find("llo") )    # will return 2

#if the string isn't there it'll return -1 or any other negative value
print( greeting.find("z") )



#SUBSTRING : we can grab a part of a string

print( greeting[2:] )       #grabs everything after index position 2  aka "llo"
print( greeting[2:4] )      #grabs values from index position 2 till 4 aka "ll"
