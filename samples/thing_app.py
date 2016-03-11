import thing as t

def main():
    a = t.Thing(2016)
    b = t.SubThing(2525, 'July')
    #list_of_things = [a, b]
    list_of_things = [a,]
    for item in list_of_things:
        print(item)
    
main()
