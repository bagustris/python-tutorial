---
title: "Basics"
teaching: 20
exercises: 25
questions:
- "How do I run Python programs?"
- "What are Python's basic data types?"
objectives:
- "Launch the IPython, doing some operations, and exit the IPython."
- "Create and run Python commands in IPython."
- "Write simple scripts that use atomic data types, variables, and lists."
keypoints:
- "Python programs are plain text files."
- "We can write Python in the IPython as well as plain text)."
- "Most common atomic data types are `int`, `float`, `str`, and `bool`."
- "Most common type of collection is `list`."
- "Use variables to store values."
- "Use `print` to display values."
- "Variables persist between cells."
- "Variables must be created before they are used."
- "Use an index to get a single character from a string or list."
- "Use a slice to get a substring or sub-list."
- "Use the built-in function `len` to find the length of a string."
- "Python is case-sensitive."
---
## Python programs are plain text files.

*   They use the `.py` extension by convention.
*   It's common to write them using a text editor or running interactively using ipython,
    but we are going to use the [IPython][IPython].
    *   Python files use `.py` extension.
    *   We can run that file using `run file.py` inside IPython
    *   Provides code completion and other helpful features.

## IPtyhon
*   Open it with --pylab option to enable plot interatively
*   When you need to edit the module and want to take effect immedietly use autoload magic

~~~
%load_ext autoreload
from module1 import function1
## edit module1
%autoreload 2

~~~
{: .python}

For more information about autoreload, you can refer to the documentation [here](https://ipython.readthedocs.io/en/stable/config/extensions/autoreload.html?highlight=autoreload).

## Use the IPython for running Python.

*   The [PIP package manager][pip] is an automated way to install the IPython.
    *   In Ubuntu-based, `pip` can be installed with `sudo apt install python3-pip`.
    *   If you have multiple version of Python (e.g., python3.6, python3.8), use instrunction with [get-pip](https://pip.pypa.io/en/stable/installing/#)
*   "Batteries included": comes with lots of scientific libraries.
*   Once you have installed Python and the IPython requirements, open a shell and type:

    ~~~
    $ python3.6 -m IPython
    ~~~
    {: .source}

    where `python3.6` is the python version you want to launch with IPython.
*   You can type code inside the shell and see the result below you commands.
*   This has several advantages:
    *   You can easily type, edit, and copy and paste blocks of code.
    *   Tab complete allows you to easily access the names of things you are using
        and learn more about them.
    *   You don't a browser (like Jupyter Notebook) and complicated setup.
    *   It allows you to display figures next to the code that produces them
        to tell a complete story of the analysis.


> ## Code vs. Text
>
> We often use the term "code" to mean
> "the source code of software written in a language such as Python".
> A "code command" in a command is a IPython that contains software;
> a "text comment started bt `#`" is one that contains ordinary prose written for human beings.
{: .callout}


## Use variables to store values.

*   Variables are names for values.
    *   Like sticky notes rather than locations in memory.
*   Use `var = value` to do assignment.
*   The variable is created when a value is assigned to it.

~~~
age = 42
first_name = 'Ahmed'
~~~
{: .python}

*   Variable names:
    *   cannot start with a digit
    *   cannot contain spaces, quotation marks, or other punctuation
    *   *may* contain an underscore (typically used to separate words in long variable names)
*   Underscores at the start like `__alistairs_real_age` have a special meaning
    so we won't do that until we understand the convention.

## Use `print` to display values.

*   Built-in function `print` displays things as text.

~~~
print(first_name, 'is', age, 'years old')
~~~
{: .python}
~~~
Ahmed is 42 years old
~~~
{: .output}

*   `print` automatically puts a single space between items and a newline at the end.

## Variables must be created before they are used.

*   If a variable doesn't exist yet, or if the name has been mis-spelled,
    Python reports an error.
    *   Unlike some languages, which "guess" a default value.

~~~
print(last_name)
~~~
{: .python}
~~~
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-1-c1fbb4e96102> in <module>()
----> 1 print(last_name)

NameError: name 'last_name' is not defined
~~~
{: .error}

*   The last line of an error message is usually the most informative.
*   Variables defined in one cell exist in all other cells once executed,
    so the relative location of cells in the notebook do not matter
    (i.e., cells lower down can still affect those above).

## Python provides the usual atomic types and operators.

*   `int`, `float`, and `str`.
*   `+`, `-`, `*`, `/`, '%', and '^' on numbers.
    *   `int/int` keeps the fractional part.
    *   `int//int` is integer division.
*   `+` and `*` on strings.
    *   Which can be written using either single or double quotes.
    *   And may include the usual C escape characters like `\t` and `\n`.

## Index and slice to get information out of a string.

*   Locations are numbered from 0 rather than 1.
*   Negative indices count backward from the end of the string.
*   Slices *include* the lower bound but *exclude* the upper bound.
    *   So `upper-lower` is the slice's length.

~~~
element = 'helium'
print('first character:', element[0])
print('last character:', element[-1])
print('middle:', element[2:5])
~~~
{: .python}
~~~
first character: h
last character: m
middle: liu
~~~
{: .output}

## Use the built-in function `len` to find the length of a string.

~~~
print(len('helium'))
~~~
{: .python}
~~~
6
~~~
{: .output}

## Python containers
Python includes several built-in containers types: list, dictionaries, sets, and tupple.

## A list stores many values in a one-dimensional structure.

*   Values separated by ',' contained within square brackets `[...]`.
*   Index, slice, and use `len` the same way as strings.

~~~
pressures = [0.273, 0.275, 0.277, 0.275, 0.276]
print('pressures:', pressures)
print('length:', len(pressures))
print('second value:', pressures[1])
print('middle:', pressures[1:-1])
~~~
{: .python}
~~~
pressures: [0.273, 0.275, 0.277, 0.275, 0.276]
length: 5
second value: 0.275
middle: [0.275, 0.277, 0.275]
~~~
{: .output}

## Lists' values can be replaced by assigning to them.

~~~
pressures[0] = 0.265
print('pressures is now:', pressures)
~~~
{: .python}
~~~
pressures is now: [0.265, 0.275, 0.277, 0.275, 0.276]
~~~
{: .output}

## Appending items to a list lengthens it.

*   Use `list.append` to add items to the end of a list.

~~~
primes = [2, 3, 5]
print('primes is initially:', primes)
primes.append(7)
primes.append(9)
print('primes has become:', primes)
~~~
{: .python}
~~~
primes is initially: [2, 3, 5]
primes has become: [2, 3, 5, 7, 9]
~~~
{: .python}

*   `append` is a *method* of lists.
    *   Like a function, but tied to a particular object.
*   Use `object_name.method_name` to call methods.
    *   Deliberately resembles the way we refer to things in a library.
*   We will meet other methods of lists as we go along.
    *   Use `help(list)` for a preview.

## Use `del` to remove items from a list entirely.

*   `del list_name[index]` removes an item from a list and shortens the list.
*   Not a function or a method, but a statement in the language.

~~~
print('primes before removing last item:', primes)
del primes[4]
print('primes after removing last item:', primes)
~~~
{: .python}
~~~
primes before removing last item: [2, 3, 5, 7, 9]
primes after removing last item: [2, 3, 5, 7]
~~~
{: .output}

## The empty list contains no values.

*   `[]` is "the zero of lists".

## Lists may be *heterogeneous*.

~~~
goals = [1, 'Create lists.', 2, 'Extract items from lists.', 3, 'Modify lists.']
~~~
{: .python}

*   Not always a good idea...

## Character strings are *immutable*.

*   Cannot change the characters in a string after it has been created.
*   Python considers the string to be a single value with parts,
    not a collection of values.

~~~
element[0] = 'C'
~~~
{: .python}
~~~
TypeError: 'str' object does not support item assignment
~~~
{: .error}

## Indexing beyond the end of a collection is an error.

*   Python reports an `IndexError` if we attempt to access a value that doesn't exist.

~~~
print('99th element of element is:', element[99])
~~~
{: .python}
~~~
IndexError: string index out of range
~~~
{: .output}


We will study about dictionaries, sets, and tupple later.
> ## More Math
>
> What is displayed when a Python cell in a notebook
> that contains several calculations is executed?
> For example, what happens when this cell is executed?
>
> ~~~
> 7 * 3
> 2 + 1
> ~~~
> {: .source}
{: .challenge}


> ## Swapping Values
>
> Draw a table showing the values of the variables in this program
> after each statement is executed.
> In simple terms, what do the last three lines of this program do?
>
> ~~~
> lowest = 1.0
> highest = 3.0
> temp = lowest
> lowest = highest
> highest = temp
> ~~~
> {: .source}
{: .challenge}

> ## Predicting Values
>
> What is the final value of `position` in the program below?
> (Try to predict the value without running the program,
> then check your prediction.)
>
> ~~~
> initial = "left"
> position = initial
> initial = "right"
> ~~~
> {: .source}
{: .challenge}

> ## Challenge
>
> If you assign `a = 123`,
> what happens if you try to get the second digit of `a`?
>
> > ## Solution
> > Numbers are not stored in the written representation,
> > so they can't be treated like strings.
> >
> > ~~~
> > a = 123
> > print(a[1])
> > ~~~
> > {: .python}
> > ~~~
> > TypeError: 'int' object is not subscriptable
> > ~~~
> > {: .error}
> {: .solution}
{: .challenge}

> ## Choosing a Name
>
> Which is a better variable name, `m`, `min`, or `minutes`?
> Why?
> Hint: think about which code you would rather inherit
> from someone who is leaving the lab:
>
> 1. `ts = m * 60 + s`
> 2. `tot_sec = min * 60 + sec`
> 3. `total_seconds = minutes * 60 + seconds`
>
> > ## Solution
> >
> > `minutes` is better because `min` might mean something like "minimum"
> > (and actually does in Python, but we haven't seen that yet).
> {: .solution}
{: .challenge}

> ## Slicing
>
> What does the following program print?
>
> ~~~
> element = 'carbon'
> print('element[1:3] is:', element[1:3])
> ~~~
> {: .python}
> ~~~
> element[1:3] is: ar
> ~~~
> {: .output}
>
> 1.  What does `thing[low:high]` do?
> 2.  What does `thing[low:]` (without a value after the colon) do?
> 3.  What does `thing[:high]` (without a value before the colon) do?
> 4.  What does `thing[:]` (just a colon) do?
{: .challenge}

> ## Fill in the Blanks
>
> Fill in the blanks so that the program below produces the output shown.
>
> ~~~
> values = ____
> values.____(1)
> values.____(3)
> values.____(5)
> print('first time:', values)
> values = values[____]
> print('second time:', values)
> ~~~
> {: .python}
>
> ~~~
> first time: [1, 3, 5]
> second time: [3, 5]
> ~~~
> {: .output}
{: .challenge}

> ## How Large is a Slice?
>
> If 'low' and 'high' are both non-negative integers,
> how long is the list `values[low:high]`?
{: .challenge}

> ## From Strings to Lists and Back
>
> Given this:
>
> ~~~
> print('string to list:', list('tin'))
> print('list to string:', ''.join(['g', 'o', 'l', 'd']))
> ~~~
> {: .python}
> ~~~
> ['t', 'i', 'n']
> 'gold'
> ~~~
> {: .output}
>
> 1.  Explain in simple terms what `list('some string')` does.
> 2.  What does `'-'.join(['x', 'y'])` generate?
{: .challenge}

> ## Working With the End
>
> What does the following program print?
>
> ~~~
> element = 'helium'
> print(element[-1])
> ~~~
> {: .python}
>
> 1.  How does Python interpret a negative index?
> 2.  If a list or string has N elements,
>     what is the most negative index that can safely be used with it,
>     and what location does that index represent?
> 3.  If `values` is a list, what does `del values[-1]` do?
> 4.  How can you display all elements but the last one without changing `values`?
>     (Hint: you will need to combine slicing and negative indexing.)
{: .challenge}

> ## Stepping Through a List
>
> What does the following program print?
>
> ~~~
> element = 'fluorine'
> print(element[::2])
> print(element[::-1])
> ~~~
> {: .python}
>
> 1.  If we write a slice as `low:high:stride`, what does `stride` do?
> 2.  What expression would select all of the even-numbered items from a collection?
{: .challenge}

> ## Slice Bounds
>
> What does the following program print?
>
> ~~~
> element = 'lithium'
> print(element[0:20])
> print(element[-1:3])
> ~~~
> {: .python}
{: .challenge}

> ## Sort and Sorted
>
> What do these two programs print?
> In simple terms, explain the difference between `sorted(letters)` and `letters.sort()`.
>
> ~~~
> # Program A
> letters = list('gold')
> result = sorted(letters)
> print('letters is', letters, 'and result is', result)
> ~~~
> {: .python}
>
> ~~~
> # Program B
> letters = list('gold')
> result = letters.sort()
> print('letters is', letters, 'and result is', result)
> ~~~
> {: .python}
{: .challenge}

> ## Copying (or Not)
>
> What do these two programs print?
> In simple terms, explain the difference between `new = old` and `new = old[:]`.
>
> ~~~
> # Program A
> old = list('gold')
> new = old      # simple assignment
> new[0] = 'D'
> print('new is', new, 'and old is', old)
> ~~~
> {: .python}
>
> ~~~
> # Program B
> old = list('gold')
> new = old[:]   # assigning a slice
> new[0] = 'D'
> print('new is', new, 'and old is', old)
> ~~~
> {: .python}
{: .challenge}

[pip]: https://pip.pypa.io/en/stable/
[IPython]: https://ipython.org/
