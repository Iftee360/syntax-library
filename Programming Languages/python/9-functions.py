### Functions

#no need to define datatype of data types of parameters, as python is dynamic language

# also you can give parameters a default value, in case no values are given or users didn't input any

def add_numbers(num1, num2=99) :
    return num1 + num2
    # whatever is after the func, will be inside the function

sum = add_numbers(4, 3)
print(sum)
sum = add_numbers(4)
print(sum)
