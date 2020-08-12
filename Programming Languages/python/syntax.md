# Python Syntax
(More to be added)
[ Note: I just made a markdown version of the official blog post made by the,
[DATAFLAIR TEAM](https://data-flair.training/blogs/author/dfteam4/) · DECEMBER 10, 2019 ]

## What is Python Syntax?

The term syntax is referred to a set of rules and principles that describes the structure of a language.
The Python syntax defines all the set of rules that are used to create sentences in Python programming.
**For example –** we have to learn grammar when we want to learn the English language.
In the same way, you will need to learn and understand the Python syntax in order to learn the Python language.

### Example of Python Syntax

Python is a popular language because of its elegant syntax structure.
Let’s take a quick look at a simple Python program and you will get an idea of how programming in Python looks like.

    1. #Simple Python Program to see if a user is eligible to vote or not.
    2.
    3. \#getting user’s name
    4. **print**("Enter your name:")
    5. name = **input**()
    6.
    7. \# getting user’s age
    8. **print**("Enter your age:")
    9. age = **int**(**input**())
    10.
    11. \# condition to check if user is eligible or not
    12. **if**( age >= 18 ):
    13. ​    **print**( name, ' is eligible to vote.')
    14. else:
    15. ​    **print**( name, ' is not eligible to vote.')


**Output:**

    Enter your name:
    Harsh
    Enter your age:
    19
    Harsh is eligible to vote.

*Now! Let us see various structures in Python syntax that are used while doing programming in Python.*

## Types of Syntax Structures in Python[![Types of syntax in Python](https://d2h0cx97tjks2p.cloudfront.net/blogs/wp-content/uploads/sites/2/2019/12/Python-syntax.jpg)](https://d2h0cx97tjks2p.cloudfront.net/blogs/wp-content/uploads/sites/2/2019/12/Python-syntax.jpg)

### 1. Python Line Structure

A Python program comprises logical lines. A **NEWLINE** token follows each of those. The interpreter ignores blank lines.

The following line causes an error.

    1. **print**("Hi
    2. How are you?")

**Output:**

    SyntaxError: EOL while scanning string literal

### 2. Python Multiline Statements

This one is an important Python syntax. We saw that Python does not mandate semicolons. A new line means a new statement. But sometimes, you may want to split a statement over two or more lines. It may be to aid readability. You can do so in the following ways.

#### 2.1. Use a backward slash

    1. **print**("Hi\
    2. how are you?")

**Output:**

    Hihow are you?

You can also use it to distribute a statement without a string across lines.

    1. a\
    2. =\
    3. 10
    4. **print**(a)

**Output:**

10

#### 2.2. Put the String in Triple Quotes

    1. **print**("""Hi
    2. ​       how are you?""")

**Output:**

Hi
how are you?

However, you can’t use backslashes inside a docstring for statements that aren’t a string.

    1. """b\
    2. =\
    3. 10"""

**Output:**

‘b=10’


    1. **print**(b)

**Output:**

    Traceback (most recent call last):
    File “<pyshell#6>”, line 1, in <module>
    print(b)
    NameError: name ‘b’ is not defined

### 3. Python Comments

Python Syntax **‘Comments’** let you store tags at the right places in the code. You can use them to explain complex sections of code. The interpreter ignores comments. Declare a comment using an octothorpe (#).

    1. #This is a comment

Python does not support general multiline comments like **Java** or **C++**.

### 4. Python Docstrings

A docstring is a documentation string. As a comment, this Python [Syntax](https://en.wikipedia.org/wiki/Syntax) is used to explain code. But unlike comments, they are more specific. Also, they are retained at runtime. This way, the programmer can inspect them at runtime. Delimit a docstring using three double-quotes. You may put it as a function’s first line to describe it.

    1. def **func**():
    2.   """
    3. ​    This function prints out a greeting
    4.   """
    5.   **print**("Hi")
    6. **func**()

**Output:**

  Hi

*Any queries yet in Python Syntax Tutorial? If yes, mention in the comment section. DataFlair’s team is here to help you.*

### 5. Python Indentation

Since Python doesn’t use curly braces to delimit blocks of code, this Python Syntax is mandatory. You can indent code under a function, loop, or class.

    1. if 2>1:
    2. ​      **print**("2 is the bigger person");
    3. ​      **print**("But 1 is worthy too");

**Output:**

  2 is the bigger person
  But 1 is worthy too


You can indent using a number of tabs or spaces, or a combination of those. But remember, indent statements under one block of code with the same amount of tabs and spaces.

    1. if 2>1:
    2. ​     **print**("2 is the bigger person");
    3.    **print**("But 1 is worthy too");

**Output:**

  SyntaxError: unindent does not match any outer indentation level


### 6. Python Multiple Statements in One Line

You can also fit in more than one statement on one line. Do this by separating them with a semicolon. But you’d only want to do so if it supplements readability.

    1. a=7;**print**(a);

**Output:**

  7

### 7. Python Quotations

Python supports the single quote and the double quote for string literals. But if you begin a string with a single quote, you must end it with a single quote. The same goes for double-quotes.

The following string is delimited by single quotes.

    1. **print**('We need a chaperone');

**Output:**

  We need a chaperone


This string is delimited by double-quotes.

1. **print**("We need a 'chaperone'");

**Output:**

We need a ‘chaperone’

Notice how we used single quotes around the word chaperone in the string? If we used double quotes everywhere, the string would terminate prematurely.

    1. **print**("We need a "chaperone"");

**Output:**

  SyntaxError: invalid syntax

### 8. Python Blank Lines

If you leave a line with just whitespace, the interpreter will ignore it.

### 9. Python Identifiers

An identifier is a name of a program element, and it is **user-defined**. This Python Syntax uniquely identifies the element. There are some rules to follow while choosing an identifier:

1. An identifier may only begin with A-Z, a-z, or an underscore(_).
2. This may be followed by letters, digits, and underscores- zero or more.
3. Python is case-sensitive. Name and name are two different identifiers.
4. A reserved keyword may not be used as an identifier. The following is a list of keywords.

| and      | def    | False   | import   | not    | True  |
| -------- | ------ | ------- | -------- | ------ | ----- |
| as       | del    | finally | in       | or     | try   |
| assert   | elif   | for     | is       | pass   | while |
| break    | else   | from    | lambda   | print  | with  |
| class    | except | global  | None     | raise  | yield |
| continue | exec   | if      | nonlocal | return |       |

Apart from these rules, there are a few naming conventions that you should follow while using this Python syntax:

1. Use uppercase initials for class names, lowercase for all others.
2. Name a private identifier with a leading underscore ( _username)
3. Name a strongly private identifier with two leading underscores ( __password)
4. Special identifiers by Python end with two leading underscores.

### 10. Python Variables

In Python, you don’t define the type of the variable. It is assumed on the basis of the value it holds.

    1. x=10
    2. **print**(x)

**Output:**

  10


    1. x='Hello'
    2. **print**(x)

**Output:**

  Hello

Here, we declared a variable x and assigned it a value of 10. Then we printed its value. Next, we assigned it the value ‘Hello’ and printed it out. So, we see, a variable can hold any type of value at a later instant. Hence, Python is a **dynamically-typed language**.

### 11. Python String Formatters

Now let us see the different types of String formatters in Python:

***Checkout DataFlair’s [Python Strings](https://data-flair.training/blogs/python-string/) article with examples.***

#### 11.1. % Operator

You can use the % operator to format a string to contain text as well as values of identifiers. Use %s where you want a value to appear. After the string, put a % operator and mention the identifiers in parameters.

    1. x=10;  printer="HP"
    2. **print**("I just printed %s pages to the printer %s" % (x, printer))

**Output:**

  I just printed 10 pages to the printer HP

#### 11.2. Format Method

The format method allows you to format a string in a similar way. At the places, you want to put values, put 0,1,2,.. in curly braces. Call the format method on the string and mention the identifiers in the parameters.

    1. **print**("I just printed {0} pages to the printer {1}".**format**(x, printer))

**Output:**

  I just printed 10 pages to the printer HP

You can also use the method to print out identifiers that match certain values.

    1. **print**("I  just printed {x} pages to the printer {printer}".**format**(x=7, printer='HP'))

**Output:**

  I just printed 7 pages to the printer HP

#### 11.3. f-strings

If you use an f-string, you just need to mention the identifiers in curly braces. Also, write ‘f’ right before the string, but outside the quotes used.

    1. **print**(f"I just printed {x} pages to the printer {printer}")

**Output:**

  I just printed 10 pages to the printer HP



So, this was all about the Python Syntax tutorial. I hope you liked the explanation.

## Summary

In this Python Syntax tutorial, we learned about the basic Python syntax. We learned about its
 * line structure,
 *  multiline statements,
 *  comments and docstrings,
 *  indentation, and quotations.
 *  blank lines,
 *  identifiers,
 *  variables,
 *  multiple statements in one line, and
 *  string formatters.

***Time to get yourself acquainted with the next DataFlair’s article, [Python comments, indentations & statements](https://data-flair.training/blogs/python-comment/).***

If you find DataFlair’s Python Syntax article helpful, do share it with your friends.

Happy Learning😃
