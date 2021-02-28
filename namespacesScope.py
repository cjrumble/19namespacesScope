# NAMESPACES LESSON
# While in Python, the namespace is a fundamental idea to structure and organize the code,
# especially more useful in large projects.However, it could be a bit difficult concept to grasp if you’re
# new to programming.Hence, we tried to make namespaces just a little easier to understand.

# Python Namespace and Scope
# Python Namespace, Scope, and Scope Resolution
# What are names in Python?
# Before getting on to namespaces, first, let’s understand what Python means by a name.
# A name in Python is just a way to access a variable like in any other languages.
# However, Python is more flexible when it comes to the variable declaration.
# You can declare a variable by just assigning a name to it.
# You can use names to reference values.
num = 5
str = 'Z'
seq = [0, 1, 1, 2, 3, 5]
# You can even assign a name to a function.
def function():
    print('It is a function.')
foo = function
foo()
# You can also assign a name and then reuse it.Check the below example; it is alright for a name to point to different values.
test = -1
print("type <test> :=", type(test))
test = "Pointing to a string now"
print("type <test> :=", type(test))
test = [0, 1, 1, 2, 3, 5, 8]
print("type <test> :=", type(test))
# Ouptut:
# type < test > := <class 'int'>
# type < test > := <class 'str'>
# type < test > := <class 'list'>

# The naming mechanism works inline with Python’s object system, i.e., everything in Python is an object.
# All the data types such as numbers, strings, functions, classes are all objects.And a name acts as a reference to get to the objects.
# What are namespaces in Python?
# A namespace is a simple system to control the names in a program.
# It ensures that names are unique and won’t lead to any conflict.
# Also, add to your knowledge that Python implements namespaces in the form of dictionaries.
# It maintains a name - to - object mapping where names act as keys and the objects as values.
# Multiple namespaces may have the same name but pointing to a different variable.

# Local Namespace
# This namespace covers the local names inside a function.
# Python creates this namespace for every function called in a program.It remains active until the function returns.

# Global Namespace
# This namespace covers the names from various imported modules used in a project.
# Python creates this namespace for every module included in your program.It’ll last until the program ends.

# Built - in Namespace
# This namespace covers the built - in functions and built - in exception names.
# Python creates it as the interpreter starts and keeps it until you exit.

# What is Scope in Python?
# Namespaces make our programs immune from name conflicts.
# However, it doesn’t give us a free ride to use a variable name anywhere we want.
# Python restricts names to be bound by specific rules known as a scope.
# The scope determines the parts of the program where you could use that name without any prefix.

# Python outlines different scopes for locals, function, modules, and built-ins.Check out from the below list.
# A  local scope, also known as the innermost scope, holds the list of all local names available in the current function.
# A scope for all the enclosing functions, it finds a name from the nearest enclosing scope and goes outwards.
# A module level scope, it takes care of all the global names from the current module.
# The outermost scope which manages the list of all the built - in names.It is the last place to search for a name that you cited in the program.

# Scope Resolution in Python – Examples
# Scope resolution for a given name begins from the inner-most function and then goes higher and higher until the program finds the related object.If the search ends without any outcome, then the program throws a NameError exception.
a_var = 10
print("begin()-> ", dir())

def foo():
    b_var = 11
    print("inside foo()-> ", dir())

foo()

print("end()-> ", dir())
# The output is as follows.
# begin()-> ['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a_var']
# inside
# foo()-> ['b_var']
# end()-> ['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a_var', 'foo']
# We used the dir() function. It lists all the names that are available in a Python program then.
# In the first print() statement, the dir() only displays the list of names inside the current scope.
# While in the second print(), it finds only one name, “b_var,” a local function variable.
# Calling dir() after defining the foo() pushes it to the list of names available in the global namespace.

# The list of names inside some nested functions. The code in this block continues from the previous block.
def outer_foo():
    outer_var = 3

    def inner_foo():
        inner_var = 5
        print(dir(), ' - names in inner_foo')

    outer_var = 7
    inner_foo()
    print(dir(), ' - names in outer_foo')

outer_foo()
# # Output:
# ['inner_var'] - names in inner_foo
# ['inner_foo', 'outer_var'] - names in outer_foo
# Defines two variables and a function inside the scope of outer_foo().
# Inside the inner_foo(), the dir() function only displays one name i.e. “inner_var”.
# It is alright as the “inner_var” is the only variable defined in there.
# If you reuse a global name inside a local namespace, then Python creates a new local variable with the same name.
a_var = 5
b_var = 7

def outer_foo():
    global a_var
    a_var = 3
    b_var = 9

    def inner_foo():
        global a_var
        a_var = 4
        b_var = 8
        print('a_var inside inner_foo :', a_var)
        print('b_var inside inner_foo :', b_var)

    inner_foo()
    print('a_var inside outer_foo :', a_var)
    print('b_var inside outer_foo :', b_var)


outer_foo()
print('a_var outside all functions :', a_var)
print('b_var outside all functions :', b_var)
# output
# a_var inside inner_foo: 4
# b_var inside inner_foo: 8
# a_var inside outer_foo: 4
# b_var inside outer_foo: 9
# a_var outside all functions: 4
# b_var outside all functions: 7

# We’ve declared a global variable as “a_var” inside both the outer_foo() and inner_foo() functions.
# However, we’ve assigned different values in the same global variable.
# And that’s the reason the value of “a_var” is same(i.e., 4) on all occasions.
# Whereas, each function is creating its own “b_var” variable inside the local scope.Andthe print() function is showing
# the values of this variable as per its local context.

# How to correctly import modules in Python?
# It is very likely that you would import some of the external modules in your program.
# So, we’ll discuss here some of the import strategies, and you can choose the best one.

# Import all  names from a module
# from < module name >
# import *
# It’ll import all the names from a module directly into your working namespace.
# Since it is an effortless way, so you might tempt to use this method.
# However, you may not be able to tell which odule imported a particular function.
print("namespace_1: ", dir())
from math import *
print("namespace_2: ", dir())
print(sqrt(144.2))
from cmath import *
print("namespace_3: ", dir())
print(sqrt(144.2))
# Output:
# namespace_1: ['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
# namespace_2: ['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos',
#               'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e',
#               'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd',
#               'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p',
#               'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
# 12.00833044182246
# namespace_3: ['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos',
#               'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e',
#               'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd',
#               'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p',
#               'log2', 'modf', 'nan', 'phase', 'pi', 'polar', 'pow', 'radians', 'rect', 'sin', 'sinh', 'sqrt', 'tan',
#               'tanh', 'trunc']
# (12.00833044182246 + 0j)
# Imported two distinct math modules, one after the other.
# There are some common names which both ofthese modules have.
# So, the second module will override the definitions of functions in the first.

# The first call to sqrt() returns a real number and the second one gives a complex number.
# And now, there is no way we can call the sqrt() function from the first math module.
# Even if we call the function using the module name, then Python will raise the NameError exception.
# So, the lesson learned here is that there are no shortcuts for quality code.

# Import specific names from a module
# from < module name > import < foo_1 >, < foo_2 >
# If you are sure of the names to be used from a module, then import them directly into your program.
# This method is slightly better but will not prevent you from polluting the namespace completely.
# It is because you can’t use any other name from the module.
# Here also, any function having the same name in your program will also override the same definition present in the module.
# The affected method will become dormant in such a case.
print("namespace_1: ", dir())
from math import sqrt, pow
print("namespace_2: ", dir())
print(sqrt(144.2))
# # Output
# namespace_1: ['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
# namespace_2: ['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'pow', 'sqrt']
# 12.00833044182246

# Import just the module using its name
# import < module name >
# It is the most reliable and suggested way of importing a module.
# However, it comes with a catch that you need to prefix the name of the module before using any name from it.
# But you can prevent the program from polluting the namespace and freely define functions with matching names in the module.
print("namespace_1: ", dir())
import math
print("namespace_2: ", dir())
print(math.sqrt(144.2))
# # Output
# namespace_1: ['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
# namespace_2: ['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'math']
# 12.00833044182246

# Quick wrap up – Python Namespace and Scope
# If you want to do serious programming, then it is vital for you to know how scopes and namespaces work in Python.
# With this knowledge, you can even develop a scalable package ecosystem to be used by a large group working on a massive project.