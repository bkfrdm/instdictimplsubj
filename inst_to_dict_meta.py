class MetaDict(type):
    def __new__(meta, classname, supers, classdict):
        for attr, val in classdict.items():
            if not attr.startswith('__') and callable(val):
                classdict[attr] = classmethod(val)

        return type.__new__(meta, classname, supers, classdict)
            
    def __call__(cls, *args):
        data = cls.main(*args)
        
        new_cls = type(
            cls.__name__,
            cls.__bases__,
            {k: v for k, v in cls.__dict__.items() if not k == '__init__'})
        
        instance = new_cls(data)
        instance = cls.rebind_init_values(instance, *args)
        
        return instance

    def rebind_init_values(cls, instance, *args):
        for n, v in zip(cls.__init__.__code__.co_names, args):
            # __dict__ descriptor is broken -> TypeError
            setattr(instance, n, v)

        return instance

      
class DictToolsMix:
    def pops(self, *keys):
        return {key: self.pop(key) for key in keys}


class InstToDict(dict, DictToolsMix, metaclass=MetaDict):
    def __init__(self, filename):
        self.filename = filename

    def data_parser(cls, *args):
        filename, = args
        return {c: ord(c) for c in filename}

    def main(cls, *args):
        filename, = args
        return cls.data_parser(filename)



if __name__ == '__main__':
    i = InstToDict('spam')
    print(i, type(i), isinstance(i, dict), sep='\n')
