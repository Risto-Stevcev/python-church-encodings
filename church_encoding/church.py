#!/usr/bin/env python
# -*- coding: utf-8 -*-

# # # # # # # # # # #
# Church Encodings  #
# # # # # # # # # # #

__author__ = "Risto Stevcev"



# Boolean Operators #
# # # # # # # # # # #

# Church Boolean (True)
# λt.λf.t
true = lambda a: lambda b: (a)

# Church Boolean (False)
# λt.λf.f
false = lambda a: lambda b: (b)

# Church AND
# λa.λb.a b false
AND = lambda a: lambda b: (a)(b)(a)

# Church OR
# λa.λb.a true b
OR  = lambda a: lambda b: (a)(a)(b)

# Church NOT
# λp.λa.λb.p b a
NOT = lambda a: lambda b: lambda c: (a)(c)(b)

# Church XOR
# λa.λb.a (not b) b
XOR = lambda a: lambda b: (a)((NOT) (b))(b)

# Convert Church Boolean to Python Bool
# (λa.λb.λc.c a b) True False
unchurch_bool = (lambda a: lambda b: lambda c: (c)(a)(b)) (True)(False)



# Church Natural Numbers (n ∈ ℕ)  #
# # # # # # # # # # # # # # # # # #

# Church Numeral: 0
# λf.λx.x-
zero = lambda f: lambda x: (x)

# Church Numeral: 1
# λf.λx.f x
one = lambda f: lambda x: (f)(x)

# Church Numeral: 2
# λf.λx.f (f x)
two = lambda f: lambda x: (f)((f)(x))

# Church Numeral: 3
# λf.λx.f (f (f x))
three = lambda f: lambda x: (f)((f)((f)(x)))

# Church Numeral: n (where n ∈ ℕ)
# num 0 = λf.λx.x
# num n = λf.λx.f (num (n-1) f x)
def num (n):
    if n == 0:
        return lambda f: lambda x: (x)
    else:
        return  lambda f: lambda x: (f)((num (n-1)) (f)(x))

# Convert Church Numeral (n ∈ ℕ) to Haskell Integer
# λa.a (λb.b+1) (0)
unchurch_num = lambda a: (a)(lambda b: b + 1)(0)



# Church Conditionals #
# # # # # # # # # # # #

# Church Conditional (If/Else)
# λp.λa.λb.p a b
ifelse = lambda p: lambda a: lambda b: (p)(a)(b)



# Church Loops  #
# # # # # # # # #

# Z Combinator (for normal-order languages, Y combinator doesn't apply)
# λf.(λx.f (x x)) (λx.f (x x))
Z = lambda f: (lambda x: f(lambda *args: x(x)(*args)))(lambda x: f(lambda *args: x(x)(*args)))



# Church Comparison Operators #
# # # # # # # # # # # # # # # #

# Church Comparison (== 0)
# λn.n (λx.false) true
is_zero = lambda n: (n) (lambda x: (false)) (true)

# Church Comparison (<)
# λm.λn.and (is_zero (sub m n)) (not (is_zero (sub n m)))
lt = lambda m: lambda n: (AND) ((is_zero) ((sub) (m)(n))) ((NOT) ((is_zero) ((sub) (n)(m))))

# Church Comparison (<=)
# λm.λn.is_zero (sub m n)
leq = lambda m: lambda n: (is_zero) ((sub) (m)(n))

# Church Comparison (==)
# λm.λn.and (leq m n) (leq n m)
eq = lambda m: lambda n: (AND) ((leq) (m)(n)) ((leq) (n)(m)) 

# Church Comparison (>=)
# λm.λn.or (not (leq m n)) (eq m n)
geq = lambda m: lambda n: (OR) ((NOT) ((leq) (m)(n))) ((eq) (m)(n))

# Church Comparison (>)
# λm.λn.not (leq m n)
gt = lambda m: lambda n: (NOT) ((leq) (m)(n))



# Church Arithmetic Operators (n ∈ ℕ) #
# # # # # # # # # # # # # # # # # # # #

# Church Successor
# λn.λf.λx.f (n f x)
succ = lambda n: lambda f: lambda x: (f)((n)(f)(x))

# Church Predecessor
# λn.λf.λx.n (λg.λh.h (g f)) (λu.x) (λu.u)
pred = lambda n: lambda f: lambda x: n (lambda g: lambda h: (h) ((g) (f))) (lambda u: (x)) (lambda u: (u))

# Church Addition
# λm.λn.λf.λx.m f (n f x)
add = lambda a: lambda b: lambda c: lambda d: (a)(c)((b)(c)(d))

# Church Subtraction
# λm.λn. n pred m
sub = lambda m: lambda n: (n) (pred) (m)

# Church Multiplication
# λm.λn.λf.m (n f)
mult = lambda a: lambda b: lambda c: (b)((a)(c))

# Church Division
# λd n m.ifelse (geq n m) (succ (d (sub n m) m)) zero 
div = Z(lambda f: lambda n: lambda m: ((succ) ( (f)((sub) (n)(m))(m) ))  
        if ((unchurch_bool) ((geq) (n)(m))) else (zero) )

# Church Exponentiation
# λm.λn.n m
exp = lambda a: lambda b: (b)(a)

# Church Factorial
# λf n.ifelse (is_zero n) one (mult n (fac (pred n))) 
fac = Z(lambda f: lambda n: ((one) if ((unchurch_bool) ((is_zero) (n))) 
        else ( (mult) (n) ((f)((pred)(n))) ) ))



# Church Lists  #
# # # # # # # # #

# Church Cons (pair)
# λa.λb.λc.c a b
cons = lambda a: lambda b: lambda c: (c)(a)(b)

# Church Car (head/first)
# λa.a true
car  = lambda a: (a)(true)

# Church Cdr (tail/second)
# λa.a false
cdr  = lambda a: (a)(false)



# Church Integers (n ∈ ℤ) #
# # # # # # # # # # # # # #

# Convert Church Numeral (natural number) to Church Integer
# λx.pair x zero
convertNZ = lambda x: (cons) (x) (zero)

# Church Negation
# λx.pair (second x) (first x)
neg = lambda x: (cons) ((cdr) (x)) ((car) (x))

# Church OneZero 
# (Fixes incorrect integer representations that don't have a zero in the pair. 
# Ex: (7, 2) == 7 - 2 == 5) 
# λoneZ x.ifelse (is_zero (first x)) 
#   x (ifelse (is_zero (second x)) x (oneZ (pair (pred (first x)) (pred (second x)))))
onezero = Z(lambda oneZ: lambda x: (x) if 
            ((unchurch_bool) ((is_zero) ((car) (x)))) 
              else ((x) if 
                   ((unchurch_bool) ((is_zero) ((cdr) (x))))
                   else ((oneZ) ((cons) ((pred) ((car) (x))) ((pred) ((cdr) (x))))) ))

# Convert Church Integer to Haskell Integer
# λx.ifelse (is_zero (first x)) (-1*(unchurch_num (second x))) 
#                               (unchurch_num (first x))
unchurch_int = lambda x: (ifelse) ((is_zero) ((car) (x))) \
                 ((-1)*((unchurch_num) ((cdr) (x)))) ((unchurch_num) ((car) (x)))



# Church Arithmetic Operators (n ∈ ℤ) #
# # # # # # # # # # # # # # # # # # # #

# Church Addition
# λx.λy.onezero (pair (add (first x) (first y)) (add (second x) (second y)))
addZ = lambda x: lambda y: (onezero) ((cons) ((add) ((car) (x))((car) (y))) 
                                             ((add) ((cdr) (x))((cdr) (y))))

# Church Subtraction
# λx.λy.onezero (pair (add (first x) (second y)) (add (second x) (first y)))
subZ = lambda x: lambda y: (onezero) ((cons) ((add) ((car) (x))((cdr) (y))) 
                                             ((add) ((cdr) (x))((car) (y))))

# Church Multiplication
# λx.λy.pair (add (mult (first x) (first y)) (mult (second x) (second y)))
#            (add (mult (first x) (second y)) (mult (second x) (first y)))
multZ = lambda x: lambda y: (cons) \
        ((add) ((mult) ((car) (x))((car) (y))) ((mult) ((cdr) (x))((cdr) (y)))) \
        ((add) ((mult) ((car) (x))((cdr) (y))) ((mult) ((cdr) (x))((car) (y))))

# Church DivNoZero
# (Divides only if the value is not zero)
# λx.λy.is_zero y zero (div x y)
divnZ = lambda x: lambda y: (zero) if ((unchurch_bool) ((is_zero) (y))) else ((div) (x) (y))

# Church Division
# λx.λy.pair (add (divnZ (first x) (first y)) (divnZ (second x) (second y)))
#            (add (divnZ (first x) (second y)) (divnZ (second x) (first y)))
divZ = lambda x: lambda y: (cons) \
       ((add) ((divnZ) ((car) (x))((car) (y))) ((divnZ) ((cdr) (x))((cdr) (y)))) \
       ((add) ((divnZ) ((car) (x))((cdr) (y))) ((divnZ) ((cdr) (x))((car) (y))))
