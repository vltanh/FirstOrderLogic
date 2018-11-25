def is_constant(x):
    if isinstance(x, str):
        return not x[0].islower()
    return False

def is_variable(x):
    if isinstance(x, str):
        return x[0].islower() or x[0] == '_'
    return False