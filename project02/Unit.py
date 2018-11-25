import re
from utils import is_variable, is_constant
from Counter import next

class Unit:
    def __init__(self):
        self.predicate = ''
        self.negated = False
        self.args = []

    @staticmethod
    def generate_from_string(s):
        unit = Unit()

        s = s.strip()

        match = re.search('^.*(?=\()', s)
        unit.predicate = match.group().strip()

        match = re.search('(?<=\().*(?=\))', s)
        unit.args = match.group().split(',')
        unit.args = [arg.strip() for arg in unit.args]

        unit.negated = False
        if unit.predicate[0] == '~':
            unit.negated = True
            unit.predicate = unit.predicate[1:]

        return unit

    def clone(self):
        unit = Unit()
        unit.predicate = self.predicate
        unit.negated = self.negated
        unit.set_args(self.args)
        return unit

    def set_args(self, args):
        self.args = [arg.strip() for arg in args]

    def get_args(self):
        return self.args

    def to_list(self):
        ret = list()
        ret += ['~'] if self.negated else ['+']
        ret += [self.predicate] + [arg for arg in self.args]
        return ret

    def __repr__(self):
        s = str()
        if self.negated: s += '~'
        s += self.predicate
        if len(self.args) > 0:
            s += '('
            for l in self.args[:-1]:
                s += l + ','
            s += self.args[-1]
            s += ')'
        return s

    def __str__(self):
        return self.__repr__()

    def get_arity(self):
        return len(self.args)

    def negate(self):
        unit = self.clone()
        unit.negated = not unit.negated
        return unit

    def checkable(self, unit):
        return unit.predicate == self.predicate and unit.get_arity() == self.get_arity()

    def potential_conflict(self, unit):
        return unit.predicate == self.predicate and unit.get_arity() == self.get_arity() and unit.negated != self.negated

    def contradict(self, unit):
        return self.predicate == unit.predicate and self.negated != unit.negated and self.args == unit.args

    def equal(self, unit):
        return self.predicate == unit.predicate and self.negated == unit.negated and self.args == unit.args

    def __eq__(self, unit):
        return self.equal(unit)

    def substitute(self, subsList):
        args = [x for x in self.args]
        if subsList:
            for idx, arg in enumerate(args):
                if subsList.get(arg, False):
                    args[idx] = subsList[arg]
        unit = self.clone()
        unit.set_args(args)
        return unit

    def get_constant_symbol(self):
        ret = set()
        for arg in self.args:
            if is_constant(arg):
                ret.add(arg)
        return ret

    def get_variable(self):
        ret = set()
        for arg in self.args:
            if is_variable(arg):
                ret.add(arg)
        return ret

    def get_ante_cons(self):
        return None, self

    def getFirstRest(self):
        return self, []

    def standardize_apart(self):
        variables = self.get_variable()
        mapping = dict()
        for variable in variables:
            suffix = next(variable)
            mapping[variable] = variable + str(suffix)

        return self.substitute(mapping)

    def __hash__(self):
        return hash((self.negated, self.predicate) + tuple(self.args))