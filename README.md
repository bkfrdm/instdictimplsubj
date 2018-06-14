    # instance returns dict object
    >>> i = InstToDict('spam')
    >>> i                                                 
    {'s': 115, 'p': 112, 'a': 97, 'm': 109}

    # instance retains dict builtin methods
    >>> i.update({'ni': 'HI'})                            
    >>> i 
    {'s': 115, 'p': 112, 'a': 97, 'm': 109, 'ni': 'HI'}

    # instance retains mixin methods
    >>> i.pops('s', 'ni', 'a')                            
    {'s': 115, 'ni': 'HI', 'a': 97}
    >>> i
    {'p': 112, 'm': 109}

    # instance retains initialize values
    >>> i.filename                                        
    'spam'
