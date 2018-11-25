from utils import is_variable, is_constant

def unify_var(var, x, subsList):
    if subsList.get(var, False):
        return unify(subsList[var], x, subsList)
    elif subsList.get(x, False):
        return unify(var, subsList[x], subsList)
    else:
        subsList[var] = x
        return subsList

def unify(x, y, subsList):
    if subsList == "Fail":
        return "Fail"
    elif x == y:
        return subsList
    elif is_variable(x):
        return unify_var(x, y, subsList)
    elif is_variable(y):
        return unify_var(y, x, subsList)
    elif isinstance(x, list) and isinstance(y, list): 
        return unify(x[1:], y[1:], unify(x[0], y[0], subsList))
    else:
        return "Fail"