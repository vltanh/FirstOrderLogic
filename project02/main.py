from KnowledgeBase import KnowledgeBase

def main():
    KB = KnowledgeBase()
    KB.consult('input/kb.txt')
    KB.query('input/query.txt', 'output/result.txt')

if __name__ == '__main__':
    main()