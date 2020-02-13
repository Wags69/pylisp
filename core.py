import lisp_types as types
from printer import print_string
from reader import read_string
import os


def pr_str(*expr):
    return ' '.join([print_string(e) for e in expr])


def string(*expr):
    return ''.join([print_string(e, prnt_rd=False) for e in expr])


def prn(*expr):
    print(' '.join([print_string(e) for e in expr]))


def println(*expr):
    print(' '.join([print_string(e) for e in expr]))


def slurp(file_name):
    #path = os.getcwd()
    test = ''
    with open(file_name, 'r') as file:
        test = file.read()

    return test


def swap(atom, fun, *params):
    param_list = []
    param_list.append(atom.value)
    if len(params) != 0:
        param_list.extend(params)
    return atom.set_value(fun(*param_list))


def cons(item, lst):
    return types.List([item] + lst)


def concat(*lsts):
    n_lst = []
    for lst in lsts:
        n_lst.extend(lst)

    return types.List(n_lst)

repl_env = types.Environment(None)
repl_env.set(types.Symbol('+'), lambda a, b: a + b)
repl_env.set(types.Symbol('-'), lambda a, b: a - b)
repl_env.set(types.Symbol('*'), lambda a, b: a * b)
repl_env.set(types.Symbol('/'), lambda a, b: a // b)
repl_env.set(types.Symbol('list'), lambda *a: types.List(a))
repl_env.set(types.Symbol('vector'), lambda *a: types.Vector(a))
repl_env.set(types.Symbol('list?'), types.is_list)
repl_env.set(types.Symbol('vector?'), types.is_vector)
repl_env.set(types.Symbol('empty?'), lambda a: len(a) == 0)
repl_env.set(types.Symbol('count'), lambda a: len(a))
repl_env.set(types.Symbol('='), lambda a, b: a == b)
repl_env.set(types.Symbol('>'), lambda a, b: a > b)
repl_env.set(types.Symbol('>='), lambda a, b: a >= b)
repl_env.set(types.Symbol('<'), lambda a, b: a < b)
repl_env.set(types.Symbol('<='), lambda a, b: a <= b)
repl_env.set(types.Symbol('pr-str'), pr_str)
repl_env.set(types.Symbol('str'), string)
repl_env.set(types.Symbol('prn'), prn)
repl_env.set(types.Symbol('println'), println)
repl_env.set(types.Symbol('read-string'), read_string)
repl_env.set(types.Symbol('slurp'), slurp)
repl_env.set(types.Symbol('atom'), types.make_atom)
repl_env.set(types.Symbol('atom?'), types.is_atom)
repl_env.set(types.Symbol('deref'), lambda a: a.value)
repl_env.set(types.Symbol('reset!'), lambda a, b: a.set_value(b))
repl_env.set(types.Symbol('swap!'), swap)
repl_env.set(types.Symbol('cons'), cons)
repl_env.set(types.Symbol('concat'), concat)