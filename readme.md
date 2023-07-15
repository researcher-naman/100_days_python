
# Python Course Notes

This complete notes guide of beginner to advance level of Python programming which I had made during Watch and learning this 100 days python course on CodeWithHarry Channel.


### Credits
- [@CodeWithHarry](https://github.com/CodeWithHarry)
### Written By
- [@self-Nasu](https://www.github.com/self-nasu)


## What is Python 🐍 ?

It is a programming language like other languages which gives us a way to communicate with computers with the help of ideas.

Ideas are the "commands" that people use to communicate with a computers 💻.





### First Program

- Just try this to run this program on your Python IDE

```python
my_name = "Naman Jain"
print("Hello and welcome" + my_name + "!!")
```


## comments in python

- We can write comments in python for making code eassy to understand by the programmer.

python does not interpret any comments and do not compile them and give output of this comments.

we use "#" in python for comments

```python
# This is a python comment
# Also this line not give any output
# print("naman jain")
```
- Also we can write multi line comments in python using single or double quotes like  

```python
'''
this is muliti line comment
hey my name is naman jain
what is your name buddy.
'''
```
```python
"""
this is muliti line comment
hey my name is naman jain
what is your name buddy.
"""
```
## 🫂 Modules in python

 A module is like a Code library which can be used to borrow the code written by somebody else which can use in our python program.

There are two type of Modules in python
- Built-In module (don't need to install)
- External module (needed to install using pip or conda)

### How to install any module in python ?

Ans: using "pip install" cmd

```python
pip install pandas
```
In this pandas in external module name

This cmd should be done before going into python console.


## Escape Sequence Character

Ther are some Escape Sequence Character in python which help use some Character in bwt string.

some of them are
- \n used for new line
- \\" used for double quote
- \\' used for single quote

examples of using them are

```python
print("hii \' My name is Naman Jain.")
print("hii this is a big statement \nSo i need to write this in new line")
print("hii it am \"naman jain\"")
```
- output
```output
hii ' My name is Naman Jain.
hii this is a big statement 
So i need to write this in new line
hii it am "naman jain"
```

### Some more attribute of print cmd

#### 1. separate

```python
print("Hey",6,7, sep="~")
```

This sep="any_syntax" means when this code will run python with add "any_syntax" bwt every element in print.

```output
Hey~6~7
```
#### 2. End with

```python
print("Hey",6,7, end="~")
```
This end="any_syntax" means this will add "any_syntax" to end of last element in print.

```output
Hey67~
```

## Variables and data Types

#### --> Some common data Typen in python are

- int
- float
- Boolean
- string

#### --> Other data types in python

- LIST (mutable)
mutable means it can be change by the program using command in code.

```python
list1 = [8,2.3,5,5.8]
```
Also we can create list inside list
```python
list2 = [8,2.3,[5.9,7]]
```

- TUPLE (immutable)
means that it cant be modified by any cmd once it has been made

```python
tuple1 = ("nasu","naman","sojumaru")
```
same we can make tuple inside tuple

- Mapped Data or dict

it a data type which has key and values pairs in it

```python
dict1 = {"name:naman","age:21","subject:python"}
```

## 💉operators in python

- \+  : Addition
- \-  : Subtraction
- \*  : Multiplication
- \/  : Division
- \// : Floor Division
- \%  : Modulus
- \** : Exponential
## 🧮 calculator using python

Today we will make simple calculator using what we learn up till now.

```python
print("PYTHON CALCULATOR\n")

a = 5 #change your value here
b = 5 #change your value here

print("\n Addition of", a ,"and", b,"is", a+b)
print("\n Subtraction of", a ,"with", b,"is", a-b)
print("\n Multiplication of", a ,"with", b,"is", a*b)
print("\n Division of", a ,"by", b,"is", a/b)
print("\n Floor Division of", a ,"by", b,"is", a//b)
print("\n Modulus of", a ,"by", b,"is", a%b)
print("\n Exponential of", a ,"to", b,"is", a**b)
```
#### Output
```output
PYTHON CALCULATOR


 Addition of 5 and 5 is 10

 Subtraction of 5 with 5 is 0

 Multiplication of 5 with 5 is 25

 Division of 5 by 5 is 1.0

 Floor Division of 5 by 5 is 1

 Modulus of 5 by 5 is 0

 Exponential of 5 to 5 is 3125
```