import math
import numpy as np
import matplotlib.pyplot as plt

class Value():

    def __init__(self, data, _children=(), _op=''):
        self.data = data
        self._prev = set(_children)
        self._op = _op

    def __repr__(self):
        return f"Value(data={self.data})"

    def __add__(self, other):
        return Value(self.data + other.data, (self, other), '+')
    
    def __mul__(self, other):
        return Value(self.data*other.data, (self, other), '*')


a = Value(2.0)
b = Value(-6.0)
c = a*b
d = Value(5.0)
e = d+c
print(e._prev)