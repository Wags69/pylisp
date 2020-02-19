# pylisp specifications
This document lays down what I want pylisp to look like from v2 onwards. 

## pylisp types
* Numbers (integers and floats)
* Strings
* Symbols (identifiers)
* Labels (immutable strings that represent something important)
* Lists (fundamental data type; on eval, first element is applied on the rest)
* Vectors (collections like lists, but the first element is not applied on the rest)
* Maps (associative arrays)
* Lambdas (first class functions)

## Other stuff
* `if` and `switch..case` for conditional evaluation
* `do` for block evaluation
* recursion as general loop construct
* map, reduce, filter, any, all
* no exceptions
* `def` binds value to symbol
* macros
