class Substitution:
    def __init__(self, mapping):
        self.mapping = mapping
    def __eq__(self, subs):
        return self.mapping == subs
    def __hash__(self):
        t = tuple()
        for k, v in self.mapping.items():
            t += ((k, v),)
        return hash(t)
    def __repr__(self):
        return str(self.mapping)