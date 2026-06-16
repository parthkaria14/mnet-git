def calc(p, q, d):
    if d > 0:
        return p * q * (1 - d)
    else:
        return p * q

print(calc(100, 3, 0.1))