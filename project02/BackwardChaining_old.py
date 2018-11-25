from Unify import unify
from Clause import Clause
from Substitution import Substitution

def backward_chain(KB, query):
    answers = backward_chain_(KB, query, {})
    subs = set()
    for x_ in answers:
        x = process_theta(x_, query)
        if x not in subs:
            yield x
            subs.add(x)
    return

def process_theta(theta, query):
    variables = query.get_variable()
    theta = compose_theta_(theta)
    result = { k : theta[k] for k in variables if theta.get(k, False) }
    return Substitution(result)

def compose_theta_(theta):
    compose_ = dict(theta)
    for k, v in compose_.items():
        while compose_.get(v, False):
            compose_[k] = compose_[v]
            compose_[v] = False
            v = compose_[k]
    compose_ = {k:v for k, v in compose_.items() if v}
    return compose_

def compose_theta(theta, theta_):
    compose = dict(theta)
    compose.update(theta_)
    return compose

def backward_chain_(KB, goals, theta):
    if not goals.to_list():
        return [theta]

    answers = list()
    first, rest = goals.getFirstRest()
    q_ = first.substitute(theta)

    for rule in KB.rules + KB.facts:
        p, q = rule.standardize_apart().get_ante_cons()
        if q.checkable(q_):
            theta_ = unify(q_.get_args(), q.get_args(), {})
            if theta_ == "Fail": continue

            new_goals = p
            for unit in rest.get_units(): new_goals.add_unit(unit)

            compose = compose_theta(theta, theta_)
            answers += backward_chain_(KB, new_goals, compose)

    return answers