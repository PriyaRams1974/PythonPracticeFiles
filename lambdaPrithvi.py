def transform(x):
    return x.upper()


def  main():
    animals = ['dog', 'cat', 'parrot', 'rabbit']

    transformFn = lambda x : x.upper()
    
    print(list(map(transform, animals)))
    print(list(map(transformFn, animals)))
    
    
main()