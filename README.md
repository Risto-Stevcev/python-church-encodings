# Church Encodings in Python

This exercise was to demonstrate and play around with church encodings in a more involved way, and as a way for me to gain experience with python and it's type system.

**Church encodings** were developed by the late and famous Alonzo Church. Church is probably most well known for inventing **lambda calculus**, a formal branch of mathematics that introduces the notion of **lambas**, or *anonymous functions*. You may have used them before when programming.

**Church encodings** are a very interesting development arising from **lambda calculus**. Church found out that every concept in programming languages can be represented using *functions*! everything from boolean logic, conditional statements, numbers (natural, integer, real, complex, imaginary), and even loops (infinite loops also)!

The most interesting thing about this is that numbers aren't anything special in math, they're just convenient placeholders. Math is really just logic in it's purest form.

So far I've translated church booleans, church boolean operators, church conditionals, church comparison operators, church numerals (natural numbers), church arithmetic operators (for natural numbers), church lists, church integers, loops with the z-combinator, and church arithmetic operators (for integers) less the exponential and factorial operators. 

**View the package on [PyPI](http://pypi.python.org/pypi/church_encoding/0.1)**


## Z Combinator

The Z combinator is used in place of the Y combinator in normal form progrmaming languages that don't implement lazy evaluation or call by name. See the [fixed-point combinator](https://en.wikipedia.org/wiki/Fixed-point_combinator) wiki for more details.


## Conditionals

The translation for some of the lambda functions involved using regular if/then statements instead of the **ifelse** lamdba function. I suspect that this might again be a limitation like the Z combinator, where the evaluation order plays a role in being able to use lambdas in the truest sense. There may be a workaround I'll find to get it to work some day.


## Installation

* Install using pip.  
   ``pip install --user church_encodings``

* Import the church module.  


    python    
    >>> import church_encoding.church as church


* Play around with the functions.  
   

    >>> dir(church)  
    >>> (church.unchurch_bool) ((church.AND) (church.true) (church.false))  
    False  


Here is a full list of the commands:  

Boolean true/false: ``true``, ``false``, ``unchurch_bool``  
Boolean operators: ``AND``, ``NOT``, ``OR``, ``XOR``  
Z-combinator: ``Z``  
Conditional: ``ifelse``  

Natural numbers: ``zero``, ``one``, ``two``, ``three``, ``num``, ``unchurch_num``  
Integers: ``convertNZ``, ``unchurch_int``  
Comparison operators (natural numbers): ``eq``, ``geq``, ``gt``, ``leq``, ``lt``  
Arithmetic operators (natural numbers): ``pred``, ``succ``, ``add``, ``sub``, ``mult``, ``div``, ``divnZ``, ``exp``, ``fac``, ``is_zero``  
Arithmetic operators (integers): ``addZ``, ``subZ``, ``multZ``, ``divZ``, ``neg``, ``onezero``  
Lists: ``car``, ``cdr``, ``cons``  


For usage examples, see the [test suite](https://github.com/Risto-Stevcev/python-church-encodings/blob/master/church-encoding/test/church_test.py)


## Credits

I'd like to give credit where it's due:

* [James Tauber's Blog](http://jtauber.com/blog/2008/11/26/church_encoding_in_python/) for starting me off in the right direction.  

* The [chuch encoding](https://en.wikipedia.org/wiki/Church_encoding) wikipedia page for being so incredibly detailed and informative.  

And finally, Church himself, for being such a badass!  

![Alonzo Church](https://upload.wikimedia.org/wikipedia/en/a/a6/Alonzo_Church.jpg)  
Alonzo Church
