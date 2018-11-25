import collections

c = collections.Counter()

def next(var):
    c.update([var])
    return c[var]