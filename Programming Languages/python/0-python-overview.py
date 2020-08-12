# Python Overview

Python is a general purpose, dynamically typed and interpreted,
object oriented programming language that was created in the late 1980s by Guido van Rossum.

Python’s design philosophy revolves around readability. It’s meant to be easy to read and
easy to write. This is accomplished by using white-space to delineate code blocks
instead of the more traditional curly brackets and semi-colons.


### How Python Runs
Generally all python code is run using an interpreter.
The most popular and original interpreter is called CPython, because it’s implemented in the c programming language.
Several other interpreters exist however, many of which are implemented in languages other than C like Java and C#.

The most common Python interpreter CPython, uses an automatic garbage collector to manage memory.
And Python is widely known for having a non-traditional, minimalist syntax
which is largely based on white space, and designed to be clean and readable.


### Python Versions

When first getting into python it can be a bit confusing because unlike many
other programming languages Python has two major, non-compatible versions that are currently widely used.

Python version 2.7.3, released in 2012, is the last iteration of version 2 that was released.
 This version is for the most part, backwards compatible with all previous versions.

In 2008, the Founder, Guido van Rossum decided to clean up the Python codebase
and overhaul a lot of the things in Python 2 that he didn’t like, thus creating Python 3.

Python 3 was adopted slowly at first, mainly because it is not backwards compatible with Python 2,
and there was a huge eco-system of package libraries written for Python 2 which now would not work in python 3.

But now-a-day’s the Python 3 ecosystem has for the most part caught up,
making Python 3 the obvious choice for new developers looking to learn the language.

 Python 3 is also the version that will be taught in this tutorial.


### Choosing an IDE

Many developers choose to write Python using a specialized integrated development environment.
Three of the most popular are Eclipse!, PyCharm and Netbeans.


### Exception Catching


try:
    answer = 10 / int(input("Enter Number: "))
except ZeroDivisionError as e:
    print(e)
except:
    print("Caught any exception")


### Classes and Objects


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def read_book(self):
         print("Reading", self.title, "by", self.author)

book1 = Book("Harry Potter", "JK Rowling");
# book1.title = "Half-Blood Prince"

print(book1.title)
book1.read_book()


### Getters and Setters


class Book:
    def __init__(self, title, author):
        self.title = title;
        self.author = author

    @property
    def title(self):
        print("getting title")
        return self._title

    @title.setter
    def title(self, value):
        print("setting title")
        self._title = value

    @title.deleter
    def title(self):
        del self._title


    def read_book(self):
         print("Reading", self.title, "by", self.author)

book1 = Book("Harry Potter", "JK Rowling");
# book1.title = "Half-Blood Prince"

print(book1.title)
book1.read_book()


### Inheritance


class Chef:

   def __init__(self, name, age):
       self.name = name
       self.age = age


   def make_chicken(self):
       print("The chef makes chicken")

   def make_salad(self):
       print("The chef makes salad")

   def make_special_dish(self):
       print("The chef makes bbq ribs")

class ItalianChef(Chef):

   def __init__(self, name, age, countryOfOrigin):
       self.countryOfOrigin = countryOfOrigin
       super().__init__(name, age)

   def make_pasta(self):
       print("The chef makes pasta")

   def make_special_dish(self):
       print("The chef makes chicken parm")


myChef = Chef("Gordon Ramsay", 50)
myChef.make_chicken()

myItalianChef = ItalianChef("Massimo Bottura", 55, "Italy")
myItalianChef.make_chicken()
print(myItalianChef.age);
