from KnowledgeBase import KnowledgeBase
from ForwardChaining import forward_chain
from BackwardChaining_old import backward_chain
from Resolution import resolution

def main():
    KB = KnowledgeBase()
    KB.consult('input/kb.txt')
    for x in [backward_chain, resolution, forward_chain]:
        print(x.__name__)
        KB.query('input/query.txt', x)

if __name__ == '__main__':
    main()