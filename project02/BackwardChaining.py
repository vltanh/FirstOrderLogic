from Unify import unify

def backward_chain(KB, query):
    query = query.get_unit(0)
    for x in fol_bc_or(KB, query, {}):
        yield x

def fol_bc_or(KB, query, theta):
    for fact in KB.facts:
        fact = fact.get_unit(0)
        if fact.checkable(query):
            theta_ = unify(fact.get_args(), query.get_args(), theta)
            if not theta_ == "Fail":
                yield theta_

    for rule in KB.rules:
        p, q = rule.standardize_apart().get_ante_cons()
        if q.checkable(query):
            theta_ = unify(q.get_args(), query.get_args(), theta)
            for theta1 in fol_bc_and(KB, p, theta_):
                yield theta1

def fol_bc_and(KB, goals, theta):
    if theta == "Fail":
        pass
    elif not goals or not goals.get_units():
        yield theta
    else:
        first, rest = goals.getFirstRest()
        for theta1 in fol_bc_or(KB, first.substitute(theta), theta):
            for theta2 in fol_bc_and(KB, rest, theta1):
                yield theta2