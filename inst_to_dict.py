class meta(type):
    def __new__(meta, classname, supers, classdict):
        print('meta.__new__:', meta, classname, supers, classdict, sep='\n......... ')
        return type.__new__(meta, classname, supers, classdict)
    
    def __init__(*args):
        print('meta.__init_:', *args, sep='\n......... ')
    
    def __call__(Class, val):
        global _val
        _val = val
        print('meta.__call__:', Class, val, sep='\n......... ')
        D = {v: ord(v) for v in val}
        class Sup(Tools, dict):
            filename = _val
            # callable instance / try filename to __init__ to get rid of global stmt
            
        return type.__call__(Sup, D)
      
class Tools:
    def pops(self, *args):
        poped = {}
        for arg in args:
            poped[arg] = self.pop(arg)
        return poped

    
class C(metaclass=meta):
    def __init__(self, filename):
        self.filename = filename




if __name__ == '__main__':
    filename = 'spam'
    I = C(filename)

    print('-'*50, '\ndefined class instance returns dict object')
    
    assert I == {k: ord(k) for k in 'spam'}, f'Failed I: {I}'
    print('I:', I, end='\n\n')

    print('-'*50, '\ndefined class instance __init__ value persists')
    
    assert I.filename == filename, f'Failed I.filename: {I.filname}'
    print('I.filename:', I.filename, end='\n\n')


    print('-'*50, '\ndefined class mixin methods inhereted')
    
    popped = I.pops('a', 'm')
    test = {k: ord(k) for k in 'am'}
    assert popped == test, f'Failed I.pops: {popped} != {test}'
    print('I.pops:', popped, end='\n\n')

    test = {k: ord(k) for k in 'sp'}
    assert I == test, f'Failed I: {I} != {test}'
    print('I:', I, end='\n\n')


    print('-'*50, '\ndict class builtins inhereted')

    I.update(f=56, q=55)
    test = {'s': 115, 'p': 112, 'f': 56, 'q': 55}
    assert I == test, f'Failed I: {I} != {test}'
    print('I.update:', I, end='\n\n')
    
    poped = I.pop('q')
    test = {'s': 115, 'p': 112, 'z': 56, 'q': 55}.pop('q')
    assert poped == test, f'Failed I.pop: {poped} != {test}'
    print('I.pop:', poped)
    print('I:', I, end='\n\n')
