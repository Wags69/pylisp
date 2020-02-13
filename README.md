# pylisp
A lisp implementation in python.

## The Basics

pylisp is a dialect of fully functional(not yet :P) dialect of lisp.
Quoting from [Wikipedia](https://en.wikipedia.org/wiki/Lisp_(programming_language)):
> Lisp (historically LISP) is a family of computer programming languages with a long history and a distinctive, fully parenthesized prefix notation.

Therefore, addition in pylisp would be postfix:
```lisp
(+ a b)
```
rather than, infix:
```
(a + b)
```
that you would see in popular languages (like C and python).
A complex expression like:
```lisp
a + b / 3 ** 6 * c
```
reduces(or rather expands) to:
```lisp
(+ a (/ b (* (** 3 6) c)))
```
You could even say + here acts like a function that takes in two parameters:
```
+(a, b) where + : int -> int
```
More or less every action in pylisp, just like in lisp, acts like a function. Moreover functions themself can be passed around and stored in variables just like you would an integer. For example, this is how you store an integer in a variable:
```lisp
(def! a 6)
```
`def!` assigns 6 to the variable a. This is how you would define a function:
```lisp
(fn* (a) (+ a 1))
```
and this is how you would pass integers to it:
```lisp
((fn* (a) (+ a 1)) 1)
```
but typing function definations again and again is quite cumbersome. So, you just save it in a variable!
```lisp
(def! ++ (fn* (a) (+ a 1)))

(++ 1) ;; this would output 1
```

## Data Types
The first integral data type is the integer, pretty straight forward. You can do you normal arithmatic operations like `+`, `*`, `-`, `/`. You can also do comparison operations like `eq?`, `gt?`, etc. For right now there is only one logical operator `nor`, but all the other logical operators can easily be implemented in pylisp itself from `nor`. The second data type is the list. The list is very important. It is the central data type of pylisp which holds the functions and its parameters together. All expressions in lisp start and end with a list. If pylisp is a cheese sandwhich, the cheese is the list. In the many examples shown above it is very easy to see what the function of a list is. But it cannot act as an array, because it solely exists for the application of a function onto its parameters/arguments. If you want contiguous storage of types, use a vector:
```lisp
[1, 2, 3, 4, 5, "6"]
```
There is also a associative array/dictionary/mapping type called the hashmap:
```lisp
{:a 1 :b 2} ;; in python this would be {"a": 1, "b": 2}
```

Here `:a` is a keyword. Its another data type that is just a special symbol just used for the sake of being a label. Then we have strings. Nothing special really.
```lisp
(+ "Hello " "World!") ;;Hello World!
```

## What can pylisp do?
Right now it's a glorified calculator whith some extra spice. pylisp can interpret itself ;). For example:
```lisp
(eval (read-string "(+ 2 3)"))
```
It even has basic flow control:
```lisp
(if true (+ 2 3) (- 2 3)) ;; this would output 5
(do (+ 2 3) (+ 3 4)) ;; this would output 7
(let* (a 6) (+ a 6)) ;; this defines a new "block" of code, where a refers to 6
```
Note the lack of loops. That's because you don't need loops. Just recurse your functions :P.
 
## What will it do?
Right now it lacks the cream of lisp , that is the quoting and macro system. I also want it to interop with python, so that pylisp can even import python modules and run python scripts. Later I want to move the pylisp implementation to rust, and then afterwords move it to C compilation.

## Thanks to:
https://github.com/kanaka/mal
