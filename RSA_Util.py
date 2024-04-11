class public_key:
    def __init__(self, n: int, e: int):
        self.n = n
        self.e = e

class private_key:
    def __init__(self, n: int, d: int):
        self.n = n
        self.d = d
        
def fme(base: int, exponent: int, mod: int):
    x = 1
    power = base % mod
    exponent = bin(exponent)
    o = len(exponent)
    for r in range(o - 1, 1, -1):
        if int(exponent[r]) == 1:
            x = (x * power) % mod
        power = (power * power) % mod
    return x
