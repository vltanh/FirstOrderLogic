from Clause import Clause
from Unit import Unit
import time
from ForwardChaining import forward_chain
from BackwardChaining_old import backward_chain
from Resolution import resolution

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

    def query(self, inp, out):
        with open(inp, 'r') as f:
            lines = f.readlines()

        algodict = [forward_chain, backward_chain, resolution]
        with open(out, 'w') as f:
            for line in lines:
                algoid = int(line[0])
                query = Clause.generate_from_string(line[1:])
                print('Query: ', query)
                self.export(f, algodict[algoid], query)
                now = time.time()
                print('Querying takes {} (s)'.format(time.time() - now))

    def export(self, f, algo, query):
        f.write('Query: {} by {}\n'.format(query, algo.__name__))
        for x in algo(self, query):
            f.write('{}\n'.format(x))

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