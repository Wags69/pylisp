from typing import Union, Any


class List(list):
    pass


class Symbol(str):
    pass


class KeyWord(str):
    def __repr__(self):
        return ':' + str.__repr__(self)[1: -1]

    def __str__(self):
        return self.__repr__()


class Vector(list):
    pass


class HashMap(dict):
    pass


class LispException(Exception):
    pass


class Environment:
    def __init__(self, outer, keys=None, values=None):
        self.outer = outer
        self.data = {}

        if keys is not None:
            for i in range(len(keys)):
                if keys[i] == '&':
                    self.data[keys[i+1]] = List(values[i:])
                    break
                self.data[keys[i]] = values[i]

    def set(self, key, value):
        self.data[key] = value
        return value

    def find(self, key):
        if key in self.data.keys():
            return self
        elif key not in self.data.keys() and self.outer is not None:
            return self.outer.find(key)
        else:
            return None

    def get(self, key):
        env: Environment = self.find(key)
        if env is None:
            raise LispException(f'{key} not found.')
        else:
            return env.data[key]


class Closure:
    def __init__(self, params, body, curr_env, eval_fn):
        self.params = params
        self.body = body
        self.curr_env = curr_env
        self.eval_fn = eval_fn

    def __call__(self, *args):
        new_env = Environment(self.curr_env, self.params, args)
        return self.eval_fn(self.body, new_env)


class Atom:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'(atom {self.value})'

    def __str__(self):
        return self.__repr__()

    def set_value(self, value):
        self.value = value
        return self.value


LispType = Union[
    List, Symbol, int, bool, None, str, KeyWord, Vector,
    HashMap, Closure, Atom
]


def is_list(obj: Any) -> bool:
    return type(obj) == List


def is_symbol(obj: Any) -> bool:
    return type(obj) == Symbol


def is_string(obj: Any) -> bool:
    return type(obj) == str


def is_vector(obj: Any) -> bool:
    return type(obj) == Vector


def is_hash_map(obj: Any) -> bool:
    return type(obj) == HashMap


def is_sequence(obj: Any) -> bool:
    return is_list(obj) or is_vector(obj)


def is_atom(obj: Any) -> bool:
    return type(obj) == Atom

def make_list(lst: list) -> List:
    return List(lst)


def make_vector(lst: list) -> Vector:
    return Vector(lst)


def make_hash_map(key_values: list) -> HashMap:
    keys = key_values[::2]
    values = key_values[1::2]
    if len(keys) == len(values):
        return HashMap({x: y for x, y in zip(keys, values)})
    else:
        raise Exception('no. of keys and values are not matching')


def make_atom(value):
    return Atom(value)


def is_pair(value):
    return len(value) != 0