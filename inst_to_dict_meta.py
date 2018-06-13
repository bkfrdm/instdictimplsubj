class Meta(type):
    def __call__(cls, *args):
        print('Meta.__call__:', cls, args, sep='\n\t')
        
        data = cls.main(*args)
        
        new_cls = type(
            cls.__name__,
            cls.__bases__,
            {k: v for k, v in cls.__dict__.items() if not k == '__init__'})
        
        instance = new_cls(data)
        for n, v in zip(cls.__init__.__code__.co_names, args):
            # __dict__ descriptor is broken -> TypeError
            setattr(instance, n, v)
            
        return instance

      
class DictTools:
    def pops(self, *keys):
        return {key: self.pop(key) for key in keys}

    
class InstToDict(dict, DictTools, metaclass=Meta):
    def __init__(self, filename):
        self.filename = filename

    @classmethod
    def data_parser(cls, *args):
        filename, = args
        return {c: ord(c) for c in filename}

    @classmethod
    def main(cls, *args):
        filename, = args
        return cls.data_parser(filename)




if __name__ == '__main__':
    filename = 'spam'
    I = InstToDict(filename)

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
