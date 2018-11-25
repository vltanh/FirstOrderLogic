from Unit import Unit
from Counter import next

class Clause:
    def __init__(self):
        self.units = []

    @staticmethod
    def generate_from_string(s):
        clause = Clause()
        units_str = s.strip().split('|')

        clause.units = []
        for unit_str in units_str:
            unit = Unit.generate_from_string(unit_str)
            clause.units.append(unit)

        return clause

    def clone(self):
        clause = Clause()
        clause.units = [x for x in self.units]
        return clause

    def to_list(self):
        return [unit.to_list() for unit in self.units]

    def __repr__(self):
        s = ''
        if self.units:
            s += str(self.units[0])
            if len(self.units) > 1:
                for unit in self.units[1:]:
                    s += '|'
                    s += str(unit)
        return s

    def get_number_of_units(self):
        return len(self.units)

    def get_units(self):
        return self.units

    def get_unit(self, idx):
        return self.units[idx]

    def add_unit(self, unit):
        self.units.append(unit)

    def remove_unit_at(self, idx):
        self.units.pop(idx)

    def substitute(self, subsList):
        units = [x for x in self.units]
        if subsList:
            for idx, unit in enumerate(units):
                units[idx] = unit.substitute(subsList)
        clause = self.clone()
        clause.units = [x for x in units]
        return clause

    def equal(self, clause):
        if self.get_number_of_units() != clause.get_number_of_units():
            return False

        for idx in range(self.get_number_of_units()):
            if not self.get_unit(idx).equal(clause.get_unit(idx)):
                return False
        return True

    def __eq__(self, clause):
        if self.get_number_of_units() != clause.get_number_of_units():
            return False

        for idx in range(self.get_number_of_units()):
            if not self.get_unit(idx).equal(clause.get_unit(idx)):
                return False
        return True

    def get_constant_symbol(self):
        ret = set()
        for unit in self.units:
            ret.update(unit.get_constant_symbol())
        return ret

    def get_variable(self):
        ret = set()
        for unit in self.units:
            ret.update(unit.get_variable())
        return ret

    def get_ante_cons(self):
        ante = Clause()
        cons = Unit()
        for unit in self.units:
            if unit.negated:
                u = unit.clone()
                u.negate()
                ante.add_unit(u)
            else:
                cons = unit.clone()
        return ante, cons

    def getFirstRest(self):
        rest = Clause()
        units = self.get_units()
        for unit in units[1:]:
            u = unit.clone()
            rest.add_unit(u)
        return units[0], rest

    def standardize_apart(self):
        # print(self)
        variables = self.get_variable()
        mapping = dict()
        for variable in variables:
            suffix = next(variable)
            mapping[variable] = variable + str(suffix)

        standard = Clause()
        for unit in self.units:
            standard.add_unit(unit.substitute(mapping))
        # print(standard)
        return standard

    def negate(self):
        result = Clause()
        for unit in self.units:
            result.add_unit(unit.negate())
        return result

    def __hash__(self):
        clause = tuple()
        for unit in self.units:
            clause += (hash(unit),)
        return hash(clause)