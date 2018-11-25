from Unify import unify
from Substitution import Substitution

def forward_chain(KB, query):
    clone_KB = KB.clone()
    query = query.get_unit(0)
    subs = set()
    for fact in clone_KB.facts:
        for x in check_done(fact, query):
            if not x == "Fail": 
                x = Substitution(x)
                if x not in subs:
                    yield x
                    subs.add(x)
        fact = fact.get_unit(0)
        gain_new_knowledge(clone_KB, fact)
    # clone_KB.show(show_facts = True, show_rules = True)

def check_done(new_fact, query):
    fact = new_fact.get_unit(0)
    if fact.checkable(query):
        theta = unify(query.get_args(), fact.get_args(), {})
        yield theta
    yield "Fail"

def gain_new_knowledge(KB, fact):
    for rule in KB.rules:
        for idx, unit in enumerate(rule.get_units()):
            if unit.potential_conflict(fact):
                theta = unify(fact.get_args(), unit.get_args(), {})
                if theta == "Fail": continue

                remainder = rule.clone()
                remainder.remove_unit_at(idx)
                remainder = remainder.substitute(theta)

                if remainder.get_number_of_units() == 1:
                    # if not KB.contain_fact(remainder):
                        KB.add_fact(remainder)
                else:
                    # if not remainder in KB.rules:
                        KB.add_rule(remainder)