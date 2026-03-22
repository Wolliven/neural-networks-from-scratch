import math
import numpy as np
import matplotlib.pyplot as plt

class Value():

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"Value(data={self.data})"

print(Value(2.0))