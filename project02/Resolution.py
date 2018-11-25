from Unify import unify
import time
from Substitution import Substitution

def resolution(KB, query):
    clone_KB = KB.clone()

    for fact in KB.facts:
        clone_KB.add_rule(fact)
    clone_KB.add_rule(query.negate())

    subs = set()
    for clause in clone_KB.rules:
        for x in gain_new_knowledge(clone_KB, clause, query):
            x = process_theta(x, query)
            if x == "Fail": continue
            if x not in subs:
                yield x
                subs.add(x)

def process_theta(theta, query):
    variables = query.get_variable()
    result = { k : theta[k] for k in variables if theta.get(k, False) }
    if len(variables) == len(result.items()):
        return Substitution(result)
    else:
        return "Fail"

def gain_new_knowledge(KB, clause, query):
    for clause_ in KB.rules:
        if clause == clause_: continue
        for idx, unit in enumerate(clause.get_units()):
            for idx_, unit_ in enumerate(clause_.get_units()):
                if unit.potential_conflict(unit_):
                    theta = unify(unit.get_args(), unit_.get_args(), {})
                    if theta == "Fail": continue

                    remainder = clause.clone()
                    remainder_ = clause_.clone()
                    remainder.remove_unit_at(idx)
                    remainder_.remove_unit_at(idx_)

                    for unit in remainder_.get_units():
                        remainder.add_unit(unit)
                    
                    if remainder.get_number_of_units() == 0:
                        yield theta
                        continue

                    remainder = remainder.substitute(theta)
                    KB.add_rule(remainder)