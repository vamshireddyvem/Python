def outer():
    print('Hello this is outer')
    def inner(name):
        return print('hello this is Inner',name)
    return inner

something=outer()
print(something('vamshi'))
