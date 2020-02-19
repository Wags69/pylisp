import reader as reader
import printer as printer
import lisp_types as types
from lisp_types import Environment
from core import repl_env
import sys


def READ(string: str) -> types.LispType:
    return reader.read_string(string)


def eval_ast(expr: types.LispType, env: Environment) -> types.LispType:
    if types.is_symbol(expr):
        return env.get(expr)
    elif types.is_list(expr):
        return types.List([EVAL(e, env) for e in expr])
    elif types.is_vector(expr):
        return types.Vector([EVAL(e, env) for e in expr])
    elif types.is_hash_map(expr):
        return types.HashMap({x: EVAL(y, env) for x, y in expr.items()})
    else:
        return expr


def EVAL(expr: types.LispType, env: Environment) -> types.LispType:
    while True:
        if not types.is_list(expr):
            return eval_ast(expr, env)

        if len(expr) == 0:
            return expr

        if types.is_list(expr):
            if expr[0] == 'def!':
                ele1, ele2 = expr[1], expr[2]
                value = env.set(types.Symbol(ele1), EVAL(ele2, env))
                return value
            elif expr[0] == 'let*':
                new_env = Environment(env)
                ele1 = expr[1]

                keys = ele1[::2]
                values = ele1[1::2]

                for k, v in zip(keys, values):
                    new_env.set(types.Symbol(k), EVAL(v, new_env))

                env = new_env
                expr = expr[2]
                continue
            elif expr[0] == 'do':
                for e in expr[1:-1]:
                    EVAL(e, env)
                expr = expr[-1]
                continue
            elif expr[0] == 'if':
                cond = EVAL(expr[1], env)
                if cond:
                    expr = expr[2]
                elif not cond and len(expr) == 4:
                    expr = expr[3]
                else:
                    expr = None
                continue
            elif expr[0] == 'fn*':
                closure = types.Closure(
                    expr[1], expr[2], env, EVAL
                )
                return closure
            else:
                fun, *args = eval_ast(expr, env)
                return fun(*args)


def PRINT(expr: types.LispType) -> str:
    return printer.print_string(expr)


def REP(expr: str) -> str:
    return PRINT(EVAL(READ(expr), repl_env))


repl_env.set(types.Symbol('eval'), lambda a: EVAL(a, repl_env))
repl_env.set(types.Symbol('*ARGV*'), types.List(sys.argv[1:]))
REP("(def! not (fn* (a) (if a false true)))")
REP('(def! load-file (fn* (f) (eval (read-string (str "(do " (slurp f) "\nnil)")))))')
#REP('(def! a (slurp "../tests/incA.mal"))')

if __name__ == '__main__':
    while True:
        try:
            print(REP(input('user> ')))
        except Exception as exception:
            print(exception)