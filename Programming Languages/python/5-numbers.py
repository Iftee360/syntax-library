
### NUMBERS


print( 2 * 3 )       # Basic Arithmetic: +, -, /, *
print( 2**3 )        # 2^3
print( 10 % 3 )      # Modulus Op. : returns remainder of 10/3  aka  1
print( 1 + 2 * 3 )   # order of operations
print(10 / 3.0)      # int's and doubles
# if int is divided by doubles, it returns a double
# But, if the result of int/int isn't a int then it'll return double unlike other languages

num = 10
num += 100           # +=, -=, /=, *=
print(num)           # 110

++num
print(num)

# MATH Module has useful math methods
import math
print( pow(2, 3) )              # 2^3 = 8
print( math.sqrt(144) )         # square root of 144
print( round(2.7) )             # rounds the num to the closest integar vaue
