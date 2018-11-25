from Clause import Clause
from Unit import Unit
import time

class KnowledgeBase:
    def __init__(self):
        self.facts = []
        self.rules = []

    def consult(self, dir):
        with open(dir, 'r') as f:
            lines = f.readlines()
            for line in lines:
                temp = Clause.generate_from_string(line)
                if temp.get_number_of_units() == 1:
                    self.facts.append(temp)
                else:
                    self.rules.append(temp)

    def query(self, dir, algo):
        with open(dir, 'r') as f:
            lines = f.readlines()
            for line in lines:
                query = Clause.generate_from_string(line)
                print('Query: ', query)
                now = time.time()
                for x in algo(self, query):
                    print(x)
                print('Querying takes {} (s)'.format(time.time() - now))

    def show(self, show_facts = True, show_rules = True):
        if show_facts:
            print('=== Facts:')
            for fact in self.facts:
                print(fact)
        if show_rules:
            print('=== Rules:')
            for rule in self.rules:
                print(rule)

    def add_fact(self, fact):
        self.facts.append(fact)
    
    def contain_fact(self, fact):
        return fact in self.facts

    def add_rule(self, rule):
        self.rules.append(rule)

    def clone(self):
        KB = KnowledgeBase()
        KB.facts = [x for x in self.facts]
        KB.rules = [x for x in self.rules]
        return KB