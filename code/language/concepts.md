# Reserved words

False as continue else from in not return yield
None assert def except global is or try
True break del finally if lambda pass while
and class elif for import nonlocal raise 



# Arithmetic Operators 

- + addition
- − subtraction
- * multiplication
-  / true division
- // integer division --> 
- % the modulo operator



# Bitwise Operators

- ∼ bitwise complement (prefix unary operator)
- & bitwise and
- | bitwise or
- ˆ bitwise exclusive-or
- << shift bits left, filling in with zeros
- >> shift bits right, filling in with sign bitv


# Sequence Operators

- s[j] element at index j
- s[start:stop] slice including indices [start,stop)
- s[start:stop:step] slice including indices start, start + step,
- start + 2 step, . . . , up to but not equalling or stop
- s+t concatenation of sequences
- k s shorthand for s + s + s + ... (k times)
- val in s containment check
- val not in s non-containment check


# Operators for Sets and Dictionaries
- key in s containment check
- key not in s non-containment check


# Calling Syntax Description

- abs(x) Return the absolute value of a number.
- all(iterable) Return True if bool(e) is True for each element e.
- any(iterable) Return True if bool(e) is True for at least one element e.
- chr(integer) Return a one-character string with the given Unicode code point.
- divmod(x, y) Return (x // y, x % y) as tuple, if x and y are integers.
- hash(obj) Return an integer hash value for the object (see Chapter 10).
- id(obj) Return the unique integer serving as an “identity” for the object.
- input(prompt) Return a string from standard input; the prompt is optional.
- isinstance(obj, cls) Determine if obj is an instance of the class (or a subclass).
- iter(iterable) Return a new iterator object for the parameter (see Section 1.8).
- len(iterable) Return the number of elements in the given iteration.
- map(f, iter1, iter2, ...) Return an iterator yielding the result of function calls f(e1, e2, ...)
- for respective elements e1 ∈ iter1,e2 ∈ iter2,...
- max(iterable) Return the largest element of the given iteration.
- max(a, b, c, ...) Return the largest of the arguments.
- min(iterable) Return the smallest element of the given iteration.
- min(a, b, c, ...) Return the smallest of the arguments.
- next(iterator) Return the next element reported by the iterator (see Section 1.8).
- open(filename, mode) Open a file with the given name and access mode.
- ord(char) Return the Unicode code point of the given character.
- pow(x, y) Return the value xy (as an integer if x and y are integers);
- equivalent to x y.
- pow(x, y, z) Return the value (xy mod z) as an integer.
- print(obj1, obj2, ...) Print the arguments, with separating spaces and trailing newline.
- range(stop) Construct an iteration of values 0, 1,..., stop−1.
- range(start, stop) Construct an iteration of values start, start+1,..., stop−1.
- range(start, stop, step) Construct an iteration of values start, start+step, start+2 step,...
- reversed(sequence) Return an iteration of the sequence in reverse.
- round(x) Return the nearest int value (a tie is broken toward the even value).
- round(x, k) Return the value rounded to the nearest 10−k (return-type matches x).
- sorted(iterable) Return a list containing elements of the iterable in sorted order.
- sum(iterable) Return the sum of the elements in the iterable (must be numeric).
- type(obj) Return the class to which the instance obj belongs.


# Function files

Calling Syntax Description
- fp.read( ) Return the (remaining) contents of a readable file as a string.
- fp.read(k) Return the next k bytes of a readable file as a string.
- fp.readline( ) Return (remainder of) the current line of a readable file as a string.
- fp.readlines( ) Return all (remaining) lines of a readable file as a list of strings.
- for line in fp: Iterate all (remaining) lines of a readable file.
- fp.seek(k) Change the current position to be at the kth byte of the file.
- fp.tell( ) Return the current position, measured as byte-offset from the start.
- fp.write(string) Write given string at current position of the writable file.
- fp.writelines(seq)
- Write each of the strings of the given sequence at the current
- position of the writable file. This command does not insert
- any newlines, beyond those that are embedded in the strings.
- print(..., file=fp) Redirect output of print function to the file.


# Common Exception Types

- Exception --> A base class for most error types
- AttributeError Raised by syntax obj.foo, if obj has no member named foo
- EOFError Raised if “end of file” reached for console or file input
- IOError Raised upon failure of I/O operation (e.g., opening file)
- IndexError Raised if index to sequence is out of bounds
- KeyError Raised if nonexistent key requested for set or dictionary
- KeyboardInterrupt Raised if user types ctrl-C while program is executing
- NameError Raised if nonexistent identifier used
- StopIteration Raised by next(iterator) if no element; see Section 1.8
- TypeError Raised when wrong type of parameter is sent to a function
- ValueError Raised when parameter has invalid value (e.g., sqrt(−5))
- ZeroDivisionError Raised when any division operator used with 0 as divisor

```python
def sqrt(x):
    if not isinstance(x, (int, float)):
        raise TypeError( x must be numeric )
    elif x < 0:
        raise ValueError( x cannot be negative )
```
# A second philosophy, often embraced by Python programmers, is that “it is easier to ask for forgiveness than it is to get permission.”



# Iterators and Generators


# Iteration

- **An iterator** is an object that manages an iteration through a series of values. If
variable, i, identifies an iterator object, then each call to the built-in function,
next(i), produces a subsequent element from the underlying series, with a
StopIteration exception raised to indicate that there are no further elements.

- **An iterable** is an object, obj, that produces an iterator via the syntax iter(obj).

# Generators
Spanish:
    Los generadores son una forma de crar objetos iterables, ya que con la palabara reservada yield, este no almacena en RAM
    sino que retorna un valor sobre el objeto.
    
    Al final genera es un objeto iterable , y para obtener los valores de este objeto iterable se usa la palabra reservada next()


### Dictionary

The dictionary class supports methods **keys( )**, **values( )**, and **items( )**

# Comprehension Syntax

[ expression for value in iterable if condition ]

- [ k k for k in range(1, n+1) ] list comprehension
- { k k for k in range(1, n+1) } set comprehension
- ( k k for k in range(1, n+1) ) generator comprehension
- { k:k k for k in range(1, n+1) } dictionary comprehension

Loops

for x, y in [ (7, 2), (5, 8), (6, 4) ]:

for k, v in mapping.items( ):

# Simultaneous Assignments

- x, y, z = 6, 2, 5
- j, k = k, j

- dir( ) and vars( )

#  First-Class Objects

In this case, we have not created a new function, we have simply defined scream
as an alias for the existing print function.

scream = print 
scream( Hello )


# Import statement

While the built-in namespace includes a few mathematical functions (e.g., abs, min, max, round), many more
are relegated to the math module (e.g., sin, cos, sqrt).

- from math import pi, sqrt // --> specific resources
- from math import * // --> all resources
- import math  // --->  example user: math.pi or math.sqrt(2).


- Existing Modules

Module Name // Description
- array // Provides compact array storage for primitive types.
- collections // Defines additional data structures and abstract base classes involving collections of objects.
- copy //  Defines general functions for making copies of objects.
- heapq // Provides heap-based priority queue functions (see Section 9.3.7).
- math // Defines common mathematical constants and functions.
- os // Provides support for interactions with the operating system.
- random  // Provides random number generation.
- re // Provides support for processing regular expressions.
- sys // Provides additional level of interaction with the Python interpreter.
- time // Provides support for measuring time, or delaying a program.


Page 76 -> solution projects
