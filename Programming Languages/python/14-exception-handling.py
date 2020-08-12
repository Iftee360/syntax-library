### Exception Handling

userInp = int(input("Enter Num"))

# try:
#     answer = 10 / userInp
# except:
#     print("Error")

try:
    answer = 10 / userInp
except ZeroDivisionError as e:
    print(e)
except ValueError as v:
    print(v)
except:
    print("Sorry, some Error Occured😓")
