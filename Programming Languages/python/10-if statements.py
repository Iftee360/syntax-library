### If Statements


is_student = False
is_smart = False


''' For C Programmers :
&& == and,      || == or,     ! == not,
else if == elif '''


if is_student and is_smart:
	print("You are a student")
elif is_student and not(is_smart):
	print("You are not a smart student")
else:
	print("You are not a student and not smart")



# >, <, >=, <=, !=, ==

if 1 > 3:
	print("1st number omparison was true")
if 1 >= 3:
	print("2nd number omparison was true")
if 1 != 3:
	print("3rd number omparison was true")


#You can also Compare Strings
if "dog" == "cat":
   print("string omparison was true")
