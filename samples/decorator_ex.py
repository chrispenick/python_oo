def verbose(original_function):

    #make a new function that prints when the original_function
    def new_function(*args, **kwargs):
        print("Entering", original_function.__name__)
        original_function(*args, **kwargs)
        print("Exiting", original_function.__name__)
        
    return new_function

@verbose
def widget_func(arg):
    print('Bob', arg)
    

